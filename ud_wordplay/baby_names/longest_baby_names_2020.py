'''
What are the longest baby names in the top 40 baby names for 2020? Make sure you can handle if there’s a tie.
'''
import timeit
def longest_baby_names_2020():
    with open('./baby_names_2020_short.txt', 'r') as file:
        longest_name_length = 0
        for line in file:
            name = line.rstrip('\n')
            if len(name) > longest_name_length:
                longest_name_length = len(name)
                list_of_longest_names = [name]
            elif len(name) == longest_name_length:
                list_of_longest_names.append(name)
        print(list_of_longest_names)

if __name__ == '__main__':
    time_taken = timeit.timeit(longest_baby_names_2020, number=1)
    print(f'time took {time_taken * 1000} milliseconds')