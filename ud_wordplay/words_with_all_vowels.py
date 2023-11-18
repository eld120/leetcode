

if __name__ == '__main__':
    with open('sowpods.txt', 'r') as f:
        print([data.strip('\n') for data in f.readlines() if 'A' in data and 'E' in data and 'I' in data and 'O' in data and 'U' in data])
       