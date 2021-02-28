# Course: CS 30
# Period: 1
# Date Created: 21/02/27
# Date Last Modified: 21/02/27
# Name: Jack Anderson
# Description: Making a menu with continuous game play


# Functions for game so far
def print_commands(command_list):
    """Prints available commands"""
    print("Available commands:")
    for command, command_desc in command_list.items():
        print(f"{command} - {command_desc}")


def print_chara_list(chara_list):
    """Prints list of characters and their info"""
    for characters, chara_info in chara_list.items():
        print(f"\n{characters.title()} is {chara_info['description']}.")
        save = f"{chara_info['how_to_save']}"
        print(f"\t{save.title()} to save them")


def print_item_list(item_list):
    """Prints list of items and their info"""
    for item_name, item_info in item_list.items():
        print(f"\nInventory Item: {item_name.title()}")
        print(f"\tDescription: {item_info['description']}")
        print(f"\tOwner: {item_info['owner']}")


def print_loc_list(loc_list):
    """Prints list of locations and their info"""
    for loc_name, loc_info in loc_list.items():
        print(f"\nThe {loc_name.title()} is {loc_info['description']}.")


def print_inv(inv_list):
    if inv_list != []:
        for inv_item in inv_list.items():
            print(f"{inv_item}")
    else:
        print("You don't have anything")


# Character list
chara = {'celine': {
          'description': 'the sister of damien',
          'how_to_save': 'bring her to damien'
        },
        'damien': {
          'description': 'the brother of celine',
          'how_to_save': 'bring celine to him'
        },
        'the hacker': {
          'description': 'a rude hacker who is good with computers',
          'how_to_save': 'give him the dented camera'
        },
        'the business man': {
          'description': 'a well-dressed business man',
          'how_to_save': 'give him the pretty cane'
        },
        'the crying spirit': {
          'description': 'a spirit with permanent tear streaks and a knack ' +
          'for music',
          'how_to_save': 'give him the pretty music box'
        }}


# Item list
inv_items = {'dented camera': {
              'description': 'a dented video camera,' +
              ' looks like it has been through a lot of use',
              'owner': 'the hacker'
            },
            'pretty cane': {
              'description': 'an ornate pretty cane with a claw ' +
              'holding a glass ball on the top',
              'owner': 'the business man'
            },
            'pretty music box': {
              'description': 'a small white box with ' +
              'a red stripe going up each side and' +
              'small metal crank on the one side',
              'owner': 'the crying spirit'
            }}


# Location list
locations = {'security office': {
              'description': 'a dark office with a desk, ' +
              '9 computer monitors sat on the desk in a ' +
              '3x3 stack showing static'
            },
            'empty room': {
              'description': 'an empty room with nothing in it ' +
              'but dust and two doors'
            },
            'library': {
              'description': 'all the bookshelves had been push to the walls' +
              ' to make room for a small pentagram in the middle'
            },
            'music room': {
              'description': 'a room with a couple of chairs and ' +
              'filled with multiple different kinds of instruments'
            },
            'office': {
              'description': 'an office with a nice desk and ' +
              'a couple of bookshelves and filing cabinets'
            },
            'classroom': {
              'description': 'a room with one large desk and ' +
              'multiple smaller desks facing a chalk board and covered in dust'
            },
            'gym': {
              'description': 'a large gym with multiple dust-covered bleachers'
            },
            'cafeteria': {
              'description': 'a broken-down cafeteria with ' +
              'rotting tables and chairs'},
            'science lab': {
              'description': 'an old lab with rotting tables and ' +
              'shelves full of broken empty bottles'
            }}


# List of commands
commands = {'up': 'move up',
            'down': 'move down',
            'right': 'move right',
            'left': 'move left',
            'pick up': 'pick up item',
            'give': 'give item to nearby character',
            'talk': 'talk to nearby character',
            'follow': 'ask nearby character to follow',
            'inventory': 'checks player inventory',
            'quit': 'quit the game'
            }


# Inventory list
player_inv = []


# Main game input loop
message = ''
while message != 'quit':
    message = input('Enter a command (type ? for help): ')
    if message == '?':
        print_commands(commands)
    elif message == 'up':
        print("You go up")
    elif message == 'down':
        print("You go down")
    elif message == 'right':
        print("You go right")
    elif message == 'left':
        print("You go left")
    elif message == 'pick up':
        print("You pick up item")
    elif message == 'give':
        print("You give item to nearby character")
    elif message == 'talk':
        print("You talk to nearby character")
    elif message == 'follow':
        print("You ask nearby character to follow you")
    elif message == 'inventory':
        print_inv(player_inv)
    elif message == 'quit':
        print("Quitting game")
    else:
        print("Invalid Command")
