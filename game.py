# Define a class for Rooms
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def set_exit(self, direction, room):
        self.exits[direction] = room

    def get_exit(self, direction):
        return self.exits.get(direction, None)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def __str__(self):
        return f"{self.name}\n\n{self.description}\n"


# Defined a class for Items
# Expand items with superpower actions
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name


# Define a class for the Player
class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.inventory = []

    def move(self, direction):
        next_room = self.current_room.get_exit(direction)
        if next_room:
            self.current_room = next_room
            print(f"You moved to the {self.current_room.name}.")
        else:
            print("You can't go that way!")

    def pick_up(self, chosen_item_name):
        for item in self.current_room.items:
            if item.name == chosen_item_name:
                self.inventory.append(item)
                self.current_room.remove_item(item)
                print(f"You picked up the {chosen_item_name}.")
                return
        print(f"There is no {chosen_item_name} here.")

    def show_inventory(self):
        if self.inventory:
            print("You are carrying:")
            for item in self.inventory:
                print(f"- {item.name}")
        else:
            print("Your inventory is empty.")


# Game Setup
def create_game():
    # Create rooms
    kitchen = Room("Kitchen", "A dank and dirty room buzzing with flies.")
    ballroom = Room("Ballroom", "A large room with shiny wooden floors; it looks like a nice place to dance.")
    dining_hall = Room("Dining Hall", "A vast room with a long table where a feast could be held.")

    # Link rooms together
    kitchen.set_exit("south", ballroom)
    ballroom.set_exit("north", kitchen)
    ballroom.set_exit("west", dining_hall)
    dining_hall.set_exit("east", ballroom)

    # Create items
    sword = Item("Sword", "A sharp-looking sword.")
    shield = Item("Shield", "A sturdy wooden shield.")

    # Place items in rooms
    kitchen.add_item(sword)
    ballroom.add_item(shield)

    # Create a player and start the game in the kitchen
    player_in_the_kitchen = Player(kitchen)
    return player_in_the_kitchen


# Main game loop
def play_game(user):
    MOVE = 1
    PICK_UP = 2
    INVENTORY = 3
    QUIT = 4

    while True:
        print(f"You are in {user.current_room}")
        command = int(input("Choose an option:\n1: move\n2: pick up\n3: inventory\n4: quit\nOption: "))

        if command == MOVE:
            direction = input("Provide direction (north|south|east|west): ")
            user.move(direction)
        elif command == PICK_UP:
            items = user.current_room.get_items()
            if len(items):
                print("The following items are available: ")
                print("0. exit")
                for item in items:
                    print(f"1. {item.name}")
                chosen_item = int(input("Which item would you like to pick up: "))
                if chosen_item != 0:
                    user.pick_up(items[chosen_item - 1].name)
                else:
                    continue
            else:
                print("There are no items available")
        elif command == INVENTORY:
            user.show_inventory()
        elif command == QUIT:
            print("Thanks for playing!")
            break
        else:
            print("Invalid command.")


# Run the game
if __name__ == "__main__":
    player = create_game()
    play_game(player)
