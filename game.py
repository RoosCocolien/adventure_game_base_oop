# Define a class for Rooms
class Room:
    def __init__(self, name, description, x=0, y=0):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.x = x
        self.y = y

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
    def __init__(self, name, current_room, rooms):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        self.rooms = rooms
        self.visited_rooms = {current_room}

    def move(self, direction):
        new_x, new_y = self.current_room.x, self.current_room.y
        if direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1
        elif direction == "up":
            new_y -= 1
        elif direction == "down":
            new_y += 1
        else:
            print("Invalid direction.")
            return

        # Find room at the new coordinates
        new_room = None # Initialize new_room to None
        # Loop through all rooms in self.rooms
        for room in self.rooms:
            # Check if the current room's coordinates match the target coordinates
            if room.x == new_x and room.y == new_y:
                new_room = room
                break

        if new_room:
            self.current_room = new_room
            self.visited_rooms.add(new_room)
            print(f"You are now in the {new_room.name}.")
        else:
            print(f"You can't go that way")

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

    def show_map(self):
        self.display_map()

    def display_map(self):
        # Determine the bounds of the map
        # Only the discovered rooms will be shown
        min_x = min(room.x for room in self.visited_rooms)
        max_x = max(room.x for room in self.visited_rooms)
        min_y = min(room.y for room in self.visited_rooms)
        max_y = max(room.y for room in self.visited_rooms)

        # Create the map grid
        # Added spaces to determinate the length of the cell
        map_grid = [["      " for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

        # Place rooms in the grid
        for room in self.visited_rooms:
            if room.items:
                map_grid[room.y - min_y][room.x - min_x] = f"[{room.name[:3].upper()}.]"
            else:
                map_grid[room.y - min_y][room.x - min_x] = f"[{room.name[:3].upper()} ]"

        # Display the map
        print("\nMap:")
        for row in map_grid:
            print("".join(row))
        print(f"\nYou are currently in the {self.current_room.name}")


# Game Setup
def create_game(name):
    # Create rooms
    kitchen = Room("Kitchen", "A dank and dirty room buzzing with flies.", x=0, y=0)
    ballroom = Room("Ballroom", "A large room with shiny wooden floors; it looks like a nice place to dance.", x=-1, y=0)
    dining_hall = Room("Dining Hall", "A vast room with a long table where a feast could be held.", x=-1, y=1)
    library = Room("Library", "A quiet place filled with books", x=0, y=-1)
    garden = Room("Garden", "A lush garden full of flowers", x=1, y=0)

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
    MOVE = 1
    PICK_UP = 2
    INVENTORY = 3
    PRINT_MAP = 4
    QUIT = 5

    while True:
        print(f"\n\n{user.name}, you are in the {user.current_room}")
        command = int(input("Choose an option:"
                            "\n1: move\n2: pick up"
                            "\n3: inventory\n4: display map"
                            "\n5: quit\n\nOption: "))

        if command == MOVE:
            direction = input("Provide direction (left|right|up|down): ")
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
        elif command == PRINT_MAP:
            user.display_map()
        elif command == QUIT:
            print("Thanks for playing!")
            break
        else:
            print("Invalid command.")


# Run the game
if __name__ == "__main__":
    name = input("What is your name?: ")
    player = create_game(name)
    play_game(player)
