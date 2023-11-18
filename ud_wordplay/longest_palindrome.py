


pal_length = 0
arr = []
if __name__ == '__main__':
    with open('./sowpods.txt', 'r') as f:
        for val in f.readlines():
            if list(val.strip('\n')) == list(reversed(val.strip('\n'))) and len(val) == pal_length:
                arr.append(val.strip('\n'))
            elif list(val.strip('\n')) == list(reversed(val.strip('\n'))) and len(val) > pal_length:
                pal_length = len(val)
                arr = []
                arr.append(val.strip('\n'))

        print(arr)