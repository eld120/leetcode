

def merge_the_tools(string, k):
    
    for i in range(0,len(string)+1, k):
        sub_string = string[0+i:i+k]
        characters = set([i for i in sub_string])
        result = ''
        for letter in sub_string:
            try:
                if letter in result:
                    continue
                else:
                    result = result + letter
            except IndexError:
                result = result + letter
            
                
        print(result)
    
    
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)