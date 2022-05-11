from rpg import Room, Item, Container, Enemy, Friend

# from item import Item
# from item import Container
# from character import Character
# from character import Enemy
# from character import Friend

# Valid Commands
movements = ["north", "n", "south", "s", "east", "e", "west", "w"]
commands = ["exit", "talk", "give", "hug", "bribe", "inv", "take", "drop", "what", "look", "who"]

alive = True

# Create rooms
kitchen = Room("Kitchen", "A dank and dirty room buzzing with flies.")
dining_hall = Room("Dining Hall", "An ornate, wood-panelled room with a large table full of rotting food.")
ballroom = Room("Ballroom", "The ballroom has seen better days, all the balls are flat.")
store_room = Room("Store Room", "It's a tiny cupboard with mops and the like.")

# Link rooms
kitchen.link_room(dining_hall, "south")
kitchen.link_room(store_room, "east")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
store_room.link_room(kitchen, "west")

# Create items
knife = Item("Knife", "Although somewhat blunt the knife will still chop a bananna.")
leg = Item("Leg", "Somebody's old prosthetic leg, a left probably.")
pizza = Item("Pizza", "A freshly delivered Margarita pizza, with no egg on it.")
wires = Item("Wires", "A tangled mess of wires.")
backpack = Container("Backpack", "A trendy bag with straps, you can wear.")

# Create Characters
dave = Enemy("Dave", "He smells of dough and cheese.")
dave.set_weakness("pizza")
dave.set_thanks_text("Dave takes the pizza, says 'Can I have it with an egg on it next time?' and leaves.")
dave.set_corrupt(True)

gary = Enemy("Gary", "The ghost of an IT engineer.")
gary.set_weakness("wires")
gary.set_thanks_text("Gary likes wires, he goes to his office to tidy them.")
gary.set_corrupt(False)

rev = Friend("The Rev", "Your chatty best mate.")
rev.set_following = False
rev.set_chit_chat(["Dave is a nightmare to work for.",
                   "I can see right through that Gary fella.",
                   "What is the point of cucumber?",
                   "I could've been a contender.",
                   "I could've been a someone.",
                   "Dave smells of cheese.",
                   "Dave likes pizza.",
                   "Why are we here?",
                   "What time is dinner",
                   "Get rid of these other idiots, I need peace and quiet to write me songs.",
                   "Caught up in the rat race, and feeling like a no one?",
                   "Could've been me in the papers, with the money and the girls.",
                   "I could've been the heavyweight champion of the world",
                   "I'm making you aware of the state of things.",
                   "I can sometimes give you a hint",
                   "A little introduction to the state of things?",
                   "I'm aching to sing about the state of things.",
                   "Gary likes wires",
                   "Because we're all run by fools that's the state of things!"
                   ])

keep_looping = True

print("""
Welcome to my crazy text based adventure game inspired by the
amazing FutureLearn "Object-oriented Programming in Python" course.

Things I've added/changed:
    - pacification of the 'fight' method
    - a roaming character "The Rev"
    - random talk responses from "The Rev"
    - three attempts to please an enemy class
    - changed the backpack into an instance of an item class
    - the backpack is an item and can contain other items, freaky
    - what, who, look, inv, drop commands
    - "all" logic on take and drop commands
    - basic "verb & noun" two word input
    - plus other things I've forgotten.

The object of the game is to please the "enemies" so The Rev can get
back to wandering round and writing more songs.


""")

