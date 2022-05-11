class Room:
    def __init__(self, room_name, room_description):
        self.name = room_name
        self.description = room_description
        self.linked_rooms = {}
        self.characters = []
        self.items = []

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def set_character(self, character_name):
        self.characters.append(character_name)

    def remove_character(self, character_name):
        self.characters.remove(character_name)

    def get_characters(self):
        return self.characters

    def describe_characters(self):
        if len(self.characters) == 0:
            print("There is nobody here.")
        else:
            for character in self.characters:
                character.describe()

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def print_description(self):
        print(self.name)
        underline = ""
        for x in range(0, len(self.name)):
            underline += "-"
        print(underline)
        print(self.description)

    def get_directions(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

        #
        # Item stuff
        #

    def set_item(self, thing):
        self.items.append(thing)

    def get_items(self):
        return self.items

    def remove_item(self, thing):
        self.items.remove(thing)

    def describe_items(self):
        if len(self.items) == 0:
            print("There are no items here.")
        else:
            print("Items here are:")
            for item in self.items:
                item.describe()
