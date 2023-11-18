

if __name__ == '__main__':
    with open('sowpods.txt', 'r') as f:
        print([data.strip('\n') for data in f.readlines() if 'A' not in data and 'E' not in data and 'I' not in data and 'O' not in data and 'U' not in data and 'Y' not in data])
       