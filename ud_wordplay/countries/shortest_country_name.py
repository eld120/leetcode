'''
what is the shortest country name? Ensure code can handle ties
'''



if __name__ == '__main__':
    with open('./countries.txt', 'r') as file:
        shortest_country_names = []
        shortest_length = 99
        for line in file:
            country = line.rstrip('\n')
            if len(country) < shortest_length:
                # how do we feel about calling len 2x considering it's read from a struct under the hood - I think
                shortest_length = len(country)
                shortest_country_names = []
                shortest_country_names.append(country)
            elif len(country) == shortest_length:
                shortest_country_names.append(country)
        print(shortest_country_names)