while Enemy.count > 0 and keep_looping:

    alive = True

    # Locate Characters
    dining_hall.set_character(dave)
    store_room.set_character(gary)
    ballroom.set_character(rev)

    # Locate items
    store_room.set_item(pizza)
    ballroom.set_item(wires)
    dining_hall.set_item(knife)
    store_room.set_item(leg)

    current_room = kitchen

    current_room.print_description()
    print()
    current_room.get_directions()
    print()
    current_room.describe_items()
    print()
    current_room.describe_characters()
    print()
    backpack.contents.clear()
    backpack.look_in()
    print()

    inhabitants = current_room.get_characters()

    while alive and Enemy.count > 0:

        if rev.following:
            rev.talk()

        raw_input = input("> ")
        if len(raw_input) == 0:
            continue
        raw_input = raw_input.lower()
        raw_input = raw_input.split()
        command = raw_input[0]
        if len(raw_input) == 0:
            continue
        if len(raw_input) > 1:
            input_item = raw_input[1]
        else:
            input_item = None

        if command in commands or command in movements:

            if command == "exit":
                confirm = input('Are you sure you want to exit? ')
                if confirm.lower() in ['y', 'yes']:
                    print('Thanks for playing, come again.')
                    keep_looping = False
                    break

            elif command in movements:
                previous_room = current_room
                current_room = current_room.move(command)

                if current_room != previous_room:
                    print("")
                    current_room.print_description()
                    print()
                    current_room.get_directions()
                    print()

                    if rev.following:
                        current_room.set_character(rev)
                        previous_room.remove_character(rev)

                    inhabitants = current_room.get_characters()

                    current_room.describe_characters()
                    print()
                    current_room.describe_items()
                    print()

            elif command == "talk":
                if inhabitants:
                    for inhabitant in inhabitants:
                        inhabitant.talk()
                else:
                    print("Why are you talking to yourself?")

            elif command == "hug":
                if inhabitants:
                    for inhabitant in inhabitants:
                        inhabitant.hug()
                else:
                    print("You wrap your arms around yourself and have a warm fuzzy feeling.")

            elif command == "bribe":
                if inhabitants:
                    for inhabitant in inhabitants:
                        inhabitant.bribe()
                else:
                    print("You slip yourself a tenner, and give yourself no clues in return.")

            elif command == "inv":

                backpack.look_in()

            elif command == "what":

                current_room.describe_items()

            elif command == "look":

                current_room.print_description()

            elif command == "who":

                current_room.describe_characters()

            elif command == "take":

                if len(current_room.items) == 0:
                    print("There is nothing here you can take.")
                else:
                    if input_item is None:
                        print("Take what?")
                        take_item = input()
                        take_item = take_item.lower()
                    else:
                        take_item = input_item

                    taken = False
                    remove_item = []

                    for item in current_room.items:
                        if take_item == item.name.lower() or take_item == 'all':
                            print("You put the " + item.name + " in your backpack.")
                            backpack.put_in(item)
                            remove_item.append(item)
                            taken = True

                    for item in remove_item:
                        current_room.remove_item(item)

                    if not taken:
                        print("There is no " + take_item + " here.")

            elif command == "drop":

                if len(backpack.contents) == 0:
                    print("There is nothing in your backpack.")
                else:
                    if input_item is None:
                        print("Drop what?")
                        drop_item = input()
                        drop_item = drop_item.lower()
                    else:
                        drop_item = input_item

                    dropped = False
                    remove_item = []

                    for item in backpack.contents:
                        if drop_item == item.name.lower() or drop_item == 'all':
                            print("You take the " + item.name + " out of your backpack and drop it on the floor.")
                            remove_item.append(item)
                            current_room.set_item(item)
                            dropped = True

                    for item in remove_item:
                        backpack.take_out(item)

                    if not dropped:
                        print("You don't have the " + drop_item + " with you.")

            elif command == "give":

                if len(backpack.contents) == 0:
                    print("There is nothing in your backpack to give.")
                else:
                    if len(inhabitants) == 0:
                        print("You give yourself a punch in the face!")
                    else:
                        if input_item is None:
                            print("What will you give?")
                            give_item = input()
                            give_item = give_item.lower()
                        else:
                            give_item = input_item

                        if len(inhabitants) > 1:
                            print("Who will you give it to?")
                            who_to = input()
                            who_to = who_to.lower()
                        else:
                            who_to = inhabitants[0].name.lower()

                        offered = False

                        for item in backpack.contents:
                            if give_item == item.name.lower():
                                offered = True
                                for inhabitant in inhabitants:
                                    if who_to == inhabitant.name.lower():
                                        inhabitant.give(give_item)
                                        if inhabitant.called_cops:
                                            alive = False
                                        elif inhabitant.taken:
                                            current_room.remove_character(inhabitant)
                                            inhabitants = current_room.get_characters()
                                            backpack.take_out(item)

                        if alive and not offered:
                            print("You don't have the " + give_item + ".")

        else:
            print("Valid commands are:")
            print(movements)
            print(commands)

    if not keep_looping:
        break

    if Enemy.count == 0:
        print("Congratulations all the weirdos have left the game.")
        print("You are now stuck here with The Rev for eternity.")
        print('')
        print('')
    else:
        print("We are sorry you have failed.")
        print("In recompense please accept this free play to try again.")
        print('')
        print('')
