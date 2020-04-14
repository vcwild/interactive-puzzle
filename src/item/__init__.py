class Item:
    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description

    def describe(self):
        print(f'A {self.name} is here:\n{self.description}')


class Sword:
    def __init__(self, title):
        self._name = title
        self._description = None
        self._attack = None
        self._defense = None

    @property
    def description(self):
        return self._description
    @property
    def attack(self):
        return self._attack
    @property
    def defense(self):
        return self._defense
    @property
    def name(self):
        return self.name

    @attack.setter
    def attack(self, value):
        self._attack = value

    @defense.setter
    def defense(self, value):
        self._defense = value

    @description.setter
    def description(self, value):
        self._description = value

    @name.setter
    def name(self, value):
        self._name = value

    def describe(self):
        print(f'Name: {self._name}\nAttack: {self._attack}\nDefense: {self._defense}\nDescription: {self._description}')
