import time

import random


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
    total_stats = random.randint(25, 35)
    while total_stats > 0:
        random_stats[random.choice(stats_list)] += 1
        total_stats -= 1
    random_class = random.choice(list(classes.keys()))
    random_hp = random.randint(10, 20)
    character = {
        "stats": random_stats,
        "class": classes[random_class],
        "HP": random_hp,
        "roll": 10,
        "coordinates": (8, 8)
    }
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
    if level == 0:
        wall = "🔲 "
    else:
        wall = random.choice(["🟨 ", "🟧 ", "🔳 ", "🔲 ", "⬜️ ", "🟦 "])
    empty = ".  "
    door = "🚪 "
    lock = "🔒 "
    room_default = [
        [wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall],
        [wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty,
         empty, wall],
        [wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty,
         empty, wall],
        [wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty,
         empty, wall],
        [wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty,
         empty, wall],
        [wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty,
         empty, wall],
        [wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty,
         empty, wall],
        [wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty,
         empty, wall],
        [wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty,
         empty, wall],
        [wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall]]
    room = room_default.copy()
    if level == 0:
        room[0][8] = "🚪 "
        room[4][4] = "\033[1m\033[33mW  \033[0m"
        room[5][4] = "\033[1m\033[33mS  \033[0m"
        room[5][3] = "\033[1m\033[33mA  \033[0m"
        room[5][5] = "\033[1m\033[33mD  \033[0m"
        room[3][4] = "⬆️ "
        room[6][4] = "⬇️ "
        room[5][2] = "⬅️ "
        room[5][6] = "➡️ "
        room[4][11] = "\033[1m\033[33mE  \033[0m"
        room[4][12] = "INT"
        room[4][13] = "ERA"
        room[4][14] = "CT "
        room[5][11] = "\033[1m\033[33mR  \033[0m"
        room[5][12] = "RES"
        room[5][13] = "TAR"
        room[5][14] = "T  "
        room[6][11] = "\033[1m\033[33mQ  \033[0m"
        room[6][12] = "  Q"
        room[6][13] = "UIT"
        room[0][8] = door
    return room


def display_map(room, character):
    room[character["coordinates"][0]][character["coordinates"][1]] = character["class"]["icon"]
    map_print = ""
    for row in room:
        map_print += ("".join(row))
        map_print += "\n"
    map_print += f"""               ℹ️ \033[95m\033[1mCHARACTER INFO\033[0m ℹ️
                       STR \033[32m{character["stats"]["str"]}\033[0m DEX \033[32m{character["stats"]["dex"]}\033[0m
                       INT \033[32m{character["stats"]["int"]}\033[0m LUC \033[32m{character["stats"]["luc"]}\033[0m
                         HP \033[32m{character["HP"]}\033[0m"""
    print(map_print)


def game():
    """
    Drive the game.
    """
    if game_intro():
        current_character = select_character()
        current_map = generate_map(0, current_character)
        display_map(current_map, current_character)


if __name__ == "__main__":
    game()

