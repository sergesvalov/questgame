import os
from flask import Flask, render_template, session, redirect, url_for, request
from data import SCENARIOS, LANGUAGES, KNIGHT_ART

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key_change_me')

def init_game():
    """Полный сброс состояния игры"""
    session.clear()
    session['current_scene'] = 'start'
    session['inventory'] = []
    session['companions'] = []
    # По умолчанию язык русский, если не был установлен ранее
    # (можно сохранить язык, если нужно, но session.clear() удалит всё)
    session['current_lang'] = 'ru'

def update_game_state(scene_data):
    if 'loot' in scene_data:
        for item in scene_data['loot']:
            if item not in session['inventory']:
                session['inventory'].append(item)
    
    if 'consume_loot' in scene_data:
        for item in scene_data['consume_loot']:
            if item in session['inventory']:
                session['inventory'].remove(item)
    
    if 'new_companion' in scene_data:
        companion = scene_data['new_companion']
        if companion not in session['companions']:
            session['companions'].append(companion)

@app.route('/game', methods=['GET', 'POST'])
def game():
    # 1. Рестарт через кнопку в меню
    if request.args.get('restart'):
        init_game()
        return redirect(url_for('game'))

    # 2. Инициализация, если сессия пуста
    if 'current_scene' not in session:
        init_game()

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
                init_game()
                session['current_lang'] = current_lang_saved
                return redirect(url_for('game'))

            # Обычный переход
            if next_scene_id in SCENARIOS.get(current_lang, {}):
                current_scene_data = SCENARIOS[current_lang][session['current_scene']]
                update_game_state(current_scene_data)
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

    return render_template(
        'index.html',
        scene=scene,
        inventory=session.get('inventory', []),
        companions=session.get('companions', []),
        current_lang=current_lang,
        languages=LANGUAGES,
        knight_art=KNIGHT_ART
    )

@app.route('/')
def index():
    return redirect(url_for('game'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)