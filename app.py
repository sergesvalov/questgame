import json
from flask import Flask, render_template, session, redirect, url_for, request
from data import SCENARIOS, LANGUAGES, KNIGHT_ART

app = Flask(__name__)
# В реальном приложении этот ключ должен быть длинным, сложным и храниться в секрете!
app.secret_key = 'your_super_secret_key_for_session_management'

# Инициализация игрового состояния в сессии
def init_game():
    """Устанавливает начальное состояние игры."""
    session.clear()
    session['current_scene'] = 'start'
    session['inventory'] = []
    session['companions'] = []
    # Устанавливаем язык по умолчанию на русский
    session['current_lang'] = 'ru'
    print("Игра инициализирована/перезапущена.")

# --- Вспомогательные функции для управления состоянием ---

def update_inventory_and_companions(scene_data):
    """Обновляет инвентарь и спутников на основе данных текущей сцены."""
    # Добавление предметов
    if 'loot' in scene_data:
        for item in scene_data['loot']:
            if item not in session['inventory']:
                session['inventory'].append(item)
    
    # Удаление (потребление) предметов
    if 'consume_loot' in scene_data:
        for item in scene_data['consume_loot']:
            if item in session['inventory']:
                session['inventory'].remove(item)
    
    # Добавление спутника
    if 'new_companion' in scene_data:
        companion = scene_data['new_companion']
        if companion not in session['companions']:
            session['companions'].append(companion)


# --- Основной маршрут игры ---

@app.route('/game', methods=['GET', 'POST'])
def game():
    # 1. Обработка перезапуска
    if request.args.get('restart'):
        init_game()
        return redirect(url_for('game'))

    # 2. Инициализация, если сессия пуста
    if 'current_scene' not in session:
        init_game()

    # 3. Обработка выбора (POST запрос)
    if request.method == 'POST':
        next_scene_id = request.form.get('next_scene')
        current_lang = session.get('current_lang', 'ru')
        
        # Проверка на существование следующей сцены
        if next_scene_id and next_scene_id in SCENARIOS.get(current_lang, {}):
            # Получаем данные текущей сцены для применения эффектов ПЕРЕД сменой сцены
            current_scene_data = SCENARIOS[current_lang][session['current_scene']]
            update_inventory_and_companions(current_scene_data)
            
            # Обновляем текущую сцену
            session['current_scene'] = next_scene_id
        else:
            print(f"ОШИБКА: Недействительная или отсутствующая сцена: {next_scene_id}")
            # Если сцена не найдена, остаемся на текущей сцене, чтобы не сломать игру.
    
    # 4. Обработка смены языка (GET параметр)
    requested_lang = request.args.get('lang')
    if requested_lang and requested_lang in LANGUAGES:
        # Пытаемся сохранить текущую сцену при смене языка
        session['current_lang'] = requested_lang
        # Перенаправляем, чтобы избавиться от параметра lang в URL
        return redirect(url_for('game'))

    # 5. Получение данных для рендеринга
    current_lang = session.get('current_lang', 'ru')
    scene_id = session.get('current_scene', 'start')
    
    # Получаем словарь сценариев для текущего языка
    lang_scenarios = SCENARIOS.get(current_lang, SCENARIOS['ru'])
    
    # Получаем данные текущей сцены. Если сцена не найдена (например, ошибка в data.py), 
    # используем начальную сцену как запасной вариант.
    scene = lang_scenarios.get(scene_id, lang_scenarios['start'])

    # 6. Рендеринг шаблона
    return render_template(
        'index.html',
        scene=scene,
        inventory=session.get('inventory', []),
        companions=session.get('companions', []),
        current_lang=current_lang,
        languages=LANGUAGES,
        knight_art=KNIGHT_ART
    )

if __name__ == '__main__':
    # В продакшене используйте Gunicorn или другой WSGI-сервер
    # Для разработки запускаем с включенным дебагом
    app.run(debug=True)