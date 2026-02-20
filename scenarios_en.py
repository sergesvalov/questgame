SCENARIOS_EN = {
    # === PROLOGUE ===
    "start": {
        "text": (
            "Consciousness returns in agonizing jolts, every ragged breath echoing with a dull, throbbing ache in your temples. "
            "You find yourself lying face-down on damp, decomposing earth, surrounded by the unsettling whisper of ancient pines swaying high above. "
            "The name 'Sir Galahad' pulses in your mind, yet it feels entirely alien, like a fading echo of a forgotten legend. "
            "Your loyal warhorse is nowhere to be seen; only trampled moss and violently splintered branches hint at a desperate struggle. "
            "As an oppressive twilight descends, a faint, overgrown trail before you mercilessly splits in two."
        ),
        "image_type": "intro",
        "question": "The grim, primeval majesty of the forest bears down upon you. You must make a choice.",
        "choices": [
            {"label": "Scour the ground for hoofprints", "next_scene": "find_horse_start"},
            {"label": "Clench your fists and march down the path", "next_scene": "meet_dwarves"},
            {"label": "Too weak to move. Stay put and await your fate", "next_scene": "stay_sad"}
        ]
    },

    # === PATH 1: SAGE ALEXEI ===
    "stay_sad": {
        "text": (
            "Exhaustion overcomes you. You pull your knees to your chest, blankly watching as ink-black darkness swallows the surrounding woods. "
            "Suddenly, a guttural, terrifying growl erupts from merely paces away, instantly freezing the blood in your veins. "
            "A hulking shadow with burning eyes slowly separates from the tree trunks. To remain here means certain, gruesome death."
        ),
        "choices": [{"label": "Leap to your feet and sprint away blindly", "next_scene": "run_to_edge"}]
    },
    "run_to_edge": {
        "text": (
            "Whip-like branches viciously tear at your face as you tear through the impenetrable thicket like a panicked beast. "
            "The cold air sears your burning lungs, but finally, miraculously, the treeline breaks. "
            "Just ahead, shining like a beacon of salvation, flicker the warm torches of a towering city fortress."
        ),
        "choices": [{"label": "Use your last ounce of strength to reach the guards", "next_scene": "city_arrest"}]
    },
    "city_arrest": {
        "text": (
            "You hurl yourself toward the heavy forged gates, but the cold steel of crossed halberds abruptly halts your advance. "
            "Bored guards look down at your shredded, mud-caked tunic with unconcealed disgust. "
            "'We do not take beggars and vagrants!' barks the sergeant, spitting on the cobblestones. 'Throw him in the dungeon, we will sort out who he is later.'"
        ),
        "choices": [{"label": "Surrender peacefully; the strength to fight is gone", "next_scene": "dungeon_cell"}]
    },
    "dungeon_cell": {
        "text": (
            "The damp, freezing cell is suffocatingly thick with the stench of mold and utter despair. "
            "Sitting on a bed of rotting straw, a chilling realization grips you: your complete amnesia is a dark magical curse binding your mind. "
            "In a burst of helpless fury, you slam your fist against the wall and notice one of the mossy stones shift slightly."
        ),
        "choices": [{"label": "Throw your entire body weight against the loose stone", "next_scene": "secret_passage"}]
    },
    "secret_passage": {
        "text": (
            "With a heavy, grinding scrape, the stone gives way, revealing a foul, slime-coated tunnel leading into the ancient sewers. "
            "You crawl blindly through the pitch-black abyss, scraping your elbows raw, until you finally tumble out into the muddy castle moat. "
            "You are battered, filthy, and entirely exhausted but the intoxicating air of freedom fills your lungs."
        ),
        "choices": [{"label": "Scrape off the mud and cautiously look around", "next_scene": "meet_sage"}]
    },
    "meet_sage": {
        "text": (
            "From the deep, shifting shadows of the fortress wall, a figure draped in a ragged gray cloak steps out. The old man's eyes radiate an ancient, piercing wisdom. "
            "'Greetings, Galahad. I am Alexei,' he murmurs, his voice like dry leaves. 'Your memories were stolen by the Dark Alchemist. "
            "I have waited here to help you shatter his vile enchantments.'"
        ),
        "new_companion": "Sage Alexei",
        "choices": [{"label": "Trust the mysterious stranger and follow him", "next_scene": "sage_stream_journey"}]
    },
    "sage_stream_journey": {
        "text": (
            "Without question, you follow Alexei along a labyrinth of hidden, winding trails until the midday sun sits high above. "
            "Despite his frail appearance, the old man exhibits a frightening endurance. Soon, the path opens onto a crystal-clear forest brook."
        ),
        "choices": [{"label": "Call for a much-needed rest by the water", "next_scene": "sage_stream_lunch"}]
    },
    "sage_stream_lunch": {
        "text": (
            "In comfortable silence, Alexei shares a meager feast of hardtack and aged cheese. "
            "Leaning over the brook to quench your burning thirst, you gaze at your reflection and realize with mounting horror that the face staring back is a complete stranger's. "
            "Your past has been wiped perfectly clean."
        ),
        "choices": [{"label": "Grind your teeth, gather your courage, and press on", "next_scene": "stone_crossroad_sage"}]
    },
    "stone_crossroad_sage": {
        "text": (
            "As evening approaches, the unwelcoming forest yields to an ancient, grass-choked imperial road. "
            "Right in the center of the path stands a massive, moss-covered monolith bearing deeply carved runes: "
            "'THE ENCHANTED — TO THE RIGHT. THE HORSELESS — TO THE LEFT.' Alexei frowns thoughtfully at the warning."
        ),
        "choices": [
            {"label": "Turn Right (Path of the Enchanted)", "next_scene": "path_enchanted"},
            {"label": "Turn Left (Path of the Horseless)", "next_scene": "path_horseless"}
        ]
    },

    # === PATH 2: HORSE ===
    "find_horse_start": {
        "text": (
            "You crawl stubbornly beneath thorny brambles, parting wet ferns in a desperate search for clues. "
            "Finally, fortune smiles upon you: nestled in the underbrush is your tattered leather saddlebag. "
            "Inside, an old, reliable dagger gleams with a reassuring chill, alongside a hunk of stale traveler's bread."
        ),
        "loot": ["Old Trusty Dagger", "Stale Bread"],
        "choices": [{"label": "Keep following the fresh trail", "next_scene": "horse_found"}]
    },
    "horse_found": {
        "text": (
            "The tracks lead you directly to a sun-drenched clearing. There, peacefully grazing on sweet grass, stands your magnificent warhorse! "
            "Spotting you, the massive beast snorts joyfully, instantly recognizing its master. "
            "Strapped to the saddle lies a true treasure trove: a finely crafted knight's sword, a full flask of wine, and generous provisions."
        ),
        "loot": ["Knight's Sword", "Flask of Wine", "Smoked Ham"],
        "choices": [{"label": "Vault into the saddle and urge the horse into a gallop", "next_scene": "ride_away_river"}]
    },
    "ride_away_river": {
        "text": (
            "The headwind roars in your ears as you ride furiously, desperate to put distance between yourself and this cursed, malevolent forest. "
            "After hours of a breakneck, foaming gallop, the exhausted horse slows. You gently halt by a babbling, crystal-clear stream to let you both catch your breath."
        ),
        "choices": [{"label": "Dismount, water the horse, and eat", "next_scene": "stream_rest"}]
    },
    "stream_rest": {
        "text": (
            "You hungrily devour the stale bread, washing it down with freezing spring water. "
            "Catching your reflection in the glassy surface of the stream, you lock eyes with a total stranger. "
            "Your memory is a hollow void, scratching agonizingly at your soul, yet the warm, rhythmic breathing of your steed brings a small measure of comfort."
        ),
        "consume_loot": ["Stale Bread"],
        "choices": [{"label": "Remount and ride toward the old main road", "next_scene": "stone_crossroad_horse"}]
    },
    "stone_crossroad_horse": {
        "text": (
            "The winding trail eventually deposits you onto a broad, cobblestone imperial highway. A colossal boulder blocks the center of the road. "
            "A weather-beaten inscription warns: 'THE ENCHANTED — TO THE RIGHT. THE HORSELESS — TO THE LEFT.' "
            "Your warhorse stamps its heavy hoof impatiently, awaiting its rider's command."
        ),
        "choices": [
            {"label": "Pull the reins to the Right (Path of the Enchanted)", "next_scene": "path_enchanted"},
            {"label": "Pull the reins to the Left (Path of the Horseless)", "next_scene": "path_horseless"}
        ]
    },

    # === PATH 3: DWARVES ===
    "meet_dwarves": {
        "text": (
            "You stride forward with broad, confident steps. Suddenly, two stout dwarves come hurtling around a steep bend, looking as if they've seen a ghost. "
            "Spotting you, they let out muffled shrieks, drop a surprisingly heavy sack in the dirt, and instantly vanish into the juniper bushes. "
            "Gold coins spill enticingly from the sack, but the crimson sun is sinking fast, and a tomb-like chill is seizing the forest."
        ),
        "loot": ["Heavy Bag of Gold"],
        "choices": [
            {"label": "Collapse into the freezing moss and try to sleep", "next_scene": "sleep_cold"},
            {"label": "Shake off the fatigue, gather wood, and build a fire", "next_scene": "dwarf_village"}
        ]
    },
    "sleep_cold": {"text": "A merciless cold pierces you to the bone, your limbs grow numb, and your fading consciousness slowly sinks into endless dark...", "choices": [{"label": "...", "next_scene": "city_arrest"}]},
    "dwarf_village": {
        "text": (
            "You spent the long, grueling night tending your life-saving fire. By dawn's first light, you arrive at the rocky foothills of a grand mountain range. "
            "Carved seamlessly into the imposing cliff face is a hidden dwarven settlement. "
            "The gray-bearded Dwarf Elder marches out to meet you, profoundly shocked that a human did not steal their lost gold."
        ),
        "choices": [{"label": "Honorably return the gold to its rightful owners", "next_scene": "dwarf_feast"}]
    },
    "dwarf_feast": {
        "text": (
            "In honor of their unimaginably noble guest, the cavern-dwellers throw a magnificent underground feast! "
            "The dwarves eagerly ask of your noble house and past glorious deeds, but you only stare blankly into your tankard of ale. "
            "Desperately trying to dredge up a single memory, you hit a solid wall of impenetrable fog."
        ),
        "loot": ["Amber Dwarven Ale", "Succulent Roast Shank"],
        "choices": [{"label": "Honestly confess your total amnesia", "next_scene": "dwarf_sleep"}]
    },
    "dwarf_sleep": {
        "text": (
            "The grim dwarves slowly shake their heavy heads in deep sympathy. "
            "'Morning brings clearer counsel, traveler,' rumbles the Elder, personally escorting you to a guest chamber fitted with a goose-down mattress. "
            "The moment your head meets the pillow, you plunge into a deep, healing slumber."
        ),
        "choices": [{"label": "Open your eyes to the first rays of dawn", "next_scene": "dwarf_morning"}]
    },
    "dwarf_morning": {
        "text": (
            "You awaken refreshed and brimming with strength, ready to move mountains. The Elder kept his ironclad word: "
            "waiting for you at the forged gates is Balin, a heavily armed tracker, prepared to guide you into the dangerous lands of the mages."
        ),
        "choices": [{"label": "Shake hands and set out on the expedition", "next_scene": "dwarf_hike_start"}]
    },
    "dwarf_hike_start": {
        "text": (
            "Balin expertly tests the tension of his crossbow string and gives you a short, approving nod. "
            "You leave the warmth of the dwarven village behind, venturing deeper into the hostile, untamed wastelands with every step. "
            "Your grand, perilous quest for fragments of the truth begins right now."
        ),
        "new_companion": "Balin the Tracker",
        "choices": [{"label": "March relentlessly until nightfall", "next_scene": "dwarf_night_camp"}]
    },
    "dwarf_night_camp": {
        "text": (
            "As pitch-black night falls, you are fortunate enough to find a dry, wind-sheltered grotto. Balin masterfully builds a hot, smokeless fire. "
            "The dwarf insists you rest first, taking the first watch himself, his sharp ears attuned to every suspicious rustle in the dark forest."
        ),
        "choices": [{"label": "Wrap your cloak tightly and try to sleep", "next_scene": "dwarf_theft_attempt"}]
    },
    "dwarf_theft_attempt": {
        "text": (
            "Your peaceful sleep is violently shattered by a sudden clatter and a stream of inventive curses from Balin! "
            "Foul, carrion-reeking cave scavengers are using the darkness to brazenly drag your supplies into a nearby crevice. "
            "You cannot waste a single second!"
        ),
        "choices": [{"label": "Draw your blade and drive the beasts back into the shadows", "next_scene": "stone_crossroad_dwarf"}]
    },
    "stone_crossroad_dwarf": {
        "text": (
            "With swift, punishing blows, you and Balin send the nimble thieves scurrying away. By dawn, your trail merges onto a wide dirt highway. "
            "An ominous stone marker materializes from the morning mist: 'THE ENCHANTED — TO THE RIGHT. THE HORSELESS — TO THE LEFT.' "
            "Balin leans grimly on his battleaxe, leaving the heavy burden of choice entirely to you."
        ),
        "choices": [
            {"label": "Take the Right Highway (Path of the Enchanted)", "next_scene": "path_enchanted"},
            {"label": "Take the Left Highway (Path of the Horseless)", "next_scene": "path_horseless"}
        ]
    },

    # === FINALE: PARODIES ===
    "path_enchanted": {
        "text": (
            "Taking a ragged breath, you turn to the right. The very air changes here: it becomes unnaturally thick and viscous, leaving an acrid tang of ozone on your tongue. "
            "The massive tree trunks are grotesquely twisted by immense magical forces, as if frozen in a silent scream of agony. "
            "This suffocating path leads you inexorably toward the dark heart of your misfortune."
        ),
        "choices": [{"label": "Push the fear away and approach the Tower", "next_scene": "tower_found"}]
    },
    "tower_found": {
        "text": (
            "The mutilated forest abruptly ends. Standing proudly in the very center of a black, scorched clearing is the sinister Tower of the Dark Alchemist. "
            "A long spire of polished obsidian aggressively pierces the heavy, leaden sky. There are no birds, no wind—only a ringing, absolute dead silence. "
            "The massive front doors are deceptively ajar, practically daring you to step into the waiting trap."
        ),
        "image_type": "tower",
        "choices": [
            {"label": "Evaluate the situation and decide on an entrance plan", "next_scene": "tower_decide"}
        ]
    },
    "tower_decide": {
        "text": (
            "You stand before the ominous entrance of the Tower. How you choose to enter will seal your fate."
        ),
        "choices": [
            {"label": "Consult with Sage Alexei (Mario)", "next_scene": "tower_mario", "condition": lambda session: "Sage Alexei" in session.get('companions', [])},
            {"label": "Leave it to Tracker Balin (Minecraft)", "next_scene": "tower_minecraft", "condition": lambda session: "Balin the Tracker" in session.get('companions', [])},
            {"label": "Enter alone through the main doors, weapon drawn (Dark Souls)", "next_scene": "tower_darksouls_entry", "condition": lambda session: not session.get('companions', [])}
        ]
    },

    # --- MARIO BRANCH (If we have Sage Alexei) ---
    "tower_mario": {
        "text": (
            "Sage Alexei furrows his bushy brows. 'Stand back, good knight! This door is but a cunning illusion of the Dark Alchemist. I shall dispel it with the ancient incantation of Ita-lia-no!' "
            "Alexei waves his staff, muttering incomprehensible runes, but suddenly stumbles mid-sentence. The air cracks with a ringing sound, and the earth beneath your boots vanishes without a trace. "
            "You plummet straight down into a colossal, green water pipe protruding from nowhere!"
        ),
        "choices": [{"label": "Fall into the pipe screaming 'Mamma mia!'", "next_scene": "mario_world"}]
    },
    "mario_world": {
        "text": (
            "Tumbling out of the pipe, you freeze in absolute awe. The sky here is obscenely blue, and cartoonish, pixelated clouds with painted-on eyes float lazily by! "
            "The bushes look suspiciously identical to the clouds, only painted green. Beneath your feet are perfectly square brick platforms hovering in mid-air, alongside massive gold coins. "
            "Alexei, suddenly wearing red and blue plumber's overalls with an 'M' on his cap, adjusts his mustache. 'Listen closely, Galahad... The Alchemist has kidnapped Princess Peach! We must rescue her!'"
        ),
        "choices": [{"label": "Jump on a turtle shell and set off to find Bowser's Castle", "next_scene": "start"}]
    },

    # --- MINECRAFT BRANCH (If we have Balin the Dwarf) ---
    "tower_minecraft": {
        "text": (
            "Balin spits contemptuously. 'Doors are for weaklings and elves! True dwarves walk wherever they please. Stand clear, lad!' "
            "Pulling a block of red powder stamped 'TNT' from his tunic, the dwarf strikes a flint and tosses the explosive right against the obsidian wall. A deafening blast shakes the earth! "
            "The wall crumbles, but instead of the Tower's interior, it reveals a shimmering dimensional rift. Losing your footing, you tumble straight into it."
        ),
        "choices": [{"label": "Fly into the portal to the sound of colorful dwarven curses", "next_scene": "minecraft_world"}]
    },
    "minecraft_world": {
        "text": (
            "You land hard on grass that is... perfectly square. The trees are square. The clouds are square. You look down in horror to find your own hand has become frighteningly blocky, composed of giant pixels! "
            "Balin looks around with grim determination. 'Right then, knight, the sun's going down fast, zombies will be crawling out soon! No time to lose!' "
            "You cast your knightly sword aside, drop to all fours, and begin frantically punching perfect cubes of dirt with your bare (but blocky) hands to build a lifesaving 3x3 dirt hut for the first night."
        ),
        "choices": [{"label": "Hide in the dirt hut from a creeper (Game Over)", "next_scene": "start"}]
    },

    # --- DARK SOULS BRANCH (If the player is alone with the horse) ---
    "tower_darksouls_entry": {
        "text": (
            "Leaving your loyal warhorse grazing safely outside, you grip your sword hilt with both hands and shove the heavy double doors open. The vast hall is shrouded in suffocating gloom. "
            "In the exact center flickers a dim, dying bonfire, with a visibly twisted, coiled sword thrust inexplicably into its embers. Approaching cautiously, you spot glowing orange runes on the stone floor: "
            "'Illusion ahead' and 'Try rolling'. The atmosphere grows unbearably oppressive. Suddenly, from the high ceiling above, the first skeletal knight in blackened armor drops heavily onto the stones."
        ),
        "choices": [{"label": "Dodge roll and strike the skeleton", "next_scene": "darksouls_fight"}]
    },
    "darksouls_fight": {
        "text": (
            "The ancient skeleton winds up a devastating swing with its rusted broadsword. Its movements are jerky, unnatural, and terrifyingly fast. One single mistake here will cost you your life, as these foes seem entirely devoid of a stamina bar."
        ),
        "random_outcomes": ["darksouls_victory", "darksouls_defeat"],
        "choices": [
            {"label": "Cross blades!", "next_scene": "darksouls_fight"} 
        ]
    },
    "darksouls_fight_again": {
        "text": (
            "Another skeleton drops from the ceiling! There are so many of them! You are breathing heavily, but you grip your sword tight. Prepare for the next attack!"
        ),
        "random_outcomes": ["darksouls_victory", "darksouls_defeat"],
        "choices": [
            {"label": "Dodge roll and strike!", "next_scene": "darksouls_fight_again"}
        ]
    },    
    "darksouls_victory": {
        "text": (
            "By some miracle, you cleanly dodge the final blow (your invincibility frames triggered perfectly!) and instantly shatter the last skeleton's skull with a crushing riposte! "
            "The undead monstrosity crumbles to dust, leaving behind a glowing, ethereal white soul. Breathing heavily, you gaze upon the empty hall. "
            "Right before you lies a spiral staircase lined with a red carpet, leading up to the second floor of the tower. Ascending, you enter a luxurious chamber."
        ),
        "choices": [{"label": "Ascend to the second floor", "next_scene": "darksouls_floor2"}]
    },
    "darksouls_floor2": {
        "text": (
            "In the center of the room, surrounded by hundreds of burning wax candles, stands a beautiful Sorceress in a form-fitting black robe, her eyes blindfolded. "
            "She turns slowly toward you and speaks in a tender whisper: 'Touch the darkness within me, Ashen One, that you may level up... Oh, and your horse has somehow climbed onto the roof again.' "
            "You look out the window to see Roach balancing precariously on the very tip of the black obsidian spire."
        ),
        "choices": [{"label": "Kneel before the Sorceress in black", "next_scene": "start"}]
    },
    "darksouls_defeat": {
        "text": (
            "You bravely attempt to parry the incoming strike with your shield, but your timing is fatally flawed. The skeleton's rusted blade cleaves effortlessly through your steel armor. "
            "You drop to your knees as the world around you rapidly drains of color and fades to gray. Right before your glazing eyes, massive, blood-red letters slice through the air: "
            "Y O U   D I E D"
        ),
        "choices": [{"label": "Revive at the last Bonfire (Return to start)", "next_scene": "start"}]
    },

    # === TIME LOOP (LEFT PATH) ===
    "path_horseless": {
        "text": (
            "Refusing to heed bad omens, you set foot firmly on the left road. "
            "At first, the forest seems deceptively serene: unseen birds chirp cheerfully overhead, and golden sunlight peeks playfully through the soft canopy. "
            "But the very instant the crimson sun touches the horizon line, the entire world abruptly plummets into a thick, foul, and suffocating darkness."
        ),
        "choices": [{"label": "Strain your eyes and move warily through the gloom", "next_scene": "ambush_loop_hit"}]
    },
    "ambush_loop_hit": {
        "text": (
            "A lightning-fast, piercing whistle slices the air from somewhere right behind you! Your body simply cannot react in time. "
            "A blow of crushing, monstrous force from a heavy club smashes into the back of your skull, instantly driving all the air from your lungs. "
            "You plummet into the abyss of nothingness, and the last thing seared into your fading reality is a raspy, mocking, and agonizingly triumphant laugh..."
        ),
        "choices": [{"label": "Convulsively awaken from the endless nightmare", "next_scene": "start"}]
    }
}
