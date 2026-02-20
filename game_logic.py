def init_game(session):
    """Полный сброс состояния игры"""
    session['current_scene'] = 'start'
    session['inventory'] = []
    session['companions'] = []
    session['ds_victories'] = 0
    # По умолчанию язык русский, если не был установлен ранее
    # (можно сохранить язык, если нужно, но session.clear() удалит всё)
    session['current_lang'] = 'ru'

def update_game_state(session, scene_data):
    state_changed = False
    
    if 'loot' in scene_data:
        for item in scene_data['loot']:
            if item not in session['inventory']:
                session['inventory'].append(item)
                state_changed = True
    
    if 'consume_loot' in scene_data:
        for item in scene_data['consume_loot']:
            if item in session['inventory']:
                session['inventory'].remove(item)
                state_changed = True
    
    if 'new_companion' in scene_data:
        companion = scene_data['new_companion']
        if companion not in session['companions']:
            session['companions'].append(companion)
            state_changed = True
            
    if state_changed:
        session.modified = True

def process_turn(session, scenarios_dict, next_scene_id, current_lang):
    """Отрабатывает переход на новую сцену, включая случайные исходы"""
    import random
    
    # Сброс игры если мы вернулись в start (Конец игры)
    if next_scene_id == 'start':
        current_lang_saved = session.get('current_lang', 'ru')
        init_game(session)
        session['current_lang'] = current_lang_saved
        return 'start'
        
    lang_scenarios = scenarios_dict.get(current_lang, {})
    if next_scene_id in lang_scenarios:
        # Обновляем состояние инвентаря/спутников на основе текущей сцены
        current_scene_data = lang_scenarios.get(session.get('current_scene', 'start'))
        if current_scene_data:
            update_game_state(session, current_scene_data)
        
        # Проверяем нет ли случайных исходов в следующей сцене
        next_scene_data = lang_scenarios[next_scene_id]
        if 'random_outcomes' in next_scene_data:
            outcomes = next_scene_data['random_outcomes']
            if isinstance(outcomes, list):
                result_scene = random.choice(outcomes)
                
                # Специальная механика для Dark Souls (3 победы)
                if result_scene == "darksouls_victory":
                    session['ds_victories'] = session.get('ds_victories', 0) + 1
                    if session['ds_victories'] < 3:
                        result_scene = 'darksouls_fight_again'
                        
                next_scene_id = result_scene
        
        session['current_scene'] = next_scene_id
        return next_scene_id
        
    return 'start'

def get_filtered_scene(scene, session):
    """Возвращает сцену, где кнопки выбора отфильтрованы по условиям (наличие спутника)"""
    filtered_scene = scene.copy()
    if 'choices' in filtered_scene:
        filtered_choices = []
        for choice in filtered_scene['choices']:
            if 'condition' not in choice or choice['condition'](session):
                filtered_choices.append(choice)
        filtered_scene['choices'] = filtered_choices
    return filtered_scene
