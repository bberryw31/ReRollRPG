import time

import random

import copy


def stage_counter(stage):
    """
    Return the current stage number starting from the given value.

    :param stage: an integer representing the first stage number
    :precondition: stage must be a non-negative integer
    :postcondition: generate the current stage number
    :return: the next stage number

    >>> counter = stage_counter(0)
    >>> next(counter)
    0
    >>> next(counter)
    1
    """
    while True:
        yield stage
        stage += 1


def clear_screen(stage):
    """
    Clear the terminal screen and display the game logo based on the current stage.

    :param stage: an integer representing the current stage
    :precondition: stage must be a non-negative integer
    :postcondition: clears the screen and prints the full game logo or a shortened version depending on the stage
    """
    print("\033[2J\033[H", end="")
    logo_re_roll_color = "\033[1m\033[{}m".format(random.choice(range(92, 97)))
    logo_re_roll = r"""

         ___           ___           ___           ___           ___       ___ 
        /\  \         /\  \         /\  \         /\  \         /\__\     /\__\
       /::\  \       /::\  \       /::\  \       /::\  \       /:/  /    /:/  /
      /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/  /    /:/  / 
     /::\~\:\  \   /::\~\:\  \   /::\~\:\  \   /:/  \:\  \   /:/  /    /:/  /  
    /:/\:\ \:\__\ /:/\:\ \:\__\ /:/\:\ \:\__\ /:/__/ \:\__\ /:/__/    /:/__/   
    \/_|::\/:/  / \:\~\:\ \/__/ \/_|::\/:/  / \:\  \ /:/  / \:\  \    \:\  \   
       |:|::/  /   \:\ \:\__\      |:|::/  /   \:\  /:/  /   \:\  \    \:\  \  
       |:|\/__/     \:\ \/__/      |:|\/__/     \:\/:/  /     \:\  \    \:\  \ 
       |:|  |        \:\__\        |:|  |        \::/  /       \:\__\    \:\__\
        \|__|         \/__/         \|__|         \/__/         \/__/     \/__/"""
    logo_rr = r"""
 ________ ________ ________ ________ _________
 ___  __ \___  __ \___  __ \___  __ \__  ____/
 __  /_/ /__  /_/ /__  /_/ /__  /_/ /_  / __
 _  _, _/ _  _, _/ _  _, _/ _  ____/ / /_/ /
 /_/ |_|  /_/ |_|  /_/ |_|  /_/      \____/



"""
    logo_rpg_color = "\033[0m\033[91m"
    logo_rpg = r"""
                            ________ ________ _________
                            ___  __ \___  __ \__  ____/
                            __  /_/ /__  /_/ /_  / __
                            _  _, _/ _  ____/ / /_/ /
                            /_/ |_|  /_/      \____/

    """
    if stage == 0:
        print(logo_re_roll_color, logo_re_roll, logo_rpg_color, logo_rpg, "\033[0m")
    else:
        print(logo_re_roll_color, logo_rr, "\033[0m")


def game_intro():
    """
    Display the game intro screen and wait for the user to start the game.

    :precondition: user's input must be standard input
    :postcondition: display welcome message and loading animation if the user enters 'start' or 's'
    :postcondition: display random error messages for invalid inputs
    :return: True when a valid input is received to start the game
    """
    clear_screen(0)
    print("\n\033[92m                            🎲 Welcome to ReRollRPG 🎲\033[0m")
    print("\n\033[2m\tEnter \'S\' or 'Start' to begin your adventure.\033[0m")
    error_counter = 0
    while True:
        user_input = input("\n > ").strip().lower()
        if user_input == "start" or user_input == "s":
            start_counter = 1
            while start_counter < 5:
                clear_screen(0)
                print("\n\033[0mLoading game" + ("." * start_counter))
                start_counter += 1
                time.sleep(0.5)
            return True
        else:
            if error_counter < 3:
                response = [
                    "Invalid input. Type 'start' to begin.",
                    "Unknown command. Type 'start' to begin."
                ]
                error_counter += 1
            else:
                response = [
                    "Excuse me? Type 'start' to begin.",
                    "Stop playing with me. Type 'start' to begin.",
                    "Lord have mercy.. Type 'start' to begin.",
                    "Are you kidding me? Type 'start' to begin.",
                    "I'm about to lose it. Type 'start' to begin.",
                ]
            print(random.choice(response))


