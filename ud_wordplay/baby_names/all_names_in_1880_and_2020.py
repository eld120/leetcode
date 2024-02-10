'''
What are all of the names that were top 40 baby names in both 1880 and 2020?
'''

def with_set():
    names_found = ''
    with open('./baby_names_1880_short.txt') as file:
        old_baby_names = {line.rstrip('\n') for line in file}
    with open('./baby_names_2020_short.txt') as file:
        new_baby_names = [line.rstrip('\n') for line in file]
        for name in new_baby_names:
            if name in old_baby_names:
                names_found += name  + " "

        print(names_found)

def with_list():
    names_found = []
    with open('./baby_names_1880_short.txt') as file:
        old_baby_names = [line.rstrip('\n') for line in file]
    with open('./baby_names_2020_short.txt') as file:
        new_baby_names = [line.rstrip('\n') for line in file]
        for name in new_baby_names:
            if name in old_baby_names:
                names_found.append(name)

        print(names_found)


def with_tuples():
    names_found = tuple()
    with open('./baby_names_1880_short.txt') as file:
        old_baby_names = tuple()
        for line in file:
            old_baby_names += (line.rstrip('\n'),)
    with open('./baby_names_2020_short.txt') as file:
        new_baby_names = [line.rstrip('\n') for line in file]
        for name in new_baby_names:
            if name in old_baby_names:
                names_found += (name,) 

        print(names_found)


if __name__ == '__main__':
    

    
    import timeit
    set_time =  timeit.timeit(with_set, number=1)
    print(f'with set took: {set_time * 1000} ms')

    list_time =  timeit.timeit(with_list, number=1)
    print(f'with list took: {list_time * 1000} ms')

    tuple_time =  timeit.timeit(with_tuples, number=1)
    print(f'with tuple took: {tuple_time * 1000} ms')


   