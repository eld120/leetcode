
'''
What are all of the words that start with a Q, end with a Z, and are less than or equal to 6 letters long?
'''



if __name__ == '__main__':
    with open('sowpods.txt', 'r') as f:
        
        result = []
        for line in f.readlines():
            l = line.rstrip('\n')
            if 'Q' == l[0] and 'Z' == l[-1] and len(l) <= 6:
                result.append(l)

        print(result)