def random_character(class_pool):
    """
    Generate a random character with randomized stats, HP, and class.

    :param class_pool: a list of available classes as strings
    :precondition: class_pool must be a non-empty list
    :precondition: class_pool must be a homogenous list of strings
    :precondition: element of class_pool must be a key in classes dictionary
    :postcondition: select a random class from class_pool
    :postcondition: assign 20–25 total stat points randomly across STR, DEX, INT, and LUC
    :postcondition: generate a random HP value between 5 and 10
    :postcondition: assign HP value to max HP
    :postcondition: assign 10 re-roll counts and 13 if class is Gambler
    :postcondition: generate a dictionary containing all the generated character attributes
    :return: a dictionary representing the generated character
    """
    classes = {
        "Bodybuilder": {
            "class_name": "Bodybuilder",
            "description": "Brain’s on cooldown, biceps are not.",
            "main_stats": ["STR"],
            "icon": "🦾 "
        },
        "Boxer": {
            "class_name": "Boxer",
            "description": "Footwork silky, punches filthy.",
            "main_stats": ["STR", "DEX"],
            "icon": "🥊 "
        },
        "Hunter": {
            "class_name": "Hunter",
            "description": "Hope I don't run out of arrows.",
            "main_stats": ["DEX"],
            "icon": "🏹 "
        },
        "Chef": {
            "class_name": "Chef",
            "description": "Your fate is medium rare.",
            "main_stats": ["DEX", "INT"],
            "icon": "🔪 "
        },
        "Fortuneteller": {
            "class_name": "Fortuneteller",
            "description": "Sees the future, then makes it worse.",
            "main_stats": ["INT"],
            "icon": "🔮 "
        },
        "Gamer": {
            "class_name": "Gamer",
            "description": "Powered by instant noodles and energy drinks.",
            "main_stats": ["INT", "LUC"],
            "icon": "🎮 "
        },
        "Gambler": {
            "class_name": "Gambler",
            "description": "Lives by the dice, fights by the odds.",
            "main_stats": ["LUC"],
            "icon": "🎰 "
        },
        "Pro Wrestler": {
            "class_name": "Pro Wrestler",
            "description": "Delivers justice from the top rope.",
            "main_stats": ["STR", "LUC"],
            "icon": "👹 "
        },
        "Jimmy": {
            "class_name": "Jimmy",
            "description": "Jimmy Jimster, the Legendary Adventurer.",
            "main_stats": ["STR", "DEX", "INT", "LUC"],
            "icon": "👑 "
        }
    }
    random_stats = {
        "str": 0,
        "dex": 0,
        "int": 0,
        "luc": 0
    }
    stats_list = ["str", "dex", "int", "luc"]
    total_stats = random.randint(20, 25)
    while total_stats > 0:
        random_stats[random.choice(stats_list)] += 1
        total_stats -= 1
    random_class = random.choice(class_pool)
    random_hp = random.randint(5, 10)
    character = {
        "stats": random_stats,
        "class": classes[random_class],
        "HP": random_hp,
        "max_HP": random_hp,
        "roll": 10,
    }
    if random_class == "Gambler":
        character["roll"] += 3
    return character


