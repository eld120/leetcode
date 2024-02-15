

def words_fit_specific_criteria(file_path):
    '''
    What are all of the words that are at least 8 letters long and use 3 or fewer different letters? For example, “REFERRER” is an answer to this question, because it uses only 3 different letters: R, E, and F.
    '''

    with open(file_path, 'r') as file:
        
        list_of_words_only_three_letters = []
        for line in file:
            word = line.rstrip('\n')
            
            
            if len(word) > 7 and len(set(word)) <= 3:
                list_of_words_only_three_letters.append(word)

    return ' - '.join(list_of_words_only_three_letters)






    

def test_two():
    assert words_fit_specific_criteria('../sowpods_test.txt') == 'REFERRER'


if __name__ == '__main__':
    print(words_fit_specific_criteria('../sowpods.txt'))
   