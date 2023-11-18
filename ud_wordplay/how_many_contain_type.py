
target = 'TYPE'

if __name__ == '__main__':
    with open('sowpods.txt', 'r') as f:
        count = 0
        for val in f.readlines():
            if target in val:
                count += 1
                
        print(count)
        
        
                    
                
                    