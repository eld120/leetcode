'''
what countries both begin and end with a vowel

'''



if __name__ == '__main__':
    # O(n^2) time complexity as written
    with open('./countries.txt', 'r') as file:
        countries_starting_ending_vowel = []
        for line in file:
            country = line.rstrip('\n')
            if country[0].lower() in 'aeiou' and country[-1].lower() in 'aeiou':
                countries_starting_ending_vowel.append(country)

        print(countries_starting_ending_vowel)