def select_character(class_pool, restart_count):
    """
    Prompt the user to confirm or re-roll the generated character

    :param class_pool: a list of available classes as strings
    :param restart_count: an integer representing the number of game restarts
    :precondition: class_pool must be a non-empty list
    :precondition: class_pool must be a homogenous list of strings
    :precondition: restart_count must be an integer
    :postcondition: unlock the "Jimmy" class if restart_count is 2
    :postcondition: unlock the "Gambler" class if the user re-rolls 5 times
    :postcondition: display the attributes of a newly generated character
    :postcondition: prompt the user to confirm or re-roll character
    :postcondition: return the generated character if the user confirms
    :postcondition: generate and display a new random character if user re-rolls
    :postcondition: display an error message if user input is invalid
    :return: a dictionary representing a character
    """
    roll_count = 0
    while True:
        clear_screen(1)
        print("\033[1mSelect a character!\n")
        if restart_count == 2:
            class_pool.append("Jimmy")
            print("\t\033[2mUnlocked Class: "
                  "\033[0m\033[91m\033[1mJimmy Jimster the legendary adventurer\033[0m 👑")
            restart_count += 1
        if roll_count == 5:
            class_pool.append("Gambler")
            print("\t\033[2mUnlocked Class: "
                  "\033[0m\033[91m\033[1mGambler\033[0m 🎰")
        new_character = random_character(class_pool)
        print(f"""
            \033[96mNew Character\033[0m

        \033[1m\033[33mSTR\033[0m : {new_character["stats"]["str"]} \t\033[2m Reduce damage taken\033[0m
        \033[1m\033[33mDEX\033[0m : {new_character["stats"]["dex"]} \t\033[2m Attack accuracy & dodge chance\033[0m
        \033[1m\033[33mINT\033[0m : {new_character["stats"]["int"]} \t\033[2m Get inspired\033[0m
        \033[1m\033[33mLUC\033[0m : {new_character["stats"]["luc"]} \t\033[2m Critical attack chance\033[0m
    
    HP : \033[1m{new_character["HP"]}\033[0m\t\033[2m Character health points\033[0m
    🎲 : \033[1m{new_character["roll"]}\033[0m\t\033[2m Available re-rolls in game\033[0m
    
    Class : \033[91m{new_character["class"]["class_name"]}\033[0m {new_character["class"]["icon"]}
        \033[95m\033[2m\033[3m{new_character["class"]["description"]}\033[0m
    
    Main Stats: \033[92m\033[1m{" + ".join(new_character["class"]["main_stats"])}\033[0m\t\033[2m Damage modifier\033[0m

        1. Confirm
        2. Re-roll
        """)
        while True:
            user_input = input(
                "\033[93mEnter \'1\' to confirm, \'2\' to re-roll.\033[0m\n > "
            ).strip()
            if user_input == "2":
                roll_count += 1
                break
            elif user_input == "1":
                return new_character
            else:
                print("Invalid input.")


def generate_map(level):
    """
    Generate a map layout for the given game stage level.

    :param level: a non-negative integer representing the current stage of the game
    :precondition: level must be a non-negative integer
    :postcondition: generate a 17x10 grid representing the map
    :postcondition: include different elements depending on the level
    :postcondition: place enemies and rewards randomly within certain area of the map
    :postcondition: place water tiles randomly within the map
    :postcondition: modify the map into a boss room on level 4
    :postcondition: generate a list of lists containing map elements
    :return: a list of lists representing the map layout
    """
    wall = random.choice(["🟨 ", "🟧 ", "🔳 ", "🔲 ", "⬜️ ", "🟦 "])
    empty = ".  "
    door = "🚪 "
    locked_door = "🔒 "
    reward = "🎁 "
    reward_spots = [(1, 1), (1, 15), (8, 1), (8, 15)]
    enemies = ["🐜 ", "🦇 ", "🦖 ", "🐊 ", "🦄 ", "🐍 ", "🦂 ", "🐌 ", "🦟 "]
    boss = "💀 "
    enemy_zone_left = [(row, col) for row in range(3, 7) for col in range(3, 6)]
    enemy_zone_right = [(row, col) for row in range(3, 7) for col in range(11, 14)]
    enemy_zone = enemy_zone_left + enemy_zone_right
    room_default = (
            [[wall] * 17] +
            [[wall] + [empty] * 15 + [wall] for _ in range(8)] +
            [[wall] * 17]
    )
    room = room_default.copy()
    if level == 0:
        room[0][8] = door
        room[9][8] = locked_door
        room[4][4] = "\033[1m\033[33mW  \033[0m"
        room[5][4] = "\033[1m\033[33mS  \033[0m"
        room[5][3] = "\033[1m\033[33mA  \033[0m"
        room[5][5] = "\033[1m\033[33mD  \033[0m"
        room[3][4] = "⬆️ "
        room[6][4] = "⬇️ "
        room[5][2] = "⬅️ "
        room[5][6] = "➡️ "
        room[4][11] = "\033[1m\033[33mQ  \033[0m"
        room[4][12] = "  Q"
        room[4][13] = "UIT"
        room[4][14] = "   "
        room[3][8] = reward
    elif level == 4:
        for row in range(1, 9):
            for col in range(1, 6):
                room[row][col] = wall
            for col in range(11, 16):
                room[row][col] = wall
        room[0][8] = door
        room[9][8] = locked_door
        room[4][8] = boss
    else:
        room[0][8] = door
        room[9][8] = locked_door
        rewards = random.sample(reward_spots, k=level)
        for row, col in rewards:
            room[row][col] = reward
        water_generator(enemy_zone_left, room)
        water_generator(enemy_zone_right, room)
        enemy_count = 0
        while enemy_count < level + 1:
            enemy_row, enemy_col = random.choice(enemy_zone)
            if room[enemy_row][enemy_col] == ".  ":
                room[enemy_row][enemy_col] = random.choice(enemies)
                enemy_count += 1
    return room


