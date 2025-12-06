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
        "sleep_cold": {"text": "Холод пробирает до костей, сознание угасает...", "choices": [{"label": "...", "next_scene": "city_arrest"}]},
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
        # === PROLOGUE ===
        "start": {
            "text": (
                "Consciousness returns in jolts, every breath echoing with a dull ache in your temples. "
                "You lie on damp, musty earth, with the crowns of ancient pines rustling overhead. "
                "The name 'Sir Galahad' pulses in your mind, but it feels alien, as if from a past life. "
                "Your loyal steed is nowhere to be found, only broken branches hint at a struggle. "
                "An old path, barely visible in the twilight, forks in two."
            ),
            "image_type": "intro",
            "question": "The forest oppresses with its grim grandeur. You must decide.",
            "choices": [
                {"label": "Look around for the horse's tracks", "next_scene": "find_horse_start"},
                {"label": "Move decisively along the path", "next_scene": "meet_dwarves"},
                {"label": "No strength. Stay put and wait", "next_scene": "stay_sad"}
            ]
        },

        # === PATH 1: SAGE ALEXEI ===
        "stay_sad": {
            "text": (
                "You remain sitting, clutching your knees, as darkness gathers. "
                "Suddenly, a guttural growl erupts nearby, freezing the blood in your veins! "
                "A massive shadow separates from the trees. Staying here means certain death."
            ),
            "choices": [{"label": "Jump up and run without looking back", "next_scene": "run_to_edge"}]
        },
        "run_to_edge": {
            "text": (
                "Branches whip your face as you dash through the thicket, ignoring the path. "
                "Breath fails you, but you burst out onto the edge of the forest. "
                "Ahead, like a saving beacon, shimmer the lights of the city walls."
            ),
            "choices": [{"label": "Approach the city guard", "next_scene": "city_arrest"}]
        },
        "city_arrest": {
            "text": (
                "You rush to the gates, but halberds block your way. "
                "The guards inspect your torn doublet with disdain. "
                "'No place for vagrants here,' barks the sergeant. 'The dungeon will sort out who you are.'"
            ),
            "choices": [{"label": "Too weak to argue. Surrender", "next_scene": "dungeon_cell"}]
        },
        "dungeon_cell": {
            "text": (
                "The damp cell smells of mold and hopelessness. "
                "Sitting on straw, you realize your memory loss is a magical curse blocking your mind. "
                "In anger, you strike the wall and notice a stone is loose."
            ),
            "choices": [{"label": "Push the stone with your shoulder", "next_scene": "secret_passage"}]
        },
        "secret_passage": {
            "text": (
                "The stone gives way, revealing a foul-smelling passage into the old sewers. "
                "You crawl in the dark, scraping your elbows, and finally emerge into the moat. "
                "You are dirty, exhausted, but finally free."
            ),
            "choices": [{"label": "Brush off and look around", "next_scene": "meet_sage"}]
        },
        "meet_sage": {
            "text": (
                "A figure in a gray cloak with a staff steps out from the wall's shadow. The old man's eyes shine with wisdom. "
                "'Greetings, Galahad. I am Alexei,' he says softly. 'The Dark Alchemist stole your memory. "
                "I have been waiting for you to help restore justice.'"
            ),
            "new_companion": "Sage Alexei",
            "choices": [{"label": "Trust him and go with Alexei", "next_scene": "sage_stream_journey"}]
        },
        "sage_stream_journey": {
            "text": (
                "You walk with Alexei along secret paths until noon. "
                "The old man proves surprisingly resilient. Soon you emerge at a picturesque forest stream."
            ),
            "choices": [{"label": "Rest by the water", "next_scene": "sage_stream_lunch"}]
        },
        "sage_stream_lunch": {
            "text": (
                "Alexei shares a modest meal with you. "
                "Leaning down to drink, you see your reflection and realize with horror that you do not recognize the face. "
                "The past has been wiped clean."
            ),
            "choices": [{"label": "Gather your courage and move on", "next_scene": "stone_crossroad_sage"}]
        },
        "stone_crossroad_sage": {
            "text": (
                "By evening, the forest gives way to an ancient road. "
                "In the middle stands a mossy stone with a crudely carved inscription: "
                "'THE ENCHANTED — RIGHT. THE HORSELESS — LEFT'. Alexei frowns thoughtfully."
            ),
            "choices": [
                {"label": "Right (Path of the Enchanted)", "next_scene": "path_enchanted"},
                {"label": "Left (Path of the Horseless)", "next_scene": "path_horseless"}
            ]
        },

        # === PATH 2: HORSE ===
        "find_horse_start": {
            "text": (
                "You crawl under the bushes, parting the ferns. "
                "Finally, luck smiles upon you: you find your leather bag. "
                "Inside lie an old trusty dagger and a piece of stale bread."
            ),
            "loot": ["Old Dagger", "Stale Bread"],
            "choices": [{"label": "Follow the tracks further", "next_scene": "horse_found"}]
        },
        "horse_found": {
            "text": (
                "The tracks lead to a sunny clearing. There, peacefully grazing, stands your warhorse! "
                "He neighs joyfully, recognizing his master. "
                "On the saddle, you find true treasures: a sword, a full flask, and supplies."
            ),
            "loot": ["Knight's Sword", "Water Flask", "Lard Piece"],
            "choices": [{"label": "Jump in the saddle and ride", "next_scene": "ride_away_river"}]
        },
        "ride_away_river": {
            "text": (
                "Wind whistles in your ears as you race away from the cursed place. "
                "After hours of frantic riding, you halt the horse by a clear stream to catch your breath."
            ),
            "choices": [{"label": "Dismount and have lunch", "next_scene": "stream_rest"}]
        },
        "stream_rest": {
            "text": (
                "You greedily eat the bread, washing it down with ice-cold water. "
                "Glancing into the mirror-like surface of the stream, you see a stranger's face. "
                "Your memory is empty, scratching at your soul, but the warm flank of your horse soothes you."
            ),
            "consume_loot": ["Stale Bread"],
            "choices": [{"label": "Ride on to the road", "next_scene": "stone_crossroad_horse"}]
        },
        "stone_crossroad_horse": {
            "text": (
                "The path leads you to an old imperial road. Soon, a massive stone blocks the way. "
                "The inscription reads: 'THE ENCHANTED — RIGHT. THE HORSELESS — LEFT'. "
                "The horse stomps impatiently, awaiting your command."
            ),
            "choices": [
                {"label": "Turn Right (Path of the Enchanted)", "next_scene": "path_enchanted"},
                {"label": "Turn Left (Path of the Horseless)", "next_scene": "path_horseless"}
            ]
        },

        # === PATH 3: DWARVES ===
        "meet_dwarves": {
            "text": (
                "You step decisively forward. Suddenly, two dwarves burst out from around the bend. "
                "Seeing you, they panic, drop a heavy pouch, and vanish into the bushes. "
                "Inside is gold, but the sun is setting, and the grave cold of the forest takes hold."
            ),
            "loot": ["Bag of Gold"],
            "choices": [
                {"label": "Fall on the moss and try to sleep", "next_scene": "sleep_cold"},
                {"label": "Gather strength and build a fire", "next_scene": "dwarf_village"}
            ]
        },
        "sleep_cold": {"text": "The cold chills you to the bone, consciousness fades...", "choices": [{"label": "...", "next_scene": "city_arrest"}]},
        "dwarf_village": {
            "text": (
                "You warmed yourself by the fire all night, and in the morning reached the foot of the mountains. "
                "There, carved into the rock, lies a village. "
                "The Dwarf Elder comes out to meet you, surprised by your honesty."
            ),
            "choices": [{"label": "Return the gold to the owners", "next_scene": "dwarf_feast"}]
        },
        "dwarf_feast": {
            "text": (
                "In honor of the noble guest, the dwarves throw a feast! "
                "They ask of your lineage and deeds, but you remain silent. "
                "Trying to recall anything, you realize there is only fog in your head."
            ),
            "loot": ["Dwarf Ale", "Roasted Shank"],
            "choices": [{"label": "Confess memory loss", "next_scene": "dwarf_sleep"}]
        },
        "dwarf_sleep": {
            "text": (
                "The dwarves shake their heads sympathetically. "
                "'Tomorrow's counsel is best,' says the Elder and leads you to a soft bed. "
                "You instantly fall into a deep sleep."
            ),
            "choices": [{"label": "Wake up at dawn", "next_scene": "dwarf_morning"}]
        },
        "dwarf_morning": {
            "text": (
                "You wake up full of strength. The Elder kept his word: "
                "at the gates waits the stern tracker Balin, ready to guide you to the mages."
            ),
            "choices": [{"label": "Set off on the journey", "next_scene": "dwarf_hike_start"}]
        },
        "dwarf_hike_start": {
            "text": (
                "Balin checks his crossbow string and nods to you. "
                "You leave the hospitable village and delve into the wild lands. "
                "Your great quest for truth begins."
            ),
            "new_companion": "Tracker Balin",
            "choices": [{"label": "Walk all day", "next_scene": "dwarf_night_camp"}]
        },
        "dwarf_night_camp": {
            "text": (
                "By nightfall, you find a cozy grotto. Balin builds a smokeless fire. "
                "You go to sleep first while the dwarf takes watch, listening to the sounds of the night."
            ),
            "choices": [{"label": "Try to sleep", "next_scene": "dwarf_theft_attempt"}]
        },
        "dwarf_theft_attempt": {
            "text": (
                "You are woken by rustling and Balin's cursing! "
                "Small cave creatures are trying to drag your belongings into the dark. "
                "You must act immediately!"
            ),
            "choices": [{"label": "Grab a weapon and drive off the thieves", "next_scene": "stone_crossroad_dwarf"}]
        },
        "stone_crossroad_dwarf": {
            "text": (
                "You fight off the thieves and emerge onto the road in the morning. "
                "Before you stands that very stone: 'THE ENCHANTED — RIGHT. THE HORSELESS — LEFT'. "
                "Balin leans on his axe, awaiting a decision."
            ),
            "choices": [
                {"label": "Right (Path of the Enchanted)", "next_scene": "path_enchanted"},
                {"label": "Left (Path of the Horseless)", "next_scene": "path_horseless"}
            ]
        },

        # === FINALE: TOWER ===
        "path_enchanted": {
            "text": (
                "You turn right. The air becomes thick, viscous, and smells of ozone. "
                "The trees around are twisted by magic, as if frozen in agony. "
                "The road leads you to the source of your trouble."
            ),
            "choices": [{"label": "Continue to the goal", "next_scene": "tower_found"}]
        },
        "tower_found": {
            "text": (
                "The forest abruptly ends. On a scorched clearing stands the Tower of the Dark Alchemist. "
                "Its spire of black obsidian pierces the sky, and dead silence reigns around. "
                "The entrance door is slightly ajar, as if inviting you into a trap."
            ),
            "image_type": "tower",
            "choices": [
                {"label": "Boldly enter the main entrance", "next_scene": "tower_entrance"},
                {"label": "Cautiously look for another way", "next_scene": "tower_side_entrance"}
            ]
        },
        "tower_entrance": {
            "text": "You push the heavy doors and enter the gloom. The echo of your footsteps rings through the hall... (Plot in development)",
            "choices": []
        },
        "tower_side_entrance": {
            "text": "Pushing aside thorny ivy, you find a narrow window to the basement. A chill blows from within... (Plot in development)",
            "choices": []
        },

        # === TIME LOOP (LEFT PATH) ===
        "path_horseless": {
            "text": (
                "You choose the left road, ignoring the warning. "
                "At first, the path seems peaceful, birds sing, and the sun shines through the leaves. "
                "But as soon as the sun touches the horizon, the forest instantly plunges into impenetrable, unnatural darkness."
            ),
            "choices": [{"label": "Ride on warily", "next_scene": "ambush_loop_hit"}]
        },
        "ambush_loop_hit": {
            "text": (
                "Suddenly, a whistle cuts through the air from behind! You don't have time to react. "
                "A heavy blow from a club to the back of your head knocks the wind out of you. "
                "The last thing you hear before fading into nothingness is a malicious, mocking laugh..."
            ),
            "choices": [{"label": "Wake up from the nightmare", "next_scene": "start"}]
        }
    },

    'el': {
        # === ΠΡΟΛΟΓΟΣ ===
        "start": {
            "text": (
                "Η συνείδηση επιστρέφει με τραντάγματα, κάθε ανάσα αντηχεί με έναν υπόκωφο πόνο στους κροτάφους. "
                "Κείθεστε σε υγρή, μουχλιασμένη γη, ενώ από πάνω θροΐζουν οι κορυφές αρχαίων πεύκων. "
                "Το όνομα «Σερ Γκάλαχαντ» σφυροκοπά στο κεφάλι σας, μα μοιάζει ξένο, σαν από άλλη ζωή. "
                "Το πιστό σας άλογο λείπει, μόνο σπασμένα κλαδιά μαρτυρούν πάλη. "
                "Ένα παλιό μονοπάτι, μόλις ορατό στο λυκόφως, χωρίζεται στα δύο."
            ),
            "image_type": "intro",
            "question": "Το δάσος καταπιέζει με τη σκοτεινή του μεγαλοπρέπεια. Πρέπει να αποφασίσετε.",
            "choices": [
                {"label": "Κοιτάξτε γύρω για ίχνη του αλόγου", "next_scene": "find_horse_start"},
                {"label": "Προχωρήστε αποφασιστικά στο μονοπάτι", "next_scene": "meet_dwarves"},
                {"label": "Δεν έχω δύναμη. Μείνε και περίμενε", "next_scene": "stay_sad"}
            ]
        },

        # === ΜΟΝΟΠΑΤΙ 1: ΣΟΦΟΣ ΑΛΕΞΙΟΣ ===
        "stay_sad": {
            "text": (
                "Μένετε καθιστός, αγκαλιάζοντας τα γόνατά σας, καθώς το σκοτάδι πυκνώνει. "
                "Ξαφνικά, πολύ κοντά ακούγεται ένας λαρυγγώδης βρυχηθμός που παγώνει το αίμα στις φλέβες! "
                "Μια τεράστια σκιά ξεκολλάει από τα δέντρα. Το να μείνετε εδώ σημαίνει βέβαιο θάνατο."
            ),
            "choices": [{"label": "Πεταχτείτε και τρέξτε χωρίς να κοιτάξετε πίσω", "next_scene": "run_to_edge"}]
        },
        "run_to_edge": {
            "text": (
                "Κλαδιά μαστιγώνουν το πρόσωπό σας καθώς τρέχετε μέσα από την πυκνή βλάστηση, χωρίς να βλέπετε δρόμο. "
                "Η ανάσα σάς προδίδει, αλλά βγαίνετε στην άκρη του δάσους. "
                "Μπροστά, σαν φάρος σωτηρίας, τρεμοπαίζουν τα φώτα των τειχών της πόλης."
            ),
            "choices": [{"label": "Πλησιάστε τη φρουρά της πόλης", "next_scene": "city_arrest"}]
        },
        "city_arrest": {
            "text": (
                "Ορμάτε προς τις πύλες, αλλά αλάβαρδες φράζουν τον δρόμο. "
                "Οι φρουροί επιθεωρούν το σχισμένο σας ένδυμα με περιφρόνηση. "
                "«Δεν υπάρχει χώρος για αλήτες εδώ», γαυγίζει ο λοχίας. «Στο μπουντρούμι θα βρούμε ποιος είσαι»."
            ),
            "choices": [{"label": "Πολύ αδύναμος για αντίσταση. Παραδοθείτε", "next_scene": "dungeon_cell"}]
        },
        "dungeon_cell": {
            "text": (
                "Το υγρό κελί μυρίζει μούχλα και απελπισία. "
                "Καθισμένος στα άχυρα, συνειδητοποιείτε ότι η απώλεια μνήμης είναι μια μαγική κατάρα που μπλοκάρει το μυαλό. "
                "Από θυμό, χτυπάτε τον τοίχο και παρατηρείτε ότι μια πέτρα κουνιέται."
            ),
            "choices": [{"label": "Σπρώξτε την πέτρα με τον ώμο", "next_scene": "secret_passage"}]
        },
        "secret_passage": {
            "text": (
                "Η πέτρα υποχωρεί, αποκαλύπτοντας ένα δύσοσμο πέρασμα προς την παλιά αποχέτευση. "
                "Σέρνεστε στο σκοτάδι, γδέρνοντας τους αγκώνες σας, και τελικά βγαίνετε στην τάφρο. "
                "Είστε βρώμικος, εξαντλημένος, αλλά επιτέλους ελεύθερος."
            ),
            "choices": [{"label": "Τιναχτείτε και κοιτάξτε γύρω", "next_scene": "meet_sage"}]
        },
        "meet_sage": {
            "text": (
                "Μια φιγούρα με γκρίζο μανδύα και ραβδί ξεπροβάλλει από τη σκιά του τείχους. Τα μάτια του γέρου λάμπουν με σοφία. "
                "«Χαίρε, Γκάλαχαντ. Είμαι ο Αλέξιος», λέει σιγά. «Ο Σκοτεινός Αλχημιστής έκλεψε τη μνήμη σου. "
                "Σε περίμενα για να βοηθήσω να αποκατασταθεί η δικαιοσύνη»."
            ),
            "new_companion": "Σοφός Αλέξιος",
            "choices": [{"label": "Εμπιστευτείτε τον και φύγετε με τον Αλέξιο", "next_scene": "sage_stream_journey"}]
        },
        "sage_stream_journey": {
            "text": (
                "Περπατάτε με τον Αλέξιο από μυστικά μονοπάτια μέχρι το μεσημέρι. "
                "Ο γέρος αποδεικνύεται εκπληκτικά ανθεκτικός. Σύντομα φτάνετε σε ένα γραφικό δασικό ρυάκι."
            ),
            "choices": [{"label": "Κάντε στάση στο νερό", "next_scene": "sage_stream_lunch"}]
        },
        "sage_stream_lunch": {
            "text": (
                "Ο Αλέξιος μοιράζεται το λιτό του γεύμα μαζί σας. "
                "Σκύβοντας να πιείτε, βλέπετε την αντανάκλασή σας και συνειδητοποιείτε με τρόμο ότι δεν αναγνωρίζετε αυτό το πρόσωπο. "
                "Το παρελθόν έχει διαγραφεί εντελώς."
            ),
            "choices": [{"label": "Βρείτε κουράγιο και προχωρήστε", "next_scene": "stone_crossroad_sage"}]
        },
        "stone_crossroad_sage": {
            "text": (
                "Μέχρι το βράδυ, το δάσος ανοίγει μπροστά σε έναν αρχαίο δρόμο. "
                "Στη μέση στέκεται μια βρύα πέτρα με μια χοντροκομμένη επιγραφή: "
                "'ΟΙ ΜΑΓΕΜΕΝΟΙ — ΔΕΞΙΑ. ΟΙ ΑΝΙΠΠΟΙ — ΑΡΙΣΤΕΡΑ'. Ο Αλέξιος συνοφρυώνεται συλλογισμένος."
            ),
            "choices": [
                {"label": "Δεξιά (Διαδρομή των Μαγεμένων)", "next_scene": "path_enchanted"},
                {"label": "Αριστερά (Διαδρομή των Ανίππων)", "next_scene": "path_horseless"}
            ]
        },

        # === ΜΟΝΟΠΑΤΙ 2: ΑΛΟΓΟ ===
        "find_horse_start": {
            "text": (
                "Σέρνεστε κάτω από τους θάμνους, παραμερίζοντας τις φτέρες. "
                "Τελικά η τύχη σάς χαμογελά: βρίσκετε τον δερμάτινο σάκο σας. "
                "Μέσα βρίσκονται ένα παλιό πιστό στιλέτο και ένα κομμάτι μπαγιάτικο ψωμί."
            ),
            "loot": ["Παλιό Στιλέτο", "Μπαγιάτικο Ψωμί"],
            "choices": [{"label": "Ακολουθήστε τα ίχνη παραπέρα", "next_scene": "horse_found"}]
        },
        "horse_found": {
            "text": (
                "Τα ίχνη οδηγούν σε ένα ηλιόλουστο ξέφωτο. Εκεί, βόσκοντας ήσυχα, στέκεται το πολεμικό σας άλογο! "
                "Χλιμιντρίζει χαρούμενα, αναγνωρίζοντας τον αφέντη του. "
                "Στη σέλα βρίσκετε αληθινούς θησαυρούς: σπαθί, γεμάτο παγούρι και προμήθειες."
            ),
            "loot": ["Σπαθί Ιππότη", "Παγούρι Νερού", "Κομμάτι Λαρδί"],
            "choices": [{"label": "Ανεβείτε στη σέλα και καλπάστε", "next_scene": "ride_away_river"}]
        },
        "ride_away_river": {
            "text": (
                "Ο άνεμος σφυρίζει στα αυτιά σας καθώς απομακρύνεστε από το καταραμένο μέρος. "
                "Μετά από ώρες ξέφρενου καλπασμού, σταματάτε το άλογο σε ένα καθαρό ρυάκι για να πάρετε ανάσα."
            ),
            "choices": [{"label": "Ξεπεζέψτε και φάτε μεσημεριανό", "next_scene": "stream_rest"}]
        },
        "stream_rest": {
            "text": (
                "Τρώτε αχόρταγα το ψωμί, πίνοντας παγωμένο νερό. "
                "Κοιτάζοντας στην καθρέφτινη επιφάνεια του ρυακιού, βλέπετε ένα ξένο πρόσωπο. "
                "Η μνήμη είναι άδεια, ξύνοντας την ψυχή, αλλά το ζεστό πλευρό του αλόγου σάς ηρεμεί."
            ),
            "consume_loot": ["Μπαγιάτικο Ψωμί"],
            "choices": [{"label": "Καλπάστε προς τον δρόμο", "next_scene": "stone_crossroad_horse"}]
        },
        "stone_crossroad_horse": {
            "text": (
                "Το μονοπάτι σάς οδηγεί σε έναν παλιό αυτοκρατορικό δρόμο. Σύντομα, μια τεράστια πέτρα φράζει τον δρόμο. "
                "Η επιγραφή λέει: 'ΟΙ ΜΑΓΕΜΕΝΟΙ — ΔΕΞΙΑ. ΟΙ ΑΝΙΠΠΟΙ — ΑΡΙΣΤΕΡΑ'. "
                "Το άλογο χτυπάει ανυπόμονα την οπλή του, περιμένοντας την εντολή σας."
            ),
            "choices": [
                {"label": "Στρίψτε Δεξιά (Διαδρομή των Μαγεμένων)", "next_scene": "path_enchanted"},
                {"label": "Στρίψτε Αριστερά (Διαδρομή των Ανίππων)", "next_scene": "path_horseless"}
            ]
        },

        # === ΜΟΝΟΠΑΤΙ 3: ΝΑΝΟΙ ===
        "meet_dwarves": {
            "text": (
                "Προχωράτε αποφασιστικά μπροστά. Ξαφνικά, δύο νάνοι πετάγονται από τη στροφή. "
                "Βλέποντάς σας, πανικοβάλλονται, πετούν ένα βαρύ πουγκί και εξαφανίζονται στους θάμνους. "
                "Μέσα έχει χρυσό, αλλά ο ήλιος δύει και το ταφικό κρύο του δάσους κυριεύει τα πάντα."
            ),
            "loot": ["Σακούλα Χρυσού"],
            "choices": [
                {"label": "Πέστε στα βρύα και προσπαθήστε να κοιμηθείτε", "next_scene": "sleep_cold"},
                {"label": "Μαζέψτε δυνάμεις και ανάψτε φωτιά", "next_scene": "dwarf_village"}]
        },
        "sleep_cold": {"text": "Το κρύο περονιάζει ως το κόκαλο, η συνείδηση σβήνει...", "choices": [{"label": "...", "next_scene": "city_arrest"}]},
        "dwarf_village": {
            "text": (
                "Ζεσταθήκατε δίπλα στη φωτιά όλη τη νύχτα και το πρωί φτάσατε στους πρόποδες των βουνών. "
                "Εκεί, σκαλισμένο στο βράχο, βρίσκεται ένα χωριό. "
                "Ο Γέροντας των νάνων βγαίνει να σας συναντήσει, έκπληκτος από την τιμιότητά σας."
            ),
            "choices": [{"label": "Επιστρέψτε τον χρυσό στους ιδιοκτήτες", "next_scene": "dwarf_feast"}]
        },
        "dwarf_feast": {
            "text": (
                "Προς τιμήν του ευγενούς καλεσμένου, οι νάνοι κάνουν γλέντι! "
                "Σας ρωτούν για τη γενιά και τα κατορθώματά σας, αλλά εσείς σιωπάτε. "
                "Προσπαθώντας να θυμηθείτε έστω κάτι, καταλαβαίνετε ότι στο μυαλό υπάρχει μόνο ομίχλη."
            ),
            "loot": ["Νανίσια Μπύρα", "Ψητό Κότσι"],
            "choices": [{"label": "Ομολογήστε την απώλεια μνήμης", "next_scene": "dwarf_sleep"}]
        },
        "dwarf_sleep": {
            "text": (
                "Οι νάνοι κουνούν τα κεφάλια τους με συμπόνια. "
                "«Η νύχτα φέρνει συμβουλές», λέει ο Γέροντας και σας οδηγεί σε ένα μαλακό κρεβάτι. "
                "Βυθίζεστε αμέσως σε βαθύ ύπνο."
            ),
            "choices": [{"label": "Ξυπνήστε την αυγή", "next_scene": "dwarf_morning"}]
        },
        "dwarf_morning": {
            "text": (
                "Ξυπνάτε γεμάτος δυνάμεις. Ο Γέροντας κράτησε τον λόγο του: "
                "στην πύλη σάς περιμένει ο σκληρός ιχνηλάτης Μπαλίν, έτοιμος να σας οδηγήσει στους μάγους."
            ),
            "choices": [{"label": "Ξεκινήστε το ταξίδι", "next_scene": "dwarf_hike_start"}]
        },
        "dwarf_hike_start": {
            "text": (
                "Ο Μπαλίν ελέγχει τη χορδή της βαλλίστρας και σας γνέφει. "
                "Αφήνετε το φιλόξενο χωριό και εισχωρείτε στις άγριες ​​εκτάσεις. "
                "Η μεγάλη σας αναζήτηση για την αλήθεια ξεκινά."
            ),
            "new_companion": "Ιχνηλάτης Μπαλίν",
            "choices": [{"label": "Περπατήστε όλη μέρα", "next_scene": "dwarf_night_camp"}]
        },
        "dwarf_night_camp": {
            "text": (
                "Μέχρι το βράδυ, βρίσκετε μια άνετη σπηλιά. Ο Μπαλίν ανάβει μια φωτιά χωρίς καπνό. "
                "Πηγαίνετε για ύπνο πρώτος, ενώ ο νάνος κρατά σκοπιά, ακούγοντας τους ήχους της νύχτας."
            ),
            "choices": [{"label": "Προσπαθήστε να κοιμηθείτε", "next_scene": "dwarf_theft_attempt"}]
        },
        "dwarf_theft_attempt": {
            "text": (
                "Σας ξυπνάει θόρυβος και οι βρισιές του Μπαλίν! "
                "Μικρά πλάσματα των σπηλαίων προσπαθούν να σύρουν τα πράγματά σας στο σκοτάδι. "
                "Πρέπει να δράσετε αμέσως!"
            ),
            "choices": [{"label": "Αρπάξτε όπλο και διώξτε τους κλέφτες", "next_scene": "stone_crossroad_dwarf"}]
        },
        "stone_crossroad_dwarf": {
            "text": (
                "Απωθείτε τους κλέφτες και βγαίνετε στον δρόμο το πρωί. "
                "Μπροστά σας στέκεται εκείνη η πέτρα: 'ΟΙ ΜΑΓΕΜΕΝΟΙ — ΔΕΞΙΑ. ΟΙ ΑΝΙΠΠΟΙ — ΑΡΙΣΤΕΡΑ'. "
                "Ο Μπαλίν στηρίζεται στο τσεκούρι του, περιμένοντας απόφαση."
            ),
            "choices": [
                {"label": "Δεξιά (Διαδρομή των Μαγεμένων)", "next_scene": "path_enchanted"},
                {"label": "Αριστερά (Διαδρομή των Ανίππων)", "next_scene": "path_horseless"}
            ]
        },

        # === ΤΕΛΟΣ: ΠΥΡΓΟΣ ===
        "path_enchanted": {
            "text": (
                "Στρίβετε δεξιά. Ο αέρας εδώ γίνεται πυκνός, παχύρρευστος και μυρίζει όζον. "
                "Τα δέντρα γύρω είναι παραμορφωμένα από τη μαγεία, σαν παγωμένα σε αγωνία. "
                "Ο δρόμος σάς οδηγεί στην πηγή του προβλήματός σας."
            ),
            "choices": [{"label": "Συνεχίστε προς τον στόχο", "next_scene": "tower_found"}]
        },
        "tower_found": {
            "text": (
                "Το δάσος τελειώνει απότομα. Σε ένα καμένο ξέφωτο υψώνεται ο Πύργος του Σκοτεινού Αλχημιστή. "
                "Η αιχμή του από μαύρο οψιδιανό τρυπάει τον ουρανό και γύρω επικρατεί νεκρική σιγή. "
                "Η πόρτα εισόδου είναι μισάνοιχτη, σαν να σας καλεί σε παγίδα."
            ),
            "image_type": "tower",
            "choices": [
                {"label": "Μπείτε τολμηρά στην κύρια είσοδο", "next_scene": "tower_entrance"},
                {"label": "Ψάξτε προσεκτικά για άλλο δρόμο", "next_scene": "tower_side_entrance"}
            ]
        },
        "tower_entrance": {
            "text": "Σπρώχνετε τα βαριά φύλλα και μπαίνετε στο ημίφως. Η ηχώ των βημάτων σας απλώνεται στην αίθουσα... (Πλοκή υπό ανάπτυξη)",
            "choices": []
        },
        "tower_side_entrance": {
            "text": "Παραμερίζοντας τον αγκαθωτό κισσό, βρίσκετε ένα στενό παράθυρο προς το υπόγειο. Από εκεί έρχεται κρύο... (Πλοκή υπό ανάπτυξη)",
            "choices": []
        },

        # === ΧΡΟΝΙΚΟΣ ΒΡΟΧΟΣ (ΑΡΙΣΤΕΡΟ ΜΟΝΟΠΑΤΙ) ===
        "path_horseless": {
            "text": (
                "Επιλέγετε τον αριστερό δρόμο, αγνοώντας την προειδοποίηση. "
                "Στην αρχή ο δρόμος φαίνεται ειρηνικός, τα πουλιά κελαηδούν και ο ήλιος λάμπει μέσα από τα φύλλα. "
                "Αλλά μόλις ο ήλιος αγγίξει τον ορίζοντα, το δάσος βυθίζεται ακαριαία σε αδιαπέραστο, αφύσικο σκοτάδι."
            ),
            "choices": [{"label": "Προχωρήστε επιφυλακτικά", "next_scene": "ambush_loop_hit"}]
        },
        "ambush_loop_hit": {
            "text": (
                "Ξαφνικά, ένα σφύριγμα σκίζει τον αέρα από πίσω! Δεν προλαβαίνετε να αντιδράσετε. "
                "Ένα βαρύ χτύπημα με ρόπαλο στο πίσω μέρος του κεφαλιού σάς κόβει την ανάσα. "
                "Το τελευταίο πράγμα που ακούτε πριν βυθιστείτε στο κενό είναι ένα μοχθηρό, κοροϊδευτικό γέλιο..."
            ),
            "choices": [{"label": "Ξυπνήστε από τον εφιάλτη", "next_scene": "start"}]
        }
    }
}