


if __name__ == '__main__':
    with open('sowpods.txt', 'r') as f:
        arr = []
        length = 0
        #print([val.strip('\n') for val in f.readlines() if target in val])
        for val in f.readlines():
            if 'A' not in val and 'E' not in val and 'I' not in val and 'O' not in val and 'U' not in val:
                if len(val) == length:
                    arr.append(val.rstrip('\n'))
                elif len(val) > length:
                    
                    length = len(val)
                    arr = []
                    arr.append(val.rstrip('\n'))
                    
        print(arr)
        
        
                    
                
                    