def water_generator(zone, room):
    """
    Place water tiles randomly within a specific area of the room.

    :param zone: a list of tuples representing a specific area of the room where water tiles may appear
    :param room: a list representing the current map
    :precondition: zone must be a list of tuples representing coordinates of room
    :precondition: room must be a list of lists representing a 17x10 grid with valid map elements
    :postcondition: a random coordinate within the zone is selected and replaced with a water tile.
    :postcondition: random adjacent coordinates are replaced with water tiles.
    """
    water_row, water_col = random.choice(zone)
    water_row_range = range(water_row - 1, water_row + 2)
    water_col_range = range(water_col - 1, water_col + 2)
    water_spots = [(row, col) for row in water_row_range for col in water_col_range]
    waters = random.sample(water_spots, k=random.randint(1, 9))
    for row, col in waters:
        room[row][col] = "🌀 "
    room[water_row][water_col] = "🌀 "


def display_map(room, character):
    """
    Display the game map with the player's current position and character info.

    :param room: a list of lists representing the current game map
    :param character: a dictionary representing the player's character
    :precondition: room must be a list of lists representing a 17x10 grid with valid map elements
    :precondition: character must be a dictionary with keys 'coordinates', 'class', 'HP', 'max_HP', 'roll', and 'stats'
    :precondition: character['coordinates'] must be a tuple of two integers within the map boundaries
    :postcondition: print a visual representation of the character's current HP and max HP
    :postcondition: print the character's re-roll count and stats
    :postcondition: print a visual representation of the current map and the character's current location
    """
    temp_room = copy.deepcopy(room)
    row, col = character["coordinates"]
    temp_room[row][col] = character["class"]["icon"]
    map_print = ""
    for row in temp_room:
        map_print += "".join(row) + "\n"
    current_hp = f"\033[91m❤︎\033[0m" * character["HP"] + "\033[2m❤︎\033[0m" * (character["max_HP"] - character["HP"])
    map_print += f"""               ℹ️ \033[95m\033[1mCHARACTER INFO\033[0m ℹ️
               HP \033[32m{current_hp}\033[0m
                     🎲 \033[91m{character["roll"]}\033[0m
                  STR \033[32m{character["stats"]["str"]}\033[0m DEX \033[32m{character["stats"]["dex"]}\033[0m
                  INT \033[32m{character["stats"]["int"]}\033[0m LUC \033[32m{character["stats"]["luc"]}\033[0m"""
    print(map_print)


def get_user_action():
    while True:
        user_input = input(
            "\033[2mEnter your choice of action.\033[0m\n > "
        )
        user_input = user_input.strip().lower()
        if user_input == "w" or user_input == "up":
            return -1, 0
        elif user_input == "s" or user_input == "down":
            return 1, 0
        elif user_input == "a" or user_input == "left":
            return 0, -1
        elif user_input == "d" or user_input == "right":
            return 0, 1
        elif user_input == "q" or user_input == "quit":
            user_confirm = input("\033[91mAre you sure you want to quit? \'Y\' to confirm.\033[0m\n > ")
            user_confirm = user_confirm.strip().lower()
            if user_confirm == "y":
                return "q"
            else:
                continue
        else:
            print("Invalid input.")


