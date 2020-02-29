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
