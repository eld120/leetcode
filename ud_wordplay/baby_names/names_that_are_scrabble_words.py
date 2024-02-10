'''

[ ] There is at least one baby name from the top 40 baby names for 2020 that, when spelled backwards, is a valid Scrabble word. Find and print all such names.
    [ ] Solve this two ways: first with an array to hold the Scrabble words, and then with a dictionary (or set) to hold the Scrabble words. Use timer functions to measure how long it takes to complete this work under each implementation. Why is the time different?
'''
from timeit import timeit



def scrabble_with_lists():
    with open('../sowpods.txt') as file:
        list_scrabble_words = [line.lower().rstrip('\n') for line in file]

    with open('./baby_names_2020_short.txt') as file:
        list_baby_names = [line.rstrip('\n') for line in file]
        name_index  = 0
        while name_index < len(list_baby_names):
            temp_name = ''
            for letter in reversed(list_baby_names[name_index]):
                temp_name += letter
            list_baby_names[name_index] = temp_name.lower()
            name_index += 1
    scrabble_names_found = []
    for name in list_baby_names:
        if name in list_scrabble_words:
            scrabble_names_found.append(name)
    print(scrabble_names_found)


def scrabble_with_set():
    with open('../sowpods.txt') as file:
        set_scrabble_words = {line.lower().rstrip('\n') for line in file}
    
    with open('./baby_names_2020_short.txt') as file:
        list_baby_names = [line.rstrip('\n') for line in file]
        name_index  = 0
        
        while name_index < len(list_baby_names):
            temp_name = ''
            for letter in reversed(list_baby_names[name_index]):
                temp_name += letter
            list_baby_names[name_index] = temp_name.lower()
            name_index += 1
        
    scrabble_names_found = []
    for name in list_baby_names:
        if name in set_scrabble_words:
            scrabble_names_found.append(name)
    print(scrabble_names_found)


if __name__ == '__main__':
    list_execution_time = timeit(scrabble_with_lists, number=1)
    print(f'list execution time: {list_execution_time * 1000}ms')

    set_execution_time = timeit(scrabble_with_set, number=1)
    print(f'set execution time: {set_execution_time * 1000}ms')
    