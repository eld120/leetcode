
target = 'GHTLY'

if __name__ == '__main__':
    with open('sowpods.txt', 'r') as f:
        #arr = []
        # print([val.strip('\n') for val in f.readlines() if target in val])
        # for val in f.readlines():
        #     if target in val:
        #         arr.append(val.rstrip('\n'))
                
        # print(arr)

        # the above code is flaky as the target could be anywhere in the data

        print([val.strip('\n') for val in f.readlines() if target in val.strip('\n')[-5:]])
        
        
                    
                
                    