def validate_action(character, action, room, stage_level):
    if action == "r":
        return "r"
    elif action == "q":
        return "q"
    row, col = character["coordinates"]
    character_new_location = (row + action[0], col + action[1])
    destination = room[character_new_location[0]][character_new_location[1]]
    if destination == ".  ":
        return character_new_location
    elif destination in ["🐜 ", "🦇 ", "🦖 ", "🐊 ", "🦄 ", "🐍 ", "🦂 ", "🐌 ", "🦟 ", "💀 "]:
        if fight_enemy(destination, character, stage_level):
            if not open_reward(character):
                room[character_new_location[0]][character_new_location[1]] = "🎁 "
                return character["coordinates"]
            room[character_new_location[0]][character_new_location[1]] = ".  "
            return character_new_location
        elif character["HP"] <= 0:
            return "dead"
        else:
            return character["coordinates"]
    elif destination == "🎁 ":
        if open_reward(character):
            room[character_new_location[0]][character_new_location[1]] = ".  "
            return character_new_location
        else:
            return character["coordinates"]
    elif destination == "🌀 ":
        drink_water(character)
        if character["HP"] <= 0:
            return "dead"
        else:
            return character["coordinates"]
    elif destination == "🚪 ":
        if room_cleared(room):
            return "clear"
        else:
            return "\033[91mYou must first defeat all enemies!\033[0m"
    elif destination == "🔒 ":
        return "\033[91mThe door is locked from the other side.\033[0m"
    else:
        return "\033[91mSomething is blocking your way...\033[0m"


def drink_water(character):
    user_decision = input("\033[91m\033[2mWater does not seem so clean... \033[0m\n"
                          "\033[93mDrink water? \nEnter \'Y\' to confirm.\n"
                          "\033[0m > ").strip().lower()
    if user_decision == "y":
        odds = random.randint(1, 100)
        if odds < 25:
            random_stat = random.choice(["str", "dex", "int", "luc"])
            random_change = random.randint(1, 2)
            character["stats"][random_stat] += random_change
            print(f"\033[94mYou feel stronger. \033[0m\n"
                  f"\t\033[1mGain \033[96m+{random_change}\033[0m \033[1m{random_stat.upper()}\033[0m!")
        elif odds < 50:
            random_increase = random.choice(range(1, 2))
            character["HP"] += random_increase
            print(f"\033[93mYou feel refreshed. \033[0m\n"
                  f"\t\033[1mHeal \033[96m{random_increase}\033[0m \033[1mHP\033[0m!")
        else:
            character["HP"] -= 1
            print(f"\033[91mYou have been poisoned! \033[0m\n"
                  f"\t\033[1mLose \033[96m1\033[0m \033[1mHP\033[0m")
        time.sleep(2)


def open_reward(character):
    def reward_hp():
        heal = round(random.uniform(0.1, 0.5) * character["max_HP"] + 0.5)

        def apply():
            character["HP"] = min(character["max_HP"], character["HP"] + heal)

        return f"\033[1mHeal \033[96m{heal}\033[0m \033[1mHP\033[0m", apply

    def reward_max_hp():
        increase = random.choice([1, 2])

        def apply():
            character["max_HP"] += increase
            character["HP"] += increase

        return f"\033[1mGain \033[96m{increase}\033[0m \033[1mMax HP\033[0m", apply

    def reward_stat():
        stat = random.choice(["str", "dex", "int", "luc"])
        increase = random.choice([1, 2])

        def apply():
            character["stats"][stat] += increase

        return f"\033[1mGain \033[96m{increase} \033[0m\033[1m{stat.upper()}\033[0m", apply

    def reward_random_stat():
        stat = random.choice(["str", "dex", "int", "luc"])
        increase = random.randint(-2, 3)

        def apply():
            character["stats"][stat] += increase
            print(f"\n\t\033[1mGained \033[96m{increase} \033[0m\033[1m{stat.upper()}\033[0m!!")
            time.sleep(1.5)

        return f"\033[1mGain \033[96m-2 ~ +3\033[0m\033[1m random stat\033[0m", apply

    user_decision = input(
        "\033[93mClaim Reward? \nEnter \'Y\' to confirm.\033[0m\n > "
    ).strip().lower()
    if user_decision != "y":
        return False
    print("\n\t\033[95mOpening Reward\033[0m", end="")
    for _ in range(3):
        time.sleep(0.5)
        print("\033[95m .\033[0m", end="", flush=True)
    print("\n")
    while True:
        first_reward = random.choice([reward_hp, reward_stat, reward_random_stat, reward_max_hp])()
        second_reward = random.choice([reward_hp, reward_stat, reward_random_stat, reward_max_hp])()
        print("\n\t 1. ", first_reward[0])
        print("\t 2. ", second_reward[0], "\n")
        while True:
            print(f"\033[2mRemaining re-rolls\033[0m 🎲 \033[91m\033[1m{character['roll']}\033[0m")
            user_input = input(
                "\033[93mEnter \'1\' or \'2\' to confirm, \'R\' to re-roll.\033[0m\n > "
            ).strip().lower()
            if user_input == "1":
                first_reward[1]()
                return True
            elif user_input == "2":
                second_reward[1]()
                return True
            elif user_input == "r":
                if character["roll"] == 0:
                    print("\033[91m\033[1mYou are out of re-rolls!\033[0m\n\033[2mBetter take what you have...")
                    continue
                character["roll"] -= 1
                break
            else:
                print("Invalid input.")

