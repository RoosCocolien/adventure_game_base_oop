from game.room import Room
from game.item import Item
from game.player import Player
from enum import Enum


class Option(Enum):
    MOVE = 1
    PICK_UP = 2
    INVENTORY = 3
    PRINT_MAP = 4
    QUIT = 5


# Game Setup
def setup_game(name):
    # Create rooms
    kitchen = Room("Kitchen",
                   "A dark and dirty room buzzing with flies.",
                   x=0, y=0)
    ballroom = Room("Ballroom",
                    "A large room with shiny wooden floors; it looks like a nice place to dance.",
                    x=-1, y=0)
    dining_hall = Room("Dining Hall",
                       "A vast room with a long table where a feast could be held.",
                       x=-1, y=1)
    library = Room("Library",
                   "A quiet place filled with books",
                   x=0, y=-1)
    garden = Room("Garden",
                  "A lush garden full of flowers",
                  x=1, y=0)

    # List of all rooms
    rooms = [kitchen, ballroom, dining_hall, library, garden]

    # Create items
    sword = Item("Sword", "A sharp-looking sword.")
    shield = Item("Shield", "A sturdy wooden shield.")

    # Place items in rooms
    kitchen.add_item(sword)
    ballroom.add_item(shield)

    # Create a player and start the game in the kitchen
    player_in_the_kitchen = Player(name, kitchen, rooms)

    return player_in_the_kitchen


# Main game loop
def play_game(user):
    print(f"\n\n{user.name}, you are in the {user.current_room}")
    while True:
        try:
            command = int(input("Choose an option:\n"
                            "1: move\n"
                            "2: pick up\n"
                            "3: inventory\n"
                            "4: display map of discovered rooms\n"
                            "5: quit\n"
                            "\nOption: "))
        except ValueError:
            print('Please enter a number')
            continue

        if command == Option.MOVE.value:
            direction = input("Provide direction (left|right|up|down): ")
            user.move(direction)
        elif command == Option.PICK_UP.value:
            items = user.current_room.get_items()
            if len(items) > 0:
                print("The following items are available: ")
                print("0. I don't want to pick anything up")
                for item in items:
                    print(f"1. {item.name}")
                chosen_item = int(input("Which item would you like to pick up: "))
                if  0 < chosen_item <= len(items):
                    user.pick_up(items[chosen_item - 1].name)
                else:
                    continue
            else:
                print("There are no items available")
        elif command == Option.INVENTORY.value:
            user.show_inventory()
        elif command == Option.PRINT_MAP.value:
            user.display_map()
        elif command == Option.QUIT.value:
            print("Thanks for playing!")
            break
        else:
            print("Invalid command.")
