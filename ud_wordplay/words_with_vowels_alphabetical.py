

if __name__ == '__main__':
    with open('sowpods.txt', 'r') as f:
        # print([data.strip('\n') for data in f.readlines()if 'A' in data and 'E' in data and 'I' in data and 'O' in data and 'U' in data])
        # need to identify all words with all vowels
        ordering = {
            'A' : 0,
            'E' : 1,
            'I': 2,
            'O': 3,
            'U': 4,
        }
        for data in f.readlines():
            if 'A' in data and 'E' in data and 'I' in data and 'O' in data and 'U' in data:
                temp = [ordering[val.rstrip('\n')] for val in data if val in 'AEIOU']
                if sorted(temp) == temp:
                    print(data.rstrip('\n'))
                    
                
                    