'''
[ ] There is at least one country name that contains another country name. Find all of these cases.
'''

if __name__ == '__main__':

    with open('./countries.txt', 'r') as file:
        countries_containing_country_names = []
        countries = [line.rstrip('\n') for line in file]
        counter = 0
        for country in countries:
            for inner_country in countries:
                if inner_country != country and inner_country in country:
                    countries_containing_country_names.append(country)
        print(countries_containing_country_names)