

if __name__ == '__main__':
    with open('sowpods.txt', 'r') as f:
        print([data.strip('\n') for data in f.readlines() if data.strip('\n')[0] == 'Y' and data.strip('\n')[-1] == 'Y'])
        