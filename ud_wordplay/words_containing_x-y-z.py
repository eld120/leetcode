

if __name__ == '__main__':
    with open('sowpods.txt', 'r') as f:
        print([data.strip('\n') for data in f.readlines() if 'X' and 'Y' and 'Z' in data])
        
