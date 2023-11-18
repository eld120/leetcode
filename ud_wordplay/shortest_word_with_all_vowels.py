


if __name__ == '__main__':
    with open('sowpods.txt', 'r') as f:
        arr = []
        length = 9999999999999999999999
        #print([val.strip('\n') for val in f.readlines() if target in val])
        for val in f.readlines():
            if 'A' in val and 'E' in val and 'I' in val and 'O' in val and 'U' in val:
                if len(val) == length:
                    arr.append(val.rstrip('\n'))
                elif len(val) < length:
                    
                    length = len(val)
                    arr = []
                    arr.append(val.rstrip('\n'))
                    
        print(arr)
        
        
                    
                
                    