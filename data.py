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
                "Сознание возвращается рывками, каждый вдох отдается тупой болью в висках. "
                "Вы лежите на сырой, пахнущей прелью земле, а над головой шумят кроны вековых сосен. "
                "Имя «Сэр Галахад» пульсирует в голове, но оно кажется чужим, словно из прошлой жизни. "
                "Вашего верного коня нет рядом, лишь сломанные ветки указывают на борьбу. "
                "Старая тропа, едва заметная в сумерках, расходится надвое."
            ),
            "image_type": "intro",
            "question": "Лес давит своим мрачным величием. Нужно решаться.",
            "choices": [
                {"label": "Осмотреться в поисках следов коня", "next_scene": "find_horse_start"},
                {"label": "Решительно двинуться по тропе", "next_scene": "meet_dwarves"},
                {"label": "Сил нет. Остаться на месте и ждать", "next_scene": "stay_sad"}
            ]
        },

        # === ВЕТКА 1: МУДРЕЦ АЛЕКСЕЙ ===
        "stay_sad": {
            "text": (
                "Вы остаетесь сидеть, обхватив колени руками, пока сгущается тьма. "
                "Внезапно совсем рядом раздается гортанный рык, от которого кровь стынет в жилах! "
                "Огромная тень отделяется от деревьев. Оставаться здесь — верная смерть."
            ),
            "choices": [{"label": "Вскочить и бежать без оглядки", "next_scene": "run_to_edge"}]
        },
        "run_to_edge": {
            "text": (
                "Ветки хлещут вас по лицу, пока вы несетесь сквозь чащу, не разбирая дороги. "
                "Дыхание сбивается, но вы вырываетесь на опушку. "
                "Впереди, спасительным маяком, мерцают огни крепостных стен города."
            ),
            "choices": [{"label": "Подойти к городской страже", "next_scene": "city_arrest"}]
        },
        "city_arrest": {
            "text": (
                "Вы бросаетесь к воротам, но путь преграждают алебарды. "
                "Стражники с презрением осматривают ваш изодранный камзол. "
                "— Бродягам здесь не место, — рявкает сержант. — В темнице разберемся, кто ты такой."
            ),
            "choices": [{"label": "Сил для спора нет. Сдаться", "next_scene": "dungeon_cell"}]
        },
        "dungeon_cell": {
            "text": (
                "Сырая камера пахнет плесенью и безнадежностью. "
                "Сидя на соломе, вы понимаете, что потеря памяти — это магическое проклятие, блокирующее разум. "
                "От злости вы ударяете по стене и замечаете, что один камень шатается."
            ),
            "choices": [{"label": "Навалиться на камень плечом", "next_scene": "secret_passage"}]
        },
        "secret_passage": {
            "text": (
                "Камень поддается, открывая смрадный лаз в старую канализацию. "
                "Вы ползете в темноте, сдирая локти, и наконец выбираетесь наружу, в крепостной ров. "
                "Вы грязны, измотаны, но наконец-то свободны."
            ),
            "choices": [{"label": "Отряхнуться и осмотреться", "next_scene": "meet_sage"}]
        },
        "meet_sage": {
            "text": (
                "Из тени стены выступает фигура в сером плаще с посохом. Глаза старика светятся мудростью. "
                "— Здравствуй, Галахад. Я Алексей, — тихо говорит он. — Твою память украл Темный Алхимик. "
                "Я ждал тебя, чтобы помочь восстановить справедливость."
            ),
            "new_companion": "Мудрец Алексей",
            "choices": [{"label": "Довериться и уйти с Алексеем", "next_scene": "sage_stream_journey"}]
        },
        "sage_stream_journey": {
            "text": (
                "Вы идете с Алексеем тайными тропами до самого полудня. "
                "Старик оказывается на удивление выносливым. Вскоре вы выходите к живописному лесному ручью."
            ),
            "choices": [{"label": "Сделать привал у воды", "next_scene": "sage_stream_lunch"}]
        },
        "sage_stream_lunch": {
            "text": (
                "Алексей делит с вами скромную трапезу. "
                "Наклонившись попить, вы видите свое отражение и с ужасом понимаете, что не узнаете этого лица. "
                "Прошлое стерто начисто."
            ),
            "choices": [{"label": "Собраться с духом и идти", "next_scene": "stone_crossroad_sage"}]
        },
        "stone_crossroad_sage": {
            "text": (
                "К вечеру лес расступается перед древним трактом. "
                "Посреди дороги стоит мшистый камень с грубо высеченной надписью: "
                "'ЗАКОЛДОВАННЫМ — НАПРАВО. БЕЗЛОШАДНЫМ — НАЛЕВО'. Алексей задумчиво хмурится."
            ),
            "choices": [
                {"label": "Направо (Путь заколдованных)", "next_scene": "path_enchanted"},
                {"label": "Налево (Путь безлошадных)", "next_scene": "path_horseless"}
            ]
        },

        # === ВЕТКА 2: КОНЬ ===
        "find_horse_start": {
            "text": (
                "Вы ползаете под кустами, раздвигая папоротник. "
                "Наконец удача улыбается вам: вы находите свою кожаную сумку. "
                "Внутри лежат старый верный кинжал и кусок черствого хлеба."
            ),
            "loot": ["Старый кинжал", "Черствый хлеб"],
            "choices": [{"label": "Идти дальше по следам", "next_scene": "horse_found"}]
        },
        "horse_found": {
            "text": (
                "Следы выводят на солнечную поляну. Там, мирно щипля траву, стоит ваш боевой конь! "
                "Он радостно ржет, узнав хозяина. "
                "На седле вы находите настоящие сокровища: меч, полную флягу и припасы."
            ),
            "loot": ["Меч рыцаря", "Фляга с водой", "Кусок сала"],
            "choices": [{"label": "Вскочить в седло и скакать", "next_scene": "ride_away_river"}]
        },
        "ride_away_river": {
            "text": (
                "Ветер свистит в ушах, вы несетесь прочь от проклятого места. "
                "Спустя несколько часов бешеной скачки вы осаживаете коня у чистого ручья, чтобы перевести дух."
            ),
            "choices": [{"label": "Спешиться и пообедать", "next_scene": "stream_rest"}]
        },
        "stream_rest": {
            "text": (
                "Вы жадно съедаете хлеб, запивая ледяной водой. "
                "Взглянув в зеркальную гладь ручья, вы видите чужое лицо. "
                "Память пуста, и от этого на душе скребут кошки, но теплый бок коня успокаивает."
            ),
            "consume_loot": ["Черствый хлеб"],
            "choices": [{"label": "Ехать дальше к тракту", "next_scene": "stone_crossroad_horse"}]
        },
        "stone_crossroad_horse": {
            "text": (
                "Тропа выводит вас к старому имперскому тракту. Вскоре путь преграждает огромный камень. "
                "Надпись гласит: 'ЗАКОЛДОВАННЫМ — НАПРАВО. БЕЗЛОШАДНЫМ — НАЛЕВО'. "
                "Конь нетерпеливо бьет копытом, ожидая вашей команды."
            ),
            "choices": [
                {"label": "Повернуть направо (Путь заколдованных)", "next_scene": "path_enchanted"},
                {"label": "Повернуть налево (Путь безлошадных)", "next_scene": "path_horseless"}
            ]
        },

        # === ВЕТКА 3: ГНОМЫ ===
        "meet_dwarves": {
            "text": (
                "Вы решительно шагаете вперед. Вдруг из-за поворота вылетают два гнома. "
                "Увидев вас, они в панике бросают тяжелый мешочек и растворяются в кустах. "
                "Внутри золото, но солнце уже садится, и лес охватывает могильный холод."
            ),
            "loot": ["Мешочек золота"],
            "choices": [
                {"label": "Упасть на мох и попытаться уснуть", "next_scene": "sleep_cold"},
                {"label": "Собрать силы и развести костер", "next_scene": "dwarf_village"}
            ]
        },
        "sleep_cold": {"text": "Холод пробирает до костей...", "choices": [{"label": "...", "next_scene": "city_arrest"}]},
        "dwarf_village": {
            "text": (
                "Всю ночь вы грелись у огня, а утром вышли к подножию гор. "
                "Там, вырубленная в скале, расположилась деревня. "
                "Старейшина гномов выходит к вам навстречу, удивленный вашей честностью."
            ),
            "choices": [{"label": "Вернуть золото владельцам", "next_scene": "dwarf_feast"}]
        },
        "dwarf_feast": {
            "text": (
                "В честь благородного гостя гномы закатывают пир! "
                "Вас спрашивают о вашем роде и подвигах, но вы молчите. "
                "Пытаясь вспомнить хоть что-то, вы понимаете, что в голове лишь туман."
            ),
            "loot": ["Эль гномов", "Жареная рулька"],
            "choices": [{"label": "Признаться в потере памяти", "next_scene": "dwarf_sleep"}]
        },
        "dwarf_sleep": {
            "text": (
                "Гномы сочувственно качают головами. "
                "— Утро вечера мудренее, — говорит Старейшина и отводит вас в мягкую постель. "
                "Вы мгновенно проваливаетесь в глубокий сон."
            ),
            "choices": [{"label": "Проснуться на рассвете", "next_scene": "dwarf_morning"}]
        },
        "dwarf_morning": {
            "text": (
                "Вы просыпаетесь полным сил. Старейшина сдержал слово: "
                "у ворот вас ждет суровый следопыт Балин, готовый проводить к магам."
            ),
            "choices": [{"label": "Отправиться в путь", "next_scene": "dwarf_hike_start"}]
        },
        "dwarf_hike_start": {
            "text": (
                "Балин проверяет тетиву арбалета и кивает вам. "
                "Вы покидаете гостеприимную деревню и углубляетесь в дикие земли. "
                "Ваш великий поход за правдой начинается."
            ),
            "new_companion": "Следопыт Балин",
            "choices": [{"label": "Идти весь день", "next_scene": "dwarf_night_camp"}]
        },
        "dwarf_night_camp": {
            "text": (
                "К ночи вы находите уютный грот. Балин разводит бездымный костер. "
                "Вы ложитесь спать первым, пока гном несет вахту, вслушиваясь в звуки ночи."
            ),
            "choices": [{"label": "Попытаться уснуть", "next_scene": "dwarf_theft_attempt"}]
        },
        "dwarf_theft_attempt": {
            "text": (
                "Вас будит шорох и ругань Балина! "
                "Мелкие пещерные твари пытаются утащить ваши пожитки в темноту. "
                "Нужно действовать немедленно!"
            ),
            "choices": [{"label": "Схватить оружие и отогнать воров", "next_scene": "stone_crossroad_dwarf"}]
        },
        "stone_crossroad_dwarf": {
            "text": (
                "Вы отбиваетесь от воришек и утром выходите на тракт. "
                "Перед вами тот самый камень: 'ЗАКОЛДОВАННЫМ — НАПРАВО. БЕЗЛОШАДНЫМ — НАЛЕВО'. "
                "Балин опирается на секиру, ожидая решения."
            ),
            "choices": [
                {"label": "Направо (Путь заколдованных)", "next_scene": "path_enchanted"},
                {"label": "Налево (Путь безлошадных)", "next_scene": "path_horseless"}
            ]
        },

        # === ФИНАЛ: БАШНЯ ===
        "path_enchanted": {
            "text": (
                "Вы сворачиваете направо. Воздух здесь становится густым, вязким и пахнет озоном. "
                "Деревья вокруг искривлены магией, словно застыли в агонии. "
                "Дорога ведет вас к источнику вашей беды."
            ),
            "choices": [{"label": "Продолжить путь к цели", "next_scene": "tower_found"}]
        },
        "tower_found": {
            "text": (
                "Лес внезапно обрывается. На выжженной поляне возвышается Башня Темного Алхимика. "
                "Ее шпиль из черного обсидиана пронзает небо, а вокруг царит мертвая тишина. "
                "Входная дверь приоткрыта, словно приглашая в ловушку."
            ),
            "image_type": "tower",
            "choices": [
                {"label": "Смело войти в главный вход", "next_scene": "tower_entrance"},
                {"label": "Осторожно искать другой путь", "next_scene": "tower_side_entrance"}
            ]
        },
        "tower_entrance": {
            "text": "Вы толкаете тяжелые створки и входите в полумрак. Эхо ваших шагов разносится по залу... (Сюжет в разработке)",
            "choices": []
        },
        "tower_side_entrance": {
            "text": "Раздвинув колючий плющ, вы находите узкое окно в подвал. Оттуда веет холодом... (Сюжет в разработке)",
            "choices": []
        },

        # === ПЕТЛЯ ВРЕМЕНИ (ЛЕВЫЙ ПУТЬ) ===
        "path_horseless": {
            "text": (
                "Вы выбираете левую дорогу, игнорируя предупреждение. "
                "Поначалу путь кажется мирным, птицы поют, а солнце светит сквозь листву. "
                "Но стоит солнцу коснуться горизонта, как лес мгновенно погружается в непроглядную, неестественную тьму."
            ),
            "choices": [{"label": "Настороженно ехать дальше", "next_scene": "ambush_loop_hit"}]
        },
        "ambush_loop_hit": {
            "text": (
                "Внезапно сзади раздается свист! Вы не успеваете среагировать. "
                "Тяжелый удар дубиной по затылку выбивает из вас дух. "
                "Последнее, что вы слышите перед тем, как провалиться в небытие — это злой, издевательский смех..."
            ),
            "choices": [{"label": "Очнуться от кошмара", "next_scene": "start"}] # ВОЗВРАТ В НАЧАЛО
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