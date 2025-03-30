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
        room[4][11] = "\033[1m\033[33mR  \033[0m"
        room[4][12] = "RES"
        room[4][13] = "TAR"
        room[4][14] = "T  "
        room[5][11] = "\033[1m\033[33mQ  \033[0m"
        room[5][12] = "  Q"
        room[5][13] = "UIT"
        room[5][14] = "   "
        room[0][8] = door
        room[9][8] = "\033[91m⬆ \033[0m"
    return room


def display_map(room, character):
    temp_room = copy.deepcopy(room)
    row, col = character["coordinates"]
    temp_room[row][col] = character["class"]["icon"]
    map_print = ""
    for row in temp_room:
        map_print += "".join(row) + "\n"
    current_hp = "▊" * character["HP"]
    map_print += f"""               ℹ️ \033[95m\033[1mCHARACTER INFO\033[0m ℹ️
               HP \033[32m{current_hp}\033[0m
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
            user_confirm = input("\033[91mAre you sure you want to quit? \"Y\" to confirm.\033[0m\n > ")
            user_confirm = user_confirm.strip().lower()
            if user_confirm == "y":
                return "q"
            else:
                continue
        elif user_input == "r" or user_input == "restart" or user_input == "re":
            user_confirm = input("\033[91mAre you sure you want to restart? \"Y\" to confirm.\033[0m\n > ")
            user_confirm = user_confirm.strip().lower()
            if user_confirm == "y":
                return "r"
            else:
                continue
        else:
            print("Invalid input.")


def validate_action(character, action, room):
    if action == "r":
        return "r"
    elif action == "q":
        return "q"
    character_new_location = (character["coordinates"][0] + action[0], character["coordinates"][1] + action[1])
    if room[character_new_location[0]][character_new_location[1]] == ".  ":
        return character_new_location
    else:
        if room[character_new_location[0]][character_new_location[1]] in ["🟨 ", "🟧 ", "🔳 ", "🔲 ", "⬜️ ", "🟦 "]:
            return "\033[91A wall is blocking your way!\033[0m"
        else:
            # return f"{room[character_new_location[0]][character_new_location[1]]} is blocking your way!"
            return "\033[91You cannot move that way!\033[0m"


def room_cleared() -> bool:
    pass


def game():
    """
    Drive the game.
    """
    if game_intro():
        stage = stage_counter(0)
        current_stage = next(stage)
        current_character = select_character()
        current_map = generate_map(current_stage, current_character)
        while True:
            display_map(current_map, current_character)
            user_action = validate_action(current_character, get_user_action(), current_map)
            if user_action == "r":
                game()
            elif user_action == "q":
                return
            elif type(user_action) == tuple:
                current_character["coordinates"] = user_action
            else:
                print(user_action)


if __name__ == "__main__":
    game()

