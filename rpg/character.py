from random import randint


class Character:
    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.corrupt = False
        self.following = False
        self.taken = False
        self.called_cops = False

    def set_following(self, is_following):
        self.following = is_following

    # Describe this character
    def describe(self):
        print(self.name + " is here! " + self.description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_corrupt(self, takes_a_bribe):
        self.corrupt = takes_a_bribe

    # Talk to this character
    def talk(self):
        """Checks to see if the character has any conversation then uses it"""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you.")

    # give something to this character
    def give(self, gift):
        print(self.name + " doesn't want anything from you, other than your friendship.")
        self.taken = False
        self.called_cops = False

    def hug(self, ):
        print(self.name + " gives you a bear hug.")

    def bribe(self):
        if self.corrupt:
            print(self.name + " says, 'Cheers, I'll ensure you get my top service level in future.'")
        else:
            print(self.name + " responds indignantly, 'What kind of person do you think I am?")
            print("Keep your bloody money!'")


class Enemy(Character):
    count = 0

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.thanks_text = "They flounce off."
        self.player_retry = 3
        self.player_retry_text = [None, "one more chance to please me.'", "two more chances to please me.'"]
        Enemy.count += 1

    def set_weakness(self, weakness_name):
        self.weakness = weakness_name

    def set_thanks_text(self, acceptance_speech):
        self.thanks_text = acceptance_speech

    def get_name(self):
        return self.weakness

    # give something to this character
    def give(self, gift):
        if gift == self.weakness:
            print("You give " + self.name + " your " + gift + ".")
            print(self.thanks_text)
            self.taken = True
            self.called_cops = False
            Enemy.count -= 1  # Defeated
            # print(Enemy.count)
        else:
            if self.player_retry > 1:
                self.player_retry -= 1
                print(self.name, "says 'Why would I want that?  I'm going to give you",
                      self.player_retry_text[self.player_retry])
                self.taken = False
            else:
                print(self.name, "doesn't want that.")
                print('')
                print("He thinks that you are unhinged and reports you to the adventure game police.")
                print("They arrive and take you away in straightjacket.")
                print('')
                self.taken = False
                self.called_cops = True

    def hug(self, ):
        print(self.name + " gives you a kick in the shin.")


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.chit_chat = []

    def set_chit_chat(self, vocab):
        self.chit_chat = vocab

    def talk(self):
        """Allows a Friend Character to talk using it's own vocab"""
        random_response_number = randint(1, len(self.chit_chat)) - 1
        print(self.name + " says, '" + self.chit_chat[random_response_number] + "'")
        self.following = True
