'''
what country names are > 50% vowels?
'''



if __name__ == '__main__':
    with open('./countries.txt', 'r') as file:
        gt_50_percent_vowels = []
        for line in file:
            country = line.rstrip('\n')
            vowel_count = 0
            for letter in country:
                if letter.lower() in 'aeiou':
                    vowel_count += 1
            if vowel_count / len(country) > .5:
                gt_50_percent_vowels.append(country)


    print(gt_50_percent_vowels)