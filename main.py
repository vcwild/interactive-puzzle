from character import Enemy
from character import Friend
from random import choice
from room import Room
from item import Item

# Basegame
item_list = ['banana', 'sword', 'melon', 'pillow', 'pistol', 'flip-flops', 'pinky']
backpack = []
life = 3
exp = 0
dead = False
randitem = Item(choice(item_list))
handr = Item(choice(item_list))

# Setting objects and descriptions
kitchen = Room('Kitchen')
kitchen.set_description('A dank and dirty room filled with hungry cockroaches.')
dining_hall = Room('Dining Hall')
dining_hall.set_description('A strange place that smells of piss and tap water.')
ballroom = Room('Ballroom')
ballroom.set_description('A large room with wide windows and wall painting peeling off.')
bedroom = Room('Bedroom')
bedroom.set_description('A closed environment with moldy walls.')
corridor = Room('Corridor')
corridor.set_description('A room that links rooms.')

# Linking rooms
kitchen.link_room(corridor, 'south')
ballroom.link_room(corridor, 'east')
ballroom.link_room(bedroom, 'south')
bedroom.link_room(ballroom, 'north')
corridor.link_room(kitchen, 'north')
corridor.link_room(ballroom, 'west')
corridor.link_room(dining_hall, 'east')
dining_hall.link_room(corridor, 'west')

# Dave the Enemy Skeleton
charpos = [corridor, dining_hall]
dave = Enemy('Dave', 'He is a smelly zombie')
dave.set_conversation('Hello dear friend, \nwanna take a little sip of this fine brandy?')
dave.set_weakness(randitem)
dave.set_item(handr)
choice(charpos).set_character(dave)

# Catrina the Friendly Skeleton
catrina = Friend('Catrina', 'She is a friendly skeleton!?')
catrina.set_conversation('Hello dude, lets go!')
kitchen.set_character(catrina)

# Set default room
current_room = bedroom

# Set item
posit = [ballroom, bedroom]
randitem.set_description(f'Nothing but a large and smelly {randitem.name}')
choice(posit).set_item(randitem)

print('Welcome, fellow traveller\nType [help] for commands\n')
while dead is False:
    current_room.get_details()
    npc = current_room.get_character()
    item = current_room.get_item()
    hand = None
    weakness = None
    if item is not None:
        item.describe()
    if npc is not None:
        hand = npc.get_item()
        npc.describe()
        if isinstance(npc, Enemy):
            weakness = npc.get_weakness()
    command = str(input('>> '))
    # Helping tips
    if command == 'help':
        print(f'Actions available:\n[backpack] [exp] [fight] [hug] [steal] [talk]')
    # Picking item up
    elif command in ['pick up', 'take', 'get']:
        if item is not None:
            backpack.append(item.name)
            print(f'You {command} the {item.name} and put it in your backpack')
            current_room.set_item(None)
        else:
            print('There is no item to be picked up')
    elif command in ['talk', 'greet', 'hello']:
        npc.talk()
    # Hug a friend
    elif command == 'hug':
        if npc is not None:
            if isinstance(npc, Friend) is True:
                npc.hug()
            else:
                print(f"{npc.name} doesn't like hugs")
        else:
            print('There is no one to hug here')
    # Stealing from someone
    elif command == 'steal':
        if npc is not None:
            if isinstance(npc, Enemy) is True and hand is not None:
                npc.steal()
                backpack.append(hand.name)
                npc.set_item(None)
            else:
                print(f'You hurt {npc.name} feelings')
        else:
            print('There is nothing to steal here')
    elif command in ['fight', 'kill', 'kick']:
        if npc is not None:
            if isinstance(npc, Enemy) is True:
                weapon = str(input(f'{npc.name} looks angry at you, choose your weapon:\n>> '))
                if weapon == 'backpack':
                    print('You cannot fight dave with your backpack')
                elif weapon in backpack:
                    if npc.fight(weapon) is True:
                        current_room.set_character(None)
                        print('Congratulations! You won 1 EXP, how pity!\n')
                        exp += 1
                    else:
                        print(f'A mere {weapon} is too weak to beat {npc.name}, too bad!')
                        life -= 1
                        if life == 0:
                            print(f'\033[31mGame over, you are dead!\033[m')
                            dead = True
                            exit()
                else:
                    print(f"You do not have {weapon}\nShowing backpack items:\n{backpack}")
            else:
                print(f"{npc.name} doesn't like fighting, just giving hugs!")
        else:
            print('Who are you fighting with?')
    elif command == 'backpack':
        print(f'Your backpack has: {backpack}')
    elif command == 'exp':
        print(f'You have {exp} experience, how sad!')
    elif command == ['move', 'change', 'bye', 'exit']:
        current_room.get_details()
        command = str(input('>> ')).lower()
    current_room = current_room.move(command)
