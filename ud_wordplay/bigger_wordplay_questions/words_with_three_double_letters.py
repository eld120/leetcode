


def find_lotsa_double_letters():
    '''
    What are all of the words that have at least 3 different double letters? For example, “BOOKKEEPER” is an answer to this question because it has a double-O, a double-K, and a double-E.
    '''
    with open('../sowpods.txt', 'r') as file:
        
        all_triple_double_letter_words = ''
        for line in file:
            word = line.rstrip('\n')
            pass_triple_double_letter_test = [False, 0]
            double_letter_tracker = dict()
            for letter in word:
                if letter in double_letter_tracker.keys():
                    double_letter_tracker[letter] += letter

                else:
                    double_letter_tracker[letter] = letter
            for key in double_letter_tracker:
                if len(double_letter_tracker[key]) > 1:
                    pass_triple_double_letter_test[1] += 1
                    if pass_triple_double_letter_test[1] == 3:
                        all_triple_double_letter_words += f'{word},'
        print(all_triple_double_letter_words)


if __name__ == '__main__':
    find_lotsa_double_letters()