# Список доступных языков для меню
LANGUAGES = {
    'ru': 'Русский',
    'en': 'English',
    'el': 'Ελληνικά' # Greek
}

# ASCII Арт Рыцаря для боковой панели
KNIGHT_ART = r"""
      ,   A
     / \  |    I
    /   \ |    I
   /____ \|    I   ---( )_
   |    | |    I  /     \
   |    | |____I      \
     (  \_/  )
      \     /
"""

# Полный словарь сценариев, сгруппированных по языкам
SCENARIOS = {
    'ru': {
        # === ПРОЛОГ ===
        "start": {
            "text": (
                "Сознание возвращается рывками, принося с собой тупую боль в висках. "
                "Вы лежите на сырой земле, глядя в кроны вековых сосен, закрывающих небо. "
                "В голове пульсирует имя: «Сэр Галахад». Но оно кажется чужим. "
                "Вокруг — тишина древнего леса. Вашего верного дестриэ нет рядом. "
                "Тропа, едва заметная в высокой траве, расходится надвое."
            ),
            "image_type": "intro",
            "question": "Лес давит своим величием. Вам нужно действовать.",
            "choices": [
                {"label": "Осмотреться в поисках следов коня", "next_scene": "find_horse_start"},
                {"label": "Решительно двинуться по тропе вперед", "next_scene": "meet_dwarves"},
                {"label": "Сил нет. Остаться на месте и ждать", "next_scene": "stay_sad"}
            ]
        },

        # === ВЕТКА 1: МУДРЕЦ АЛЕКСЕЙ -> КАМЕНЬ ===
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
            "text": (
                "Из тени выступает старик в плаще.\n"
                "— Я Алексей, — говорит он. — Твою память украл Темный Алхимик. Я помогу тебе найти Храм Памяти."
            ),
            "new_companion": "Мудрец Алексей",
            "choices": [{"label": "Уйти с Алексеем", "next_scene": "sage_stream_journey"}]
        },
        "sage_stream_journey": {
            "text": "Вы идете с Алексеем до полудня и выходите к ручью.",
            "choices": [{"label": "Сделать привал", "next_scene": "sage_stream_lunch"}]
        },
        "sage_stream_lunch": {
            "text": (
                "Алексей делится с вами едой. Вы смотрите в воду и не узнаете своего лица. "
                "Страх подступает, но мудрый спутник успокаивает."
            ),
            "choices": [{"label": "Продолжить путь", "next_scene": "stone_crossroad_sage"}]
        },
        "stone_crossroad_sage": {
            "text": (
                "К вечеру вы с Алексеем доходите до странной развилки. Посреди дороги стоит древний мшистый камень.\n"
                "Надпись гласит: 'ЗАКОЛДОВАННЫМ — НАПРАВО. БЕЗЛОШАДНЫМ — НАЛЕВО'.\n"
                "Алексей хмыкает: 'Коней у нас нет, а проклятие на тебе есть. Куда пойдем?'"
            ),
            "question": "Дороги расходятся.",
            "choices": [
                {"label": "Направо (Путь заколдованных)", "next_scene": "path_enchanted"},
                {"label": "Налево (Путь безлошадных)", "next_scene": "path_horseless"}
            ]
        },

        # === ВЕТКА 2: КОНЬ -> КАМЕНЬ ===
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
            "text": (
                "Вы съедаете хлеб, запивая водой. В отражении ручья вы видите чужое лицо. "
                "Память стерта. Вы в отчаянии, но конь рядом."
            ),
            "consume_loot": ["Черствый хлеб"],
            "choices": [{"label": "Ехать дальше", "next_scene": "stone_crossroad_horse"}]
        },
        "stone_crossroad_horse": {
            "text": (
                "Тропа выводит вас на старый тракт. Вскоре вы видите развилку с камнем.\n"
                "Надпись гласит: 'ЗАКОЛДОВАННЫМ — НАПРАВО. БЕЗЛОШАДНЫМ — НАЛЕВО'.\n"
                "Вы сидите верхом, значит, налево вам нельзя? Но вы точно заколдованы..."
            ),
            "question": "Конь бьет копытом, ожидая команды.",
            "choices": [
                {"label": "Повернуть направо (Путь заколдованных)", "next_scene": "path_enchanted"},
                {"label": "Повернуть налево (Путь безлошадных)", "next_scene": "path_horseless"}
            ]
        },

        # === ВЕТКА 3: ГНОМЫ -> ПОХОД -> КАМЕНЬ ===
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
            "text": "Вас отправляют спать. 'Утро вечера мудренее'.",
            "choices": [{"label": "Проснуться", "next_scene": "dwarf_morning"}]
        },
        "dwarf_morning": {
            "text": "Утром Старейшина дает вам в помощь следопыта Балина.",
            "choices": [{"label": "В путь!", "next_scene": "dwarf_hike_start"}]
        },
        "dwarf_hike_start": {
            "text": "Балин проверяет арбалет. Вы выходите за ворота деревни гномов. Ваш великий поход начинается.",
            "new_companion": "Следопыт Балин",
            "choices": [{"label": "Отправиться в путь", "next_scene": "dwarf_night_camp"}]
        },
        "dwarf_night_camp": {
            "text": "Вы с Балином устраиваете привал в гроте. Он ложится спать первым.",
            "choices": [{"label": "Попытаться уснуть", "next_scene": "dwarf_theft_attempt"}]
        },
        "dwarf_theft_attempt": {
            "text": "Ночью вас будит царапающий звук. Мелкие существа пытаются утащить ваши вещи!",
            "question": "Времени мало, нужно действовать быстро.",
            "choices": [{"label": "Схватить оружие и отогнать воришек", "next_scene": "stone_crossroad_dwarf"}]
        },
        "stone_crossroad_dwarf": {
            "text": (
                "Вы отгоняете воришек. Утром вы продолжаете путь и выходите к старому тракту.\n"
                "Посреди дороги стоит древний мшистый камень. Надпись: 'ЗАКОЛДОВАННЫМ — НАПРАВО. БЕЗЛОШАДНЫМ — НАЛЕВО'."
            ),
            "question": "Балин задумчиво осматривает камень.",
            "choices": [
                {"label": "Направо (Путь заколдованных)", "next_scene": "path_enchanted"},
                {"label": "Налево (Путь безлошадных)", "next_scene": "path_horseless"}
            ]
        },

        # === НОВЫЙ СЮЖЕТНЫЙ БЛОК: БАШНЯ ===

        "path_enchanted": {
            "text": "Вы сворачиваете направо. Воздух здесь становится густым, пахнет озоном и старой магией. Дорога ведет вас все глубже в мистические земли.",
            "choices": [
                {"label": "Продолжить путь", "next_scene": "tower_found"}
            ]
        },
        "tower_found": {
            "text": (
                "Спустя много часов, вы, наконец, выходите на обширную поляну. "
                "В самом её центре возвышается башня — тонкий шпиль из обсидиана, пронзающий облака. "
                "Ее стены не отражают свет, а поглощают его, и вокруг царит мертвая тишина. "
                "Это Башня Темного Алхимика, хранителя вашей потерянной памяти. Двери широко распахнуты."
            ),
            "image_type": "tower",
            "question": "Внутри вас ждет нечто большее, чем просто воспоминания.",
            "choices": [
                {"label": "Войти в Башню", "next_scene": "tower_entrance"},
                {"label": "Искать другой вход", "next_scene": "tower_side_entrance"}
            ]
        },
        "tower_entrance": {
            "text": "Вы смело входите в темный зал. Пол скрипит под ногами. (Сюжет будет добавлен позже)",
            "choices": []
        },
        "tower_side_entrance": {
            "text": "Вы находите узкий проход за витком плюща. Он ведет в подвал. (Сюжет будет добавлен позже)",
            "choices": []
        },
        
        # === ФИНАЛЫ ПОСЛЕ КАМНЯ (без башни) ===
        "path_horseless": {
            "text": "Вы выбираете левую дорогу. Она выглядит заброшенной и печальной. Здесь слишком тихо. (Продолжение следует...)",
            "choices": []
        }
    },
    
    # --- Английский перевод (English) ---
    'en': {
        "start": {
            "text": (
                "Consciousness returns in jolts, bringing with it a dull ache in your temples. "
                "You lie on damp earth, gazing at the crowns of ancient pines blocking the sky. "
                "The name 'Sir Galahad' pulses in your mind, but it feels alien. "
                "Silence of the ancient forest surrounds you. Your loyal steed is missing. "
                "A faint trail, barely visible in the tall grass, forks ahead."
            ),
            "image_type": "intro",
            "question": "The forest is overwhelmingly vast. You must act.",
            "choices": [
                {"label": "Look for the horse's tracks", "next_scene": "find_horse_start"},
                {"label": "Move decisively along the path", "next_scene": "meet_dwarves"},
                {"label": "No strength. Stay put and wait", "next_scene": "stay_sad"}
            ]
        },
        "stay_sad": {
            "text": "As twilight falls, a monster's growl echoes! To stay here is certain death.",
            "choices": [{"label": "Jump up and run", "next_scene": "run_to_edge"}]
        },
        "run_to_edge": {
            "text": "You burst out onto the edge of the forest. City lights glimmer ahead.",
            "choices": [{"label": "Approach the city guards", "next_scene": "city_arrest"}]
        },
        "city_arrest": {
            "text": "The guards at the gate stop you. You look like a vagrant.",
            "choices": [{"label": "Surrender", "next_scene": "dungeon_cell"}]
        },
        "dungeon_cell": {
            "text": "In the cell, you realize your memory loss is a curse. One stone in the wall is loose.",
            "choices": [{"label": "Push against the stone", "next_scene": "secret_passage"}]
        },
        "secret_passage": {
            "text": "You escape through the sewer system, dirty but free.",
            "choices": [{"label": "Look around", "next_scene": "meet_sage"}]
        },
        "meet_sage": {
            "text": (
                "A cloaked old man steps out of the shadows.\n"
                "— I am Alexei. The Dark Alchemist stole your memory. I will help you find the Temple of Memory."
            ),
            "new_companion": "Sage Alexei",
            "choices": [{"label": "Go with Alexei", "next_scene": "sage_stream_journey"}]
        },
        "sage_stream_journey": {
            "text": "You walk with Alexei until noon and reach a stream.",
            "choices": [{"label": "Make camp", "next_scene": "sage_stream_lunch"}]
        },
        "sage_stream_lunch": {
            "text": (
                "Alexei shares his food. You look into the water and don't recognize your face. "
                "Fear rises, but the wise companion soothes you."
            ),
            "choices": [{"label": "Continue the journey", "next_scene": "stone_crossroad_sage"}]
        },
        "stone_crossroad_sage": {
            "text": (
                "By evening, you reach a strange fork in the road with a mossy, ancient stone.\n"
                "The inscription reads: 'THE ENCHANTED — RIGHT. THE HORSELESS — LEFT'.\n"
                "Alexei muses: 'We have no horses, but a curse is upon you. Which path do we take?'"
            ),
            "question": "The roads diverge.",
            "choices": [
                {"label": "Right (Path of the Enchanted)", "next_scene": "path_enchanted"},
                {"label": "Left (Path of the Horseless)", "next_scene": "path_horseless"}
            ]
        },
        "find_horse_start": {
            "text": "Under a bush, you find your bag with a dagger and hard bread.",
            "loot": ["Old Dagger", "Stale Bread"],
            "choices": [{"label": "Follow the tracks", "next_scene": "horse_found"}]
        },
        "horse_found": {
            "text": "In the clearing, you find your horse! On the saddle: a sword, water, and lard.",
            "loot": ["Knight's Sword", "Water Flask", "Lard Piece"],
            "choices": [{"label": "Ride away", "next_scene": "ride_away_river"}]
        },
        "ride_away_river": {
            "text": "You ride away from the forest. After hours, you stop by a stream.",
            "choices": [{"label": "Have lunch", "next_scene": "stream_rest"}]
        },
        "stream_rest": {
            "text": (
                "You eat the bread, drinking water. You see a strange face in the stream's reflection. "
                "Memory is gone. You are desperate, but the horse is near."
            ),
            "consume_loot": ["Stale Bread"],
            "choices": [{"label": "Ride further", "next_scene": "stone_crossroad_horse"}]
        },
        "stone_crossroad_horse": {
            "text": (
                "The trail leads to an old road. Soon you see a fork with a stone.\n"
                "The inscription reads: 'THE ENCHANTED — RIGHT. THE HORSELESS — LEFT'.\n"
                "You are mounted, so left is forbidden? But you are certainly enchanted..."
            ),
            "question": "Your horse stomps, awaiting a command.",
            "choices": [
                {"label": "Turn Right (Path of the Enchanted)", "next_scene": "path_enchanted"},
                {"label": "Turn Left (Path of the Horseless)", "next_scene": "path_horseless"}
            ]
        },
        "meet_dwarves": {
            "text": "Dwarves run away, dropping gold. It's getting cold.",
            "loot": ["Bag of Gold"],
            "choices": [
                {"label": "Sleep (freeze)", "next_scene": "sleep_cold"},
                {"label": "Build a fire", "next_scene": "dwarf_village"}
            ]
        },
        "sleep_cold": {"text": "...", "choices": [{"label": "...", "next_scene": "city_arrest"}]},
        "dwarf_village": {
            "text": "You find the dwarf village. The Elder meets you.",
            "choices": [{"label": "Return the gold", "next_scene": "dwarf_feast"}]
        },
        "dwarf_feast": {
            "text": "At the feast, they ask about your past, but you remember nothing.",
            "loot": ["Dwarf Ale", "Roasted Shank"],
            "choices": [{"label": "Confess", "next_scene": "dwarf_sleep"}]
        },
        "dwarf_sleep": {
            "text": "They send you to bed. 'Tomorrow's counsel is best.'",
            "choices": [{"label": "Wake up", "next_scene": "dwarf_morning"}]
        },
        "dwarf_morning": {
            "text": "In the morning, the Elder assigns Balin the Tracker to you.",
            "choices": [{"label": "To the road!", "next_scene": "dwarf_hike_start"}]
        },
        "dwarf_hike_start": {
            "text": "Balin checks his crossbow. You leave the village. Your great journey begins.",
            "new_companion": "Tracker Balin",
            "choices": [{"label": "Set off", "next_scene": "dwarf_night_camp"}]
        },
        "dwarf_night_camp": {
            "text": "You and Balin make camp in a grotto. He takes the first watch.",
            "choices": [{"label": "Try to sleep", "next_scene": "dwarf_theft_attempt"}]
        },
        "dwarf_theft_attempt": {
            "text": "A scratching sound wakes you. Small creatures are trying to steal your items!",
            "question": "Act fast.",
            "choices": [{"label": "Grab weapon and drive off the thieves", "next_scene": "stone_crossroad_dwarf"}]
        },
        "stone_crossroad_dwarf": {
            "text": (
                "You drive off the thieves. In the morning, you reach the old road.\n"
                "In the middle stands the ancient, mossy stone. Inscription: 'THE ENCHANTED — RIGHT. THE HORSELESS — LEFT'."
            ),
            "question": "Balin examines the stone thoughtfully.",
            "choices": [
                {"label": "Right (Path of the Enchanted)", "next_scene": "path_enchanted"},
                {"label": "Left (Path of the Horseless)", "next_scene": "path_horseless"}
            ]
        },
        "path_enchanted": {
            "text": "You turn right. The air here grows thick, smelling of ozone and old magic. The road guides you deeper into the mystical lands.",
            "choices": [
                {"label": "Continue the path", "next_scene": "tower_found"}
            ]
        },
        "tower_found": {
            "text": (
                "After many hours, you finally emerge into a vast clearing. "
                "At its very center rises a tower—a thin obsidian spire piercing the clouds. "
                "Its walls absorb light rather than reflecting it, and a dead silence reigns around. "
                "This is the Tower of the Dark Alchemist, keeper of your lost memory. The doors stand wide open."
            ),
            "image_type": "tower",
            "question": "Something greater than just memories awaits you inside.",
            "choices": [
                {"label": "Enter the Tower", "next_scene": "tower_entrance"},
                {"label": "Search for another entrance", "next_scene": "tower_side_entrance"}
            ]
        },
        "tower_entrance": {
            "text": "You bravely enter the dark hall. The floor creaks underfoot. (Plot to be added later)",
            "choices": []
        },
        "tower_side_entrance": {
            "text": "You find a narrow passage behind a twist of ivy. It leads to the basement. (Plot to be added later)",
            "choices": []
        },
        "path_horseless": {
            "text": "You choose the left road. It looks abandoned and desolate. It is too quiet here. (To be continued...)",
            "choices": []
        }
    },

    # --- Греческий перевод (Greek) ---
    'el': {
        "start": {
            "text": (
                "Η συνείδησή σας επανέρχεται με τραντάγματα, φέρνοντας έναν θαμπό πόνο στους κροτάφους σας. "
                "Είστε ξαπλωμένος σε υγρή γη, κοιτάζοντας τις κορυφές των αρχαίων πεύκων που κρύβουν τον ουρανό. "
                "Το όνομα «Σερ Γκάλαχαντ» χτυπά στο μυαλό σας, αλλά μοιάζει ξένο. "
                "Σας περιβάλλει η σιωπή του αρχαίου δάσους. Ο πιστός σας ίππος λείπει. "
                "Ένα αχνό μονοπάτι, μόλις ορατό, διχάζεται μπροστά."
            ),
            "image_type": "intro",
            "question": "Το δάσος είναι τρομερά απέραντο. Πρέπει να δράσετε.",
            "choices": [
                {"label": "Ψάξτε για ίχνη του αλόγου", "next_scene": "find_horse_start"},
                {"label": "Προχωρήστε αποφασιστικά κατά μήκος του μονοπατιού", "next_scene": "meet_dwarves"},
                {"label": "Δεν έχετε δύναμη. Μείνετε και περιμένετε", "next_scene": "stay_sad"}
            ]
        },
        "stay_sad": {
            "text": "Καθώς πέφτει το σούρουπο, αντηχεί ένας βρυχηθμός τέρατος! Το να μείνετε εδώ σημαίνει βέβαιος θάνατος.",
            "choices": [{"label": "Πεταχτείτε και τρέξτε", "next_scene": "run_to_edge"}]
        },
        "run_to_edge": {
            "text": "Ξεπετάγεστε στην άκρη του δάσους. Τα φώτα της πόλης αχνοφέγγουν μπροστά.",
            "choices": [{"label": "Πλησιάστε τους φρουρούς της πόλης", "next_scene": "city_arrest"}]
        },
        "city_arrest": {
            "text": "Οι φρουροί στην πύλη σας σταματούν. Μοιάζετε με αλήτη.",
            "choices": [{"label": "Παραδοθείτε", "next_scene": "dungeon_cell"}]
        },
        "dungeon_cell": {
            "text": "Στο κελί, συνειδητοποιείτε ότι η απώλεια μνήμης είναι κατάρα. Μια πέτρα στον τοίχο είναι χαλαρή.",
            "choices": [{"label": "Σπρώξτε την πέτρα", "next_scene": "secret_passage"}]
        },
        "secret_passage": {
            "text": "Δραπετεύετε μέσω του αποχετευτικού συστήματος, βρώμικος αλλά ελεύθερος.",
            "choices": [{"label": "Ρίξτε μια ματιά γύρω", "next_scene": "meet_sage"}]
        },
        "meet_sage": {
            "text": (
                "Ένας ηλικιωμένος άνδρας με μανδύα βγαίνει από τις σκιές.\n"
                "— Είμαι ο Αλέξιος. Ο Σκοτεινός Αλχημιστής έκλεψε τη μνήμη σου. Θα σε βοηθήσω να βρεις τον Ναό της Μνήμης."
            ),
            "new_companion": "Σοφός Αλέξιος",
            "choices": [{"label": "Πηγαίνετε με τον Αλέξιο", "next_scene": "sage_stream_journey"}]
        },
        "sage_stream_journey": {
            "text": "Περπατάτε με τον Αλέξιο μέχρι το μεσημέρι και φτάνετε σε ένα ρυάκι.",
            "choices": [{"label": "Κάντε στάση", "next_scene": "sage_stream_lunch"}]
        },
        "sage_stream_lunch": {
            "text": (
                "Ο Αλέξιος μοιράζεται το φαγητό του. Κοιτάτε στο νερό και δεν αναγνωρίζετε το πρόσωπό σας. "
                "Ο φόβος ανεβαίνει, αλλά ο σοφός σύντροφος σας ηρεμεί."
            ),
            "choices": [{"label": "Συνεχίστε το ταξίδι", "next_scene": "stone_crossroad_sage"}]
        },
        "stone_crossroad_sage": {
            "text": (
                "Μέχρι το βράδυ, φτάνετε σε ένα παράξενο σταυροδρόμι με μια βρύα, αρχαία πέτρα.\n"
                "Η επιγραφή λέει: 'ΟΙ ΜΑΓΕΜΕΝΟΙ — ΔΕΞΙΑ. ΟΙ ΑΝΙΠΠΟΙ — ΑΡΙΣΤΕΡΑ'.\n"
                "Ο Αλέξιος συλλογίζεται: 'Δεν έχουμε άλογα, αλλά μια κατάρα είναι πάνω σου. Ποιο μονοπάτι παίρνουμε;'"
            ),
            "question": "Οι δρόμοι αποκλίνουν.",
            "choices": [
                {"label": "Δεξιά (Διαδρομή των Μαγεμένων)", "next_scene": "path_enchanted"},
                {"label": "Αριστερά (Διαδρομή των Ανίππων)", "next_scene": "path_horseless"}
            ]
        },
        "find_horse_start": {
            "text": "Κάτω από έναν θάμνο, βρίσκετε την τσάντα σας με ένα στιλέτο και μπαγιάτικο ψωμί.",
            "loot": ["Παλιό Στιλέτο", "Μπαγιάτικο Ψωμί"],
            "choices": [{"label": "Ακολουθήστε τα ίχνη", "next_scene": "horse_found"}]
        },
        "horse_found": {
            "text": "Στο ξέφωτο, βρίσκετε το άλογό σας! Στη σέλα: ένα σπαθί, νερό και λαρδί.",
            "loot": ["Σπαθί Ιππότη", "Παγούρι Νερού", "Κομμάτι Λαρδί"],
            "choices": [{"label": "Καβαλήστε μακριά", "next_scene": "ride_away_river"}]
        },
        "ride_away_river": {
            "text": "Απομακρύνεστε από το δάσος. Μετά από ώρες, σταματάτε δίπλα σε ένα ρυάκι.",
            "choices": [{"label": "Φάτε μεσημεριανό", "next_scene": "stream_rest"}]
        },
        "stream_rest": {
            "text": (
                "Τρώτε το ψωμί, πίνοντας νερό. Βλέπετε ένα άγνωστο πρόσωπο στην αντανάκλαση του ρυακιού. "
                "Η μνήμη έχει χαθεί. Είστε απελπισμένος, αλλά το άλογο είναι κοντά."
            ),
            "consume_loot": ["Μπαγιάτικο Ψωμί"],
            "choices": [{"label": "Συνεχίστε", "next_scene": "stone_crossroad_horse"}]
        },
        "stone_crossroad_horse": {
            "text": (
                "Το μονοπάτι οδηγεί σε έναν παλιό δρόμο. Σύντομα βλέπετε μια διακλάδωση με μια πέτρα.\n"
                "Η επιγραφή λέει: 'ΟΙ ΜΑΓΕΜΕΝΟΙ — ΔΕΞΙΑ. ΟΙ ΑΝΙΠΠΟΙ — ΑΡΙΣΤΕΡΑ'.\n"
                "Είστε ανεβασμένος, οπότε η αριστερή είναι απαγορευμένη; Αλλά είστε σίγουρα μαγεμένος..."
            ),
            "question": "Το άλογό σας χτυπάει την οπλή, περιμένοντας μια εντολή.",
            "choices": [
                {"label": "Στρίψτε Δεξιά (Διαδρομή των Μαγεμένων)", "next_scene": "path_enchanted"},
                {"label": "Στρίψτε Αριστερά (Διαδρομή των Ανίππων)", "next_scene": "path_horseless"}
            ]
        },
        "meet_dwarves": {
            "text": "Οι νάνοι φεύγουν, ρίχνοντας χρυσάφι. Κάνει κρύο.",
            "loot": ["Σακούλα Χρυσού"],
            "choices": [
                {"label": "Κοιμηθείτε (παγώστε)", "next_scene": "sleep_cold"},
                {"label": "Ανάψτε φωτιά", "next_scene": "dwarf_village"}
            ]
        },
        "sleep_cold": {"text": "...", "choices": [{"label": "...", "next_scene": "city_arrest"}]},
        "dwarf_village": {
            "text": "Βρίσκετε το χωριό των νάνων. Ο Γέροντας σας συναντά.",
            "choices": [{"label": "Επιστρέψτε το χρυσάφι", "next_scene": "dwarf_feast"}]
        },
        "dwarf_feast": {
            "text": "Στο γλέντι, ρωτούν για το παρελθόν σας, αλλά δεν θυμάστε τίποτα.",
            "loot": ["Νανίσια Μπύρα", "Ψητό Κότσι"],
            "choices": [{"label": "Εξομολογηθείτε", "next_scene": "dwarf_sleep"}]
        },
        "dwarf_sleep": {
            "text": "Σας στέλνουν για ύπνο. 'Η νύχτα φέρνει συμβουλές.'",
            "choices": [{"label": "Ξυπνήστε", "next_scene": "dwarf_morning"}]
        },
        "dwarf_morning": {
            "text": "Το πρωί, ο Γέροντας σας παραχωρεί τον Μπαλίν τον Ιχνηλάτη.",
            "choices": [{"label": "Στο δρόμο!", "next_scene": "dwarf_hike_start"}]
        },
        "dwarf_hike_start": {
            "text": "Ο Μπαλίν ελέγχει την βαλλίστρα του. Φεύγετε από το χωριό. Το μεγάλο σας ταξίδι αρχίζει.",
            "new_companion": "Ιχνηλάτης Μπαλίν",
            "choices": [{"label": "Ξεκινήστε", "next_scene": "dwarf_night_camp"}]
        },
        "dwarf_night_camp": {
            "text": "Εσείς και ο Μπαλίν κάνετε κατασκήνωση σε μια σπηλιά. Αυτός αναλαμβάνει την πρώτη βάρδια.",
            "choices": [{"label": "Προσπαθήστε να κοιμηθείτε", "next_scene": "dwarf_theft_attempt"}]
        },
        "dwarf_theft_attempt": {
            "text": "Ένας ήχος ξύνει σας ξυπνάει. Μικρά πλάσματα προσπαθούν να κλέψουν τα αντικείμενά σας!",
            "question": "Δράστε γρήγορα.",
            "choices": [{"label": "Πιάστε όπλο και διώξτε τους κλέφτες", "next_scene": "stone_crossroad_dwarf"}]
        },
        "stone_crossroad_dwarf": {
            "text": (
                "Διώχνετε τους κλέφτες. Το πρωί, φτάνετε στον παλιό δρόμο.\n"
                "Στη μέση στέκεται η αρχαία, βρύα πέτρα. Επιγραφή: 'ΟΙ ΜΑΓΕΜΕΝΟΙ — ΔΕΞΙΑ. ΟΙ ΑΝΙΠΠΟΙ — ΑΡΙΣΤΕΡΑ'."
            ),
            "question": "Ο Μπαλίν εξετάζει την πέτρα σκεπτικός.",
            "choices": [
                {"label": "Δεξιά (Διαδρομή των Μαγεμένων)", "next_scene": "path_enchanted"},
                {"label": "Αριστερά (Διαδρομή των Ανίππων)", "next_scene": "path_horseless"}
            ]
        },
        "path_enchanted": {
            "text": "Στρίβετε δεξιά. Ο αέρας εδώ γίνεται πυκνός, μυρίζοντας όζον και αρχαία μαγεία. Ο δρόμος σας οδηγεί βαθύτερα στα μυστικιστικά εδάφη.",
            "choices": [
                {"label": "Συνεχίστε το μονοπάτι", "next_scene": "tower_found"}
            ]
        },
        "tower_found": {
            "text": (
                "Μετά από πολλές ώρες, βγαίνετε επιτέλους σε ένα απέραντο ξέφωτο. "
                "Στο κέντρο του υψώνεται ένας πύργος—μια λεπτή αιχμή από οψιδιανό που διαπερνά τα σύννεφα. "
                "Οι τοίχοι του απορροφούν το φως αντί να το αντανακλούν, και επικρατεί μια νεκρική σιωπή. "
                "Αυτός είναι ο Πύργος του Σκοτεινού Αλχημιστή, φύλακα της χαμένης σας μνήμης. Οι πόρτες είναι ορθάνοιχτες."
            ),
            "image_type": "tower",
            "question": "Κάτι περισσότερο από απλές αναμνήσεις σας περιμένει μέσα.",
            "choices": [
                {"label": "Εισέλθετε στον Πύργο", "next_scene": "tower_entrance"},
                {"label": "Ψάξτε για άλλη είσοδο", "next_scene": "tower_side_entrance"}
            ]
        },
        "tower_entrance": {
            "text": "Εισέρχεστε γενναία στη σκοτεινή αίθουσα. Το πάτωμα τρίζει κάτω από τα πόδια σας. (Η πλοκή θα προστεθεί αργότερα)",
            "choices": []
        },
        "tower_side_entrance": {
            "text": "Βρίσκετε ένα στενό πέρασμα πίσω από μια συστροφή κισσού. Οδηγεί στο υπόγειο. (Η πλοκή θα προστεθεί αργότερα)",
            "choices": []
        },
        "path_horseless": {
            "text": "Επιλέγετε τον αριστερό δρόμο. Φαίνεται εγκαταλελειμμένος και έρημος. Κάνει πολλή ησυχία. (Συνέχεια...)",
            "choices": []
        }
    }
}
