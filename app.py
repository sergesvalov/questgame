import os
from flask import Flask, render_template, session, redirect, url_for, request
from data import LANGUAGES, KNIGHT_ART, UI_TRANSLATIONS
from scenarios import SCENARIOS
from game_logic import init_game, update_game_state

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key_change_me')



@app.route('/game', methods=['GET', 'POST'])
def game():
    # 1. Рестарт через кнопку в меню
    if request.args.get('restart'):
        init_game(session)
        return redirect(url_for('game'))

    # 2. Инициализация, если сессия пуста
    if 'current_scene' not in session:
        init_game(session)

    # 3. Обработка хода игрока
    if request.method == 'POST':
        next_scene_id = request.form.get('next_scene')
        current_lang = session.get('current_lang', 'ru')
        
        if next_scene_id:
            # === ИСПРАВЛЕНИЕ: СБРОС ПРИ ПЕТЛЕ ВРЕМЕНИ ===
            # Если переход ведет в 'start', мы делаем полный сброс (init_game),
            # чтобы очистить инвентарь и спутников.
            if next_scene_id == 'start':
                # Сохраним текущий язык перед очисткой, чтобы не сбрасывался на RU
                current_lang_saved = session.get('current_lang', 'ru')
                init_game(session)
                session['current_lang'] = current_lang_saved
                return redirect(url_for('game'))

            # Обычный переход
            if next_scene_id in SCENARIOS.get(current_lang, {}):
                current_scene_data = SCENARIOS[current_lang][session['current_scene']]
                update_game_state(session, current_scene_data)
                # Check if next scene has random outcomes
                next_scene_data = SCENARIOS[current_lang][next_scene_id]
                if 'random_outcomes' in next_scene_data:
                    import random
                    outcomes = next_scene_data['random_outcomes']
                    if isinstance(outcomes, list):
                        result_scene = random.choice(outcomes)
                        if result_scene == "darksouls_victory":
                            session['ds_victories'] = session.get('ds_victories', 0) + 1
                            if session['ds_victories'] < 3:
                                result_scene = 'darksouls_fight_again'
                        next_scene_id = result_scene
                
                session['current_scene'] = next_scene_id

    # 4. Смена языка
    requested_lang = request.args.get('lang')
    if requested_lang and requested_lang in LANGUAGES:
        session['current_lang'] = requested_lang
        return redirect(url_for('game'))

    # 5. Подготовка данных для отображения
    current_lang = session.get('current_lang', 'ru')
    scene_id = session.get('current_scene', 'start')
    lang_scenarios = SCENARIOS.get(current_lang, SCENARIOS['ru'])
    
    # Защита от несуществующей сцены
    scene = lang_scenarios.get(scene_id, lang_scenarios['start'])
    
    # Filter choices based on conditions if they exist
    filtered_scene = scene.copy()
    if 'choices' in filtered_scene:
        filtered_choices = []
        for choice in filtered_scene['choices']:
            if 'condition' not in choice or choice['condition'](session):
                filtered_choices.append(choice)
        filtered_scene['choices'] = filtered_choices

    return render_template(
        'index.html',
        scene=filtered_scene,
        inventory=session.get('inventory', []),
        companions=session.get('companions', []),
        current_lang=current_lang,
        languages=LANGUAGES,
        knight_art=KNIGHT_ART,
        ui=UI_TRANSLATIONS.get(current_lang, UI_TRANSLATIONS['ru'])
    )

@app.route('/')
def index():
    return redirect(url_for('game'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)