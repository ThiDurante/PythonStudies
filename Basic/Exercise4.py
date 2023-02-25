"""
Create a program that manipulates a shopping list
"""

import os

shopping_list = ['apple', 'banana', 'water']

while True:
    action = input('What do you want to do? \
        Insert, delete or list? ').lower()
    try:
        if action == 'list':
            os.system('cls')
            for i, item in enumerate(shopping_list):
                print(f'{i} {item}')
        elif action == 'delete':
            try:
                index = int(input('Please select index: '))
                if (shopping_list[index]):
                    del (shopping_list[index])
                # else:
                #     raise Exception('')
            except IndexError:
                print('Thats not a valid index')
            except TypeError:
                print('Please insert an integer')
        elif action == 'insert':
            item_to_add = input('What do you want to insert? ').lower()
            try:
                if (not item_to_add.isalpha()):
                    raise Exception('')
                shopping_list.append(item_to_add)
            except:
                print('Item must only contain alphabetical characters')
        else:
            raise Exception('')
    except:
        print('Please type a valid option')
