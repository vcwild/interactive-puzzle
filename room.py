from time import sleep


def bars(txt):
    text = '\nMoving to...'
    for i in text:
        print(i, end='')
        sleep(0.07)
    print()
    print(f'{"~" * len(txt)}')
    print(txt)
    print(f'{"~" * len(txt)}')


class Room:
    def __init__(self, room_name=None):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.charitem = None

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def set_item(self, item_name):
        self.item = item_name

    def get_item(self):
        return self.item

    def describe(self):
        print(f'\033[32m{self.description}\033[m')

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        # To show code:
        # print(self.name + " linked rooms :" + repr(self.linked_rooms))

    def get_details(self):
        bars(self.name)
        self.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f'\033[33mThe {room.get_name()} is {direction}\033[m')

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            return self

    def set_character(self, value):
        self.character = value

    def get_character(self):
        return self.character
