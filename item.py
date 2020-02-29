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
