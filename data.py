LANGUAGES = {
    'ru': 'Русский',
    'en': 'English',
    'el': 'Ελληνικά'
}

# Арт: Герб (Щит с крестом)
KNIGHT_ART = r"""
      _______
     /       \
    |    |    |
    |  --+--  |
    |    |    |
     \       /
      \     /
       \___/
"""

SCENARIOS = {
    'ru': {
        # === ПРОЛОГ ===
        "start": {
            "text": (
                "Сознание возвращается рывками. Вы лежите на сырой земле. "
                "Имя «Сэр Галахад» пульсирует в голове, но вы ничего не помните. Коня нет. "
                "Тропа расходится надвое."
            ),
            "image_type": "intro",
            "question": "Лес давит своим величием.",
            "choices": [
                {"label": "Искать следы коня", "next_scene": "find_horse_start"},
                {"label": "Пойти по тропе", "next_scene": "meet_dwarves"},
                {"label": "Ждать помощи", "next_scene": "stay_sad"}
            ]
        },

        # === ВЕТКА 1: МУДРЕЦ ===
        "stay_sad": {
            "text": "В сумерках раздается рык монстра! Сидеть здесь — значит умереть.",
            "choices": [{"label": "Вскочить и бежать", "next_scene": "run_to_edge"}]
        },
        "run_to_edge": {
            "text": "Вы выбегаете на опушку. Впереди огни города.",
            "choices": [{"label": "Подойти к страже", "next_scene": "city_arrest"}]
        },
        "city_arrest": {
            "text": "Стража у ворот не пускает вас. Вы выглядите как бродяга.",
            "choices": [{"label": "Сдаться", "next_scene": "dungeon_cell"}]
        },
        "dungeon_cell": {
            "text": "В тюремной камере вы понимаете, что потеря памяти — это проклятие. Один камень в стене шатается.",
            "choices": [{"label": "Навалиться на камень", "next_scene": "secret_passage"}]
        },
        "secret_passage": {
            "text": "Через канализацию вы выбираетесь наружу, грязный, но свободный.",
            "choices": [{"label": "Осмотреться", "next_scene": "meet_sage"}]
        },
        "meet_sage": {
            "text": "— Я Алексей. Твою память украл Темный Алхимик. Я помогу тебе.",
            "new_companion": "Мудрец Алексей",
            "choices": [{"label": "Уйти с Алексеем", "next_scene": "sage_stream_journey"}]
        },
        "sage_stream_journey": {
            "text": "Вы идете с Алексеем до полудня и выходите к ручью.",
            "choices": [{"label": "Сделать привал", "next_scene": "sage_stream_lunch"}]
        },
        "sage_stream_lunch": {
            "text": "Алексей делится с вами едой. Вы смотрите в воду и не узнаете своего лица.",
            "choices": [{"label": "Продолжить путь", "next_scene": "stone_crossroad_sage"}]
        },
        "stone_crossroad_sage": {
            "text": "Вы у камня. Надпись: 'ЗАКОЛДОВАННЫМ — НАПРАВО. БЕЗЛОШАДНЫМ — НАЛЕВО'.",
            "choices": [
                {"label": "Направо (Путь заколдованных)", "next_scene": "path_enchanted"},
                {"label": "Налево (Путь безлошадных)", "next_scene": "path_horseless"}
            ]
        },

        # === ВЕТКА 2: КОНЬ ===
        "find_horse_start": {
            "text": "Под кустом вы находите свою сумку с кинжалом и хлебом.",
            "loot": ["Старый кинжал", "Черствый хлеб"],
            "choices": [{"label": "Идти по следам", "next_scene": "horse_found"}]
        },
        "horse_found": {
            "text": "На поляне вы находите своего коня! На седле: меч, вода и сало.",
            "loot": ["Меч рыцаря", "Фляга с водой", "Кусок сала"],
            "choices": [{"label": "Ускакать прочь", "next_scene": "ride_away_river"}]
        },
        "ride_away_river": {
            "text": "Вы скачете прочь от леса. Спустя часы вы останавливаетесь у ручья.",
            "choices": [{"label": "Пообедать", "next_scene": "stream_rest"}]
        },
        "stream_rest": {
            "text": "Вы съедаете хлеб. Память стерта. Вы в отчаянии, но конь рядом.",
            "consume_loot": ["Черствый хлеб"],
            "choices": [{"label": "Ехать дальше", "next_scene": "stone_crossroad_horse"}]
        },
        "stone_crossroad_horse": {
            "text": "Вы у камня. 'ЗАКОЛДОВАННЫМ — НАПРАВО. БЕЗЛОШАДНЫМ — НАЛЕВО'.",
            "choices": [
                {"label": "Направо (Путь заколдованных)", "next_scene": "path_enchanted"},
                {"label": "Налево (Путь безлошадных)", "next_scene": "path_horseless"}
            ]
        },

        # === ВЕТКА 3: ГНОМЫ ===
        "meet_dwarves": {
            "text": "Гномы убегают, бросая золото. Холодает.",
            "loot": ["Мешочек золота"],
            "choices": [
                {"label": "Спать (замерзнуть)", "next_scene": "sleep_cold"},
                {"label": "Развести костер", "next_scene": "dwarf_village"}
            ]
        },
        "sleep_cold": {"text": "...", "choices": [{"label": "...", "next_scene": "city_arrest"}]},
        "dwarf_village": {
            "text": "Вы находите деревню гномов. Старейшина встречает вас.",
            "choices": [{"label": "Вернуть золото", "next_scene": "dwarf_feast"}]
        },
        "dwarf_feast": {
            "text": "На пиру вас спрашивают о прошлом, но вы не помните ничего.",
            "loot": ["Эль гномов", "Жареная рулька"],
            "choices": [{"label": "Признаться", "next_scene": "dwarf_sleep"}]
        },
        "dwarf_sleep": {
            "text": "Вас отправляют спать.",
            "choices": [{"label": "Проснуться", "next_scene": "dwarf_morning"}]
        },
        "dwarf_morning": {
            "text": "Утром Старейшина дает вам в помощь следопыта Балина.",
            "choices": [{"label": "В путь!", "next_scene": "dwarf_hike_start"}]
        },
        "dwarf_hike_start": {
            "text": "Балин проверяет арбалет. Вы выходите за ворота деревни гномов.",
            "new_companion": "Следопыт Балин",
            "choices": [{"label": "Отправиться в путь", "next_scene": "dwarf_night_camp"}]
        },
        "dwarf_night_camp": {
            "text": "Вы с Балином устраиваете привал в гроте.",
            "choices": [{"label": "Попытаться уснуть", "next_scene": "dwarf_theft_attempt"}]
        },
        "dwarf_theft_attempt": {
            "text": "Ночью вас будит царапающий звук. Мелкие воры!",
            "choices": [{"label": "Отогнать воришек", "next_scene": "stone_crossroad_dwarf"}]
        },
        "stone_crossroad_dwarf": {
            "text": "Вы у камня. 'ЗАКОЛДОВАННЫМ — НАПРАВО. БЕЗЛОШАДНЫМ — НАЛЕВО'.",
            "choices": [
                {"label": "Направо (Путь заколдованных)", "next_scene": "path_enchanted"},
                {"label": "Налево (Путь безлошадных)", "next_scene": "path_horseless"}
            ]
        },

        # === ФИНАЛЫ ===
        "path_enchanted": {
            "text": "Вы сворачиваете направо. Воздух здесь густой и пахнет магией.",
            "choices": [{"label": "Продолжить путь", "next_scene": "tower_found"}]
        },
        "tower_found": {
            "text": "Вы выходите к Башне Темного Алхимика.",
            "image_type": "tower",
            "choices": [
                {"label": "Войти в Башню", "next_scene": "tower_entrance"},
                {"label": "Искать другой вход", "next_scene": "tower_side_entrance"}
            ]
        },
        "tower_entrance": {
            "text": "Вы входите в темный зал. (Сюжет в разработке)",
            "choices": []
        },
        "tower_side_entrance": {
            "text": "Вы находите подвал. (Сюжет в разработке)",
            "choices": []
        },

        # === ПЕТЛЯ ВРЕМЕНИ (ЛЕВЫЙ ПУТЬ) ===
        "path_horseless": {
            "text": "Вы выбираете левую дорогу. Лес кажется мирным, но с закатом приходит тьма.",
            "choices": [{"label": "Ехать дальше", "next_scene": "ambush_loop_hit"}]
        },
        "ambush_loop_hit": {
            "text": "Внезапно! Удар по голове выбивает вас из сознания. Кто-то хихикает и убегает. Тьма...",
            "choices": [{"label": "Очнуться", "next_scene": "start"}] # ВОЗВРАТ В НАЧАЛО
        }
    },
    
    'en': {
        "start": {
            "text": "You wake up on damp earth. No memory. No horse.",
            "image_type": "intro",
            "question": "What do you do?",
            "choices": [
                {"label": "Find horse", "next_scene": "find_horse_start"},
                {"label": "Walk path", "next_scene": "meet_dwarves"},
                {"label": "Wait", "next_scene": "stay_sad"}
            ]
        },
        "stay_sad": {"text": "Monster!", "choices": [{"label": "Run", "next_scene": "run_to_edge"}]},
        "run_to_edge": {"text": "City lights.", "choices": [{"label": "Guards", "next_scene": "city_arrest"}]},
        "city_arrest": {"text": "Arrested.", "choices": [{"label": "Jail", "next_scene": "dungeon_cell"}]},
        "dungeon_cell": {"text": "Cell.", "choices": [{"label": "Escape", "next_scene": "secret_passage"}]},
        "secret_passage": {"text": "Old man.", "choices": [{"label": "Who?", "next_scene": "meet_sage"}]},
        "meet_sage": {"text": "I am Alexei.", "new_companion": "Sage Alexei", "choices": [{"label": "Go", "next_scene": "sage_stream_journey"}]},
        "sage_stream_journey": {"text": "Stream.", "choices": [{"label": "Rest", "next_scene": "sage_stream_lunch"}]},
        "sage_stream_lunch": {"text": "Lunch.", "choices": [{"label": "Go", "next_scene": "stone_crossroad_sage"}]},
        "stone_crossroad_sage": {"text": "Stone: Enchanted Right.", "choices": [{"label": "Right", "next_scene": "path_enchanted"}, {"label": "Left", "next_scene": "path_horseless"}]},
        "find_horse_start": {"text": "Found bag.", "loot": ["Dagger", "Bread"], "choices": [{"label": "Track", "next_scene": "horse_found"}]},
        "horse_found": {"text": "Found horse!", "loot": ["Sword", "Water"], "choices": [{"label": "Ride", "next_scene": "ride_away_river"}]},
        "ride_away_river": {"text": "Stream stop.", "choices": [{"label": "Eat", "next_scene": "stream_rest"}]},
        "stream_rest": {"text": "Ate bread.", "consume_loot": ["Bread"], "choices": [{"label": "Go", "next_scene": "stone_crossroad_horse"}]},
        "stone_crossroad_horse": {"text": "Stone on horse.", "choices": [{"label": "Right", "next_scene": "path_enchanted"}, {"label": "Left", "next_scene": "path_horseless"}]},
        "meet_dwarves": {"text": "Dwarves ran.", "loot": ["Gold"], "choices": [{"label": "Village", "next_scene": "dwarf_village"}]},
        "dwarf_village": {"text": "Village.", "choices": [{"label": "Feast", "next_scene": "dwarf_feast"}]},
        "dwarf_feast": {"text": "Feast.", "loot": ["Ale"], "choices": [{"label": "Sleep", "next_scene": "dwarf_sleep"}]},
        "dwarf_sleep": {"text": "Sleep.", "choices": [{"label": "Wake", "next_scene": "dwarf_morning"}]},
        "dwarf_morning": {"text": "Balin joins.", "new_companion": "Balin", "choices": [{"label": "Hike", "next_scene": "stone_crossroad_dwarf"}]},
        "stone_crossroad_dwarf": {"text": "Stone with Balin.", "choices": [{"label": "Right", "next_scene": "path_enchanted"}, {"label": "Left", "next_scene": "path_horseless"}]},
        "path_enchanted": {"text": "Magic air.", "choices": [{"label": "Tower", "next_scene": "tower_found"}]},
        "tower_found": {"text": "Dark Tower.", "image_type": "tower", "choices": [{"label": "Enter", "next_scene": "tower_entrance"}]},
        "tower_entrance": {"text": "Inside.", "choices": []},
        
        # TIME LOOP (LEFT PATH)
        "path_horseless": {
            "text": "You go left. The path gets unnaturally dark.",
            "choices": [{"label": "Ride on", "next_scene": "ambush_loop_hit"}]
        },
        "ambush_loop_hit": {
            "text": "Hit to the head! You black out...",
            "choices": [{"label": "Wake up", "next_scene": "start"}]
        }
    },
    'el': {
        "start": {
            "text": "Ξυπνάτε. Δεν θυμάστε τίποτα.",
            "image_type": "intro",
            "question": "Τι κάνετε;",
            "choices": [
                {"label": "Ψάξτε άλογο", "next_scene": "find_horse_start"},
                {"label": "Μονοπάτι", "next_scene": "meet_dwarves"},
                {"label": "Περιμένετε", "next_scene": "stay_sad"}
            ]
        },
        "stay_sad": {"text": "Τέρας!", "choices": [{"label": "Τρέξτε", "next_scene": "run_to_edge"}]},
        "run_to_edge": {"text": "Πόλη.", "choices": [{"label": "Φρουροί", "next_scene": "city_arrest"}]},
        "city_arrest": {"text": "Σύλληψη.", "choices": [{"label": "Φυλακή", "next_scene": "dungeon_cell"}]},
        "dungeon_cell": {"text": "Κελί.", "choices": [{"label": "Απόδραση", "next_scene": "secret_passage"}]},
        "secret_passage": {"text": "Γέρος.", "choices": [{"label": "Ποιος;", "next_scene": "meet_sage"}]},
        "meet_sage": {"text": "Είμαι ο Αλέξιος.", "new_companion": "Σοφός Αλέξιος", "choices": [{"label": "Πάμε", "next_scene": "sage_stream_journey"}]},
        "sage_stream_journey": {"text": "Ρυάκι.", "choices": [{"label": "Ξεκούραση", "next_scene": "sage_stream_lunch"}]},
        "sage_stream_lunch": {"text": "Φαγητό.", "choices": [{"label": "Πάμε", "next_scene": "stone_crossroad_sage"}]},
        "stone_crossroad_sage": {"text": "Πέτρα: Μαγεμένοι Δεξιά.", "choices": [{"label": "Δεξιά", "next_scene": "path_enchanted"}, {"label": "Αριστερά", "next_scene": "path_horseless"}]},
        "find_horse_start": {"text": "Τσάντα.", "loot": ["Στιλέτο", "Ψωμί"], "choices": [{"label": "Ίχνη", "next_scene": "horse_found"}]},
        "horse_found": {"text": "Άλογο!", "loot": ["Σπαθί", "Νερό"], "choices": [{"label": "Φύγε", "next_scene": "ride_away_river"}]},
        "ride_away_river": {"text": "Στάση.", "choices": [{"label": "Φάε", "next_scene": "stream_rest"}]},
        "stream_rest": {"text": "Έφαγες.", "consume_loot": ["Ψωμί"], "choices": [{"label": "Δρόμος", "next_scene": "stone_crossroad_horse"}]},
        "stone_crossroad_horse": {"text": "Πέτρα με άλογο.", "choices": [{"label": "Δεξιά", "next_scene": "path_enchanted"}, {"label": "Αριστερά", "next_scene": "path_horseless"}]},
        "meet_dwarves": {"text": "Νάνοι.", "loot": ["Χρυσός"], "choices": [{"label": "Χωριό", "next_scene": "dwarf_village"}]},
        "dwarf_village": {"text": "Χωριό.", "choices": [{"label": "Γιορτή", "next_scene": "dwarf_feast"}]},
        "dwarf_feast": {"text": "Γιορτή.", "loot": ["Μπύρα"], "choices": [{"label": "Ύπνος", "next_scene": "dwarf_sleep"}]},
        "dwarf_sleep": {"text": "Ύπνος.", "choices": [{"label": "Ξύπνα", "next_scene": "dwarf_morning"}]},
        "dwarf_morning": {"text": "Μπαλίν.", "new_companion": "Μπαλίν", "choices": [{"label": "Ταξίδι", "next_scene": "stone_crossroad_dwarf"}]},
        "stone_crossroad_dwarf": {"text": "Πέτρα με Μπαλίν.", "choices": [{"label": "Δεξιά", "next_scene": "path_enchanted"}, {"label": "Αριστερά", "next_scene": "path_horseless"}]},
        "path_enchanted": {"text": "Μαγεία.", "choices": [{"label": "Πύργος", "next_scene": "tower_found"}]},
        "tower_found": {"text": "Σκοτεινός Πύργος.", "image_type": "tower", "choices": [{"label": "Μπες", "next_scene": "tower_entrance"}]},
        "tower_entrance": {"text": "Μέσα.", "choices": []},
        
        # TIME LOOP (LEFT PATH)
        "path_horseless": {
            "text": "Πάτε αριστερά. Σκοτάδι.",
            "choices": [{"label": "Προχώρα", "next_scene": "ambush_loop_hit"}]
        },
        "ambush_loop_hit": {
            "text": "Χτύπημα στο κεφάλι! Λιποθυμάτε...",
            "choices": [{"label": "Ξυπνήστε", "next_scene": "start"}]
        }
    }
}