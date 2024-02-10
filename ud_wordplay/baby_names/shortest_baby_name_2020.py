'''
What is the shortest baby name in the top 40 baby names for 2020?
'''

if __name__ == '__main__':
    with open('./baby_names_2020_short.txt', 'r') as file:
        shortest_baby_names = []
        shortest_name_length = 20
        for line in file:
            name = line.rstrip('\n')
            if len(name) < shortest_name_length:
                shortest_name_length = len(name)
                shortest_baby_names = [name]
            elif len(name) == shortest_name_length:
                shortest_baby_names.append(name)
        print(shortest_baby_names)