import time

import random

import copy

def stage_counter(stage):
    while True:
        yield stage
        stage += 1

def clear_screen(stage):
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
    clear_screen(0)
    print("\n\033[92m                            🎲 Welcome to ReRollRPG 🎲\033[0m")
    print("\n\033[2m   Type 'start' to begin your adventure.\033[0m")
    error_counter = 0
    while True:
        user_input = input("\n> ").strip().lower()
        if user_input == "start" or user_input == "s":
            start_counter = 1
            while start_counter < 3:
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


def random_character():
    classes = {
        "Bodybuilder": {
            "class_name": "Bodybuilder",
            "description": "There is nothing that cannot be lifted.",
            "main_stats": ["STR"],
            "icon": "🦾 "
        },
        "Hunter": {
            "class_name": "Hunter",
            "description": "Hunts rabbits for a living.",
            "main_stats": ["DEX"],
            "icon": "🏹 "
        },
        "Fortuneteller": {
            "class_name": "Fortuneteller",
            "description": "Sees the future, then makes it worse.",
            "main_stats": ["INT"],
            "icon": "🔮 "
        },
        "Gambler": {
            "class_name": "Gambler",
            "description": "Lives by the dice, fights by the odds.",
            "main_stats": ["LUC"],
            "icon": "🎰 "
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
    random_class = random.choice(list(classes.keys()))
    random_hp = random.randint(5, 10)
    character = {
        "stats": random_stats,
        "class": classes[random_class],
        "HP": random_hp,
        "max_HP": random_hp,
        "roll": 10,
    }
    if random_class == "Gambler":
        character["roll"] += 10
    return character


def select_character():
    clear_screen(1)
    print("Select a character!")
    while True:
        new_character = random_character()
        clear_screen(1)
        print(f"""
            \033[96mNew Character\033[0m

        \033[1m\033[33mSTR\033[0m : {new_character["stats"]["str"]}
        \033[1m\033[33mDEX\033[0m : {new_character["stats"]["dex"]}
        \033[1m\033[33mINT\033[0m : {new_character["stats"]["int"]}
        \033[1m\033[33mLUC\033[0m : {new_character["stats"]["luc"]}
    
    HP : {new_character["HP"]}
    Class : \033[91m{new_character["class"]["class_name"]}\033[0m {new_character["class"]["icon"]}
        {new_character["class"]["description"]}       
    Main Stats: \033[92m\033[1m{" + ".join(new_character["class"]["main_stats"])}\033[0m

        1. Confirm
        2. Re-roll
        """)
        while True:
            user_input = input("Enter 1 to Confirm, 2 to Re-roll.\n> ").strip()
            if user_input == "2":
                break
            elif user_input == "1":
                return new_character
            else:
                print("Invalid input.")


def generate_map(level, character):
    wall = random.choice(["🟨 ", "🟧 ", "🔳 ", "🔲 ", "⬜️ ", "🟦 "])
    empty = ".  "
    door = "🚪 "
    locked_door = "🔒 "
    reward = "🎁 "
    reward_spots = [(1, 1), (1, 15), (8, 1), (8, 15)]
    enemies = ["🐜 ", "🦇 ", "🦖 ", "🐊 ", "🦄 ", "🐍 ", "🦂 ", "🐌 ", "🦟 "]
    enemy_zone_left = [(row, col) for row in range(2, 8) for col in range(2, 7)]
    enemy_zone_right = [(row, col) for row in range(2, 8) for col in range(10, 15)]
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
    else:
        room[0][5] = door
        room[0][11] = door
        room[9][8] = locked_door
        rewards = random.sample(reward_spots, k=level)
        for row, col in rewards:
            room[row][col] = reward
        enemy_spot = random.sample(enemy_zone, k=level + 1)
        for row, col in enemy_spot:
            room[row][col] = random.choice(enemies)
    return room


def display_map(room, character):
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
        user_input = input("\033[2mEnter your choice of action.\033[0m\n > ")
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
            user_confirm = input("\033[91mAre you sure you want to quit? Y to confirm.\033[0m\n > ")
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
    elif destination in ["🐜 ", "🦇 ", "🦖 ", "🐊 ", "🦄 ", "🐍 ", "🦂 ", "🐌 ", "🦟 "]:
        if fight_enemy(destination, character, stage_level):
            if not open_reward(character):
                room[character_new_location[0]][character_new_location[1]] = "🎁 "
                return character["coordinates"]
            room[character_new_location[0]][character_new_location[1]] = ".  "
            return character_new_location
        elif character["HP"] <= 0:
            death()
        else:
            return character["coordinates"]
    elif destination == "🎁 ":
        if open_reward(character):
            room[character_new_location[0]][character_new_location[1]] = ".  "
            return character_new_location
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


def open_reward(character):
    def reward_hp():
        heal = round(random.uniform(0.1, 0.5) * character["max_HP"] + 0.5)

        def apply():
            character["HP"] = min(character["max_HP"], character["HP"] + heal)

        return f"\033[1mHeal \033[96m{heal}\033[0m \033[1mHP\033[0m", apply

    def reward_max_hp():
        increase = random.choice([-1, 1, 2])

        def apply():
            character["max_HP"] += increase
            character["HP"] += increase

        return f"\033[1mGain \033[96m{increase}\033[0m \033[1mMax HP\033[0m", apply

    def reward_stat():
        stat = random.choice(["str", "dex", "int", "luc"])
        increase = random.choice([-1, 1, 2])

        def apply():
            character["stats"][stat] += increase

        return f"\033[1mGain \033[96m{increase} \033[0m\033[1m{stat.upper()}\033[0m", apply

    def reward_random_stat():
        stat = random.choice(["str", "dex", "int", "luc"])
        increase = random.randint(-3, 3)

        def apply():
            character["stats"][stat] += increase
            print(f"\n\t\033[1mGained \033[96m{increase} \033[0m\033[1m{stat.upper()}\033[0m!!")
            time.sleep(1.5)

        return f"\033[1mGain \033[96m-3 ~ +3\033[0m\033[1m random stat\033[0m", apply

    user_decision = input("\033[93mClaim Reward? Y to confirm.\033[0m\n > ").strip().lower()
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
            print(f"\033[2mRemaining Re-rolls\033[0m 🎲 \033[91m\033[1m{character['roll']}\033[0m")
            user_input = input("\033[93mEnter 1 or 2 to confirm, R to re-roll\033[0m\n > ").strip().lower()
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
            "HP": 5 * stage_level,
            "atk_mod": round(1.0 * stage_level, 1)
        },
        "🦇 ": {
            "name": "Cave Bat",
            "HP": 6 * stage_level,
            "atk_mod": round(1.1 * stage_level, 1)
        },
        "🦖 ": {
            "name": "Ancient Raptor",
            "HP": 12 * stage_level,
            "atk_mod": round(1.5 * stage_level, 1)
        },
        "🐊 ": {
            "name": "Crocodile",
            "HP": 10 * stage_level,
            "atk_mod": round(1.3 * stage_level, 1)
        },
        "🦄 ": {
            "name": "Baby Unicorn",
            "HP": 8 * stage_level,
            "atk_mod": round(1.4 * stage_level, 1)
        },
        "🐍 ": {
            "name": "Fat Serpent",
            "HP": 7 * stage_level,
            "atk_mod": round(1.3 * stage_level, 1)
        },
        "🦂 ": {
            "name": "Scorpion Prince",
            "HP": 9 * stage_level,
            "atk_mod": round(1.3 * stage_level, 1)
        },
        "🐌 ": {
            "name": "Doom-slug",
            "HP": 20 * stage_level,
            "atk_mod": round(0.5 * stage_level, 1)
        },
        "🦟 ": {
            "name": "Mosquito Queen",
            "HP": 4 * stage_level,
            "atk_mod": round(1.6 * stage_level, 1)
        }
    }
    user_input = input(f"\033[93mFight \033[91m\033[1m{enemies[enemy]["name"]}\033[0m"
                       f"\033[93m? Y to confirm.\033[0m > ")
    if user_input.strip().lower() == "y":
        print("\n\033[91m\033[1mYou are in combat!\033[0m\n")
        print(f" {character["class"]["icon"]} " + "\033[91m❤︎\033[0m" * character["HP"] + "\n")
        print(f" {enemy} " + "\033[93m❤︎\033[0m" * enemies[enemy]["HP"] + "\n")
        while enemies[enemy]["HP"] > 0 and character["HP"] > 0:
            time.sleep(1)
            character_damage = 0
            for stat in character["class"]["main_stats"]:
                character_damage += round(character["stats"][stat.lower()] * random.random())
            if character["stats"]["luc"] * 3 + 25 > random.randint(1, 100):
                enemies[enemy]["HP"] -= round(character_damage * 1.5)
                print("\033[94m\033[1mCRITICAL HIT!\033[0m")
                print(f"You attacked {enemies[enemy]["name"]} dealing "
                      f"\033[91m\033[1m{character_damage * 2}\033[0m damage!\n")
                print(f" {enemy} " + "\033[93m❤︎\033[0m" * enemies[enemy]["HP"] + "\n")
            elif character["stats"]["dex"] * 2 + 50 < random.randint(1, 100):
                print("\033[94mYou Missed!\033[0m\n")
            else:
                enemies[enemy]["HP"] -= character_damage
                print(f"You attacked {enemies[enemy]["name"]} dealing "
                      f"\033[91m\033[1m{character_damage}\033[0m damage!\n")
                print(f" {enemy} " + "\033[93m❤︎\033[0m" * enemies[enemy]["HP"] + "\n")
            time.sleep(1)
            if enemies[enemy]["HP"] > 0:
                enemy_damage = (1 + random.random()) * enemies[enemy]["atk_mod"]
                if character["stats"]["dex"] * 2 + 25 > random.randint(1, 100):
                    print("\033[95mYou dodged the enemy's attack!\033[0m\n")
                else:
                    received_damage = max(1, round(enemy_damage - random.random() * character["stats"]["str"]))
                    print(f"{enemies[enemy]["name"]} attacked you dealing "
                          f"\033[91m\033[1m{received_damage}\033[0m damage!\n")
                    character["HP"] -= received_damage
                    print(f" {character["class"]["icon"]} " + "\033[91m❤︎\033[0m" * character["HP"] + "\n")
        if character["HP"] <= 0:
            return False
        else:
            print(f"\033[99mYou defeated {enemies[enemy]["name"]}!")
            return True
    else:
        return False


def death():
    print("You have died..")
    user_input = input("R to restart. > ").lower().strip()
    if user_input == "r":
        game()


def room_cleared(room) -> bool:
    room_is_clear = True
    for row in room:
        for col in row:
            if col in ["🐜 ", "🦇 ", "🦖 ", "🐊 ", "🦄 ", "🐍 ", "🦂 ", "🐌 ", "🦟 "]:
                room_is_clear = False
    return room_is_clear



def game():
    """
    Drive the game.
    """
    if game_intro():
        current_character = select_character()
        stage = stage_counter(0)
        current_stage = next(stage)
        restart_counter = 0
        while True:
            current_character["coordinates"] = 8, 8
            current_map = generate_map(current_stage, current_character)
            clear_screen(1)
            while True:
                display_map(current_map, current_character)
                user_action = validate_action(current_character, get_user_action(), current_map, current_stage)
                clear_screen(1)
                if user_action == "q":
                    print("\n\n\033[97m\tCoward! I mean.. thanks for playing!\033[0m\n\n")
                    return
                elif type(user_action) == tuple:
                    current_character["coordinates"] = user_action
                elif user_action == "clear":
                    current_stage = next(stage)
                    break
                else:
                    print(user_action)


if __name__ == "__main__":
    game()

