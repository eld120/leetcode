import re


if __name__ == "__main__":
    N = int(input("enter:"))
    
    count = 0
    lst = []
    
    while count < N:
        count += 1
        ans = input()
        
        if 'insert' in ans:
            try:
                end = re.search(r'(?<=insert\s\d\s).*', ans)
                middle = re.search(r'(?<=insert\s)\d+', ans)
                lst.insert(int(middle.group(0)), int(end.group(0)))  
                
            except AttributeError:
                print(end)
                print('insert not found')
                continue
              
        elif 'print' in ans:
            print(lst)
        elif 'remove' in ans:
            try:
                end = re.search(r'(?<=remove\s).*', ans)
                lst.remove(int(end.group(0)))
            except AttributeError:
                print('remove not performed')
                continue
            
        elif 'append' in ans:
            try:
                end = re.search(r'(?<=append\s).*', ans)
                lst.append(int(end.group(0)))
            except AttributeError:
                print('append not performed')
                continue
        elif 'sort' in ans:
            lst.sort()
        elif 'pop' in ans:
            try:
                lst.pop()
            except:
                print('pop not peformed')
        elif 'reverse' in ans:
            lst.reverse()
            
        
    
        
        
       
