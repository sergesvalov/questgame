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
