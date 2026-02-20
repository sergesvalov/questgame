import os
from flask import Flask, render_template, session, redirect, url_for, request
from data import LANGUAGES, UI_TRANSLATIONS
from scenarios import SCENARIOS
from game_logic import init_game, process_turn, get_filtered_scene

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
            process_turn(session, SCENARIOS, next_scene_id, current_lang)
            return redirect(url_for('game'))

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
    filtered_scene = get_filtered_scene(scene, session)

    return render_template(
        'index.html',
        scene=filtered_scene,
        inventory=session.get('inventory', []),
        companions=session.get('companions', []),
        current_lang=current_lang,
        languages=LANGUAGES,
        ui=UI_TRANSLATIONS.get(current_lang, UI_TRANSLATIONS['ru'])
    )

@app.route('/')
def index():
    return redirect(url_for('game'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)