def fight_enemy(enemy, character, stage_level):
    enemies = {
        "🐜 ": {
            "name": "Tunnel Ant",
            "HP": 4 * stage_level,
            "atk_mod": round(0.8 * stage_level, 1)
        },
        "🦇 ": {
            "name": "Cave Bat",
            "HP": 5 * stage_level,
            "atk_mod": round(1.0 * stage_level, 1)
        },
        "🦖 ": {
            "name": "Ancient Raptor",
            "HP": 8 * stage_level,
            "atk_mod": round(1.3 * stage_level, 1)
        },
        "🐊 ": {
            "name": "Angry Crocodile",
            "HP": 7 * stage_level,
            "atk_mod": round(1.2 * stage_level, 1)
        },
        "🦄 ": {
            "name": "Baby Unicorn",
            "HP": 6 * stage_level,
            "atk_mod": round(1.3 * stage_level, 1)
        },
        "🐍 ": {
            "name": "Fat Serpent",
            "HP": 5 * stage_level,
            "atk_mod": round(1.1 * stage_level, 1)
        },
        "🦂 ": {
            "name": "Scorpion Prince",
            "HP": 4 * stage_level,
            "atk_mod": round(1.1 * stage_level, 1)
        },
        "🐌 ": {
            "name": "Doom Slug",
            "HP": 10 * stage_level,
            "atk_mod": round(0.5 * stage_level, 1)
        },
        "🦟 ": {
            "name": "Giant Mosquito",
            "HP": 5 * stage_level,
            "atk_mod": round(1.0 * stage_level, 1)
        },
        "💀 ": {
            "name": "Dungeon Boss",
            "HP": 50,
            "atk_mod": 5
        }
    }
    user_input = input(f"\033[93mFight \033[91m\033[1m{enemies[enemy]["name"]}\033[0m"
                       f"\033[93m? \nEnter \'Y\' to confirm.\033[0m\n > ")
    if user_input.strip().lower() == "y":
        print("\n\033[91m\033[1mYou are in combat!\033[0m\n")
        print(f" {character["class"]["icon"]} " + "\033[91m❤︎\033[0m" * character["HP"] + "\n")
        print(f" {enemy} " + "\033[93m❤︎\033[0m" * enemies[enemy]["HP"] + "\n")
        while enemies[enemy]["HP"] > 0 and character["HP"] > 0:
            time.sleep(1)
            character_damage = 1
            for stat in character["class"]["main_stats"]:
                character_damage += round(character["stats"][stat.lower()] * random.random() * 0.5)
            if character["stats"]["luc"] * 3 + 25 > random.randint(1, 100):
                enemies[enemy]["HP"] -= round(character_damage * 1.5)
                print("\033[94m\033[1mCRITICAL HIT!\033[0m")
                print(f"You attacked {enemies[enemy]["name"]} dealing "
                      f"\033[91m\033[1m{round(character_damage * 1.5)}\033[0m damage!\n")
                print(f" {enemy} " + "\033[93m❤︎\033[0m" * enemies[enemy]["HP"] + "\n")
            elif character["stats"]["dex"] * 2 + 60 < random.randint(1, 100):
                print("\033[94mYou Missed!\033[0m\n")
            else:
                enemies[enemy]["HP"] -= character_damage
                print(f"You attacked {enemies[enemy]["name"]} dealing "
                      f"\033[91m\033[1m{character_damage}\033[0m damage!\n")
                print(f" {enemy} " + "\033[93m❤︎\033[0m" * enemies[enemy]["HP"] + "\n")
            if character["stats"]["int"] + 10 > random.randint(1, 100):
                character["roll"] += 1
                print("\033[95m\033[2mYou gained inspiration from combat!\033[0m 🎲 \033[93m\033[1m+1\033[0m\n")
            time.sleep(1)
            if enemies[enemy]["HP"] > 0:
                enemy_damage = (1 + random.random()) * enemies[enemy]["atk_mod"]
                if character["stats"]["dex"] * 2 + 25 > random.randint(1, 100):
                    print("\033[95mYou dodged the enemy's attack!\033[0m\n")
                else:
                    received_damage = max(1, round(enemy_damage - random.random() * character["stats"]["str"] * 0.5))
                    print(f"{enemies[enemy]["name"]} attacked you dealing "
                          f"\033[91m\033[1m{received_damage} damage!\n")
                    character["HP"] -= received_damage
                    print(f" {character["class"]["icon"]} " + "\033[91m❤︎\033[0m" * character["HP"] + "\n")
                if character["stats"]["int"] + 10 > random.randint(1, 100):
                    print("\033[95m\033[2mYou gained inspiration from combat!\033[0m 🎲 \033[93m\033[1m+1\033[0m\n")
        if character["HP"] <= 0:
            return False
        else:
            print(f"\033[99mYou defeated {enemies[enemy]["name"]}!")
            return True
    else:
        return False


