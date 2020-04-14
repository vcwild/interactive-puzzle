class Character:
    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.item = None

    # Describe this character
    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

    def typename(self):
        return type(self).__name__

    # Give the character items
    def set_item(self, item_name):
        self.item = item_name

    def get_item(self):
        return self.item


# Starting a subclass of Character
class Enemy(Character):
    # Create an enemy
    def __init__(self, char_name, char_description, item_name=None):
        # Statement to create a subclass based on the superclass
        super().__init__(char_name, char_description)
        self.weakness = None
        self.item = item_name

    def set_weakness(self, value):
        self.weakness = value

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness.name:
            print(f'You crushed {self.name} over with the mighty {combat_item}.')
            return True
        else:
            print(f'{self.name} crushes you, breaking your {combat_item} in half')
            return False

    def steal(self=None):
        print(f'You stole a {self.item.name} from {self.name}')


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None

    def hug(self):
        print(f'{self.name} hugs you back')