def room_cleared(room) -> bool:
    room_is_clear = True
    for row in room:
        for col in row:
            if col in ["🐜 ", "🦇 ", "🦖 ", "🐊 ", "🦄 ", "🐍 ", "🦂 ", "🐌 ", "🦟 ", "💀 "]:
                room_is_clear = False
    return room_is_clear


def game():
    """
    Drive the game.
    """
    restart = True
    restart_counter = 0
    class_pool = [
        "Bodybuilder", "Hunter", "Fortuneteller", "Chef", "Pro Wrestler", "Gamer", "Boxer"
    ]
    while restart:
        restart = False
        dead = False
        if game_intro():
            current_character = select_character(class_pool, restart_counter)
            stage = stage_counter(0)
            current_stage = next(stage)
            while not dead:
                current_character["coordinates"] = 8, 8
                current_map = generate_map(current_stage)
                clear_screen(1)
                while not dead:
                    display_map(current_map, current_character)
                    user_action = validate_action(current_character, get_user_action(), current_map, current_stage)
                    clear_screen(1)
                    if user_action == "q":
                        print("\n\n\033[97m\tCoward! I mean.. thanks for playing!\033[0m\n\n")
                        return
                    elif user_action == "dead":
                        print("\n\n\033[91m\tYou have died...\033[0m\n")
                        dead = True
                        while True:
                            user_restart = input(
                                "\033[93mEnter \'R\' to restart, \'Q\' to quit.\033[0m\n > "
                            ).strip().lower()
                            if user_restart == "r":
                                restart = True
                                restart_counter += 1
                                break
                            elif user_restart == "q":
                                print("\033[1m\033[97m\t\nThanks for playing!\033[0m\n")
                                return
                            else:
                                print("Invalid input.")
                    elif type(user_action) == tuple:
                        current_character["coordinates"] = user_action
                    elif user_action == "clear":
                        if current_stage == 4:
                            print("\033[1m\033[93m\n\tDungeon Cleared\033[0m\n")
                            user_restart = input(
                                "\033[93mEnter \'R\' to play again, any other key to quit.\033[0m\n > "
                            ).strip().lower()
                            if user_restart == "r":
                                restart = True
                                restart_counter += 1
                                break
                            else:
                                print("\033[1m\033[97m\n\tThanks for playing!\033[0m\n")
                                return
                        else:
                            current_stage = next(stage)
                            break
                    else:
                        print(user_action)


if __name__ == "__main__":
    game()

