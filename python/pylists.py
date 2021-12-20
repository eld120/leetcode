import re


if __name__ == "__main__":
    N = int(input())
    
    count = 0
    lst = []
    
    while count < N:
        ans = input()
        
        if 'insert' in ans:
            end = re.search(r'(?<=insert\s\d)\d+', ans)
            middle = re.search(r'(?<=insert\s)\d+', ans)
            lst.insert(int(middle.group(0)), int(end.group(0)))    
        if 'print' in ans:
            print(lst)
        if 'remove' in ans:
            
            end = re.search(r'(?<=insert\s)\d', ans)
            lst.remove(int(end.group(0)))
        if 'append' in ans:
            end = re.search(r'(?<=insert\s)\d', ans)
            lst.append(int(end.group(0)))
        if 'sort' in ans:
            lst.sort()
        if 'pop' in ans:
            lst.pop()
        if 'reverse' in ans:
            lst.reverse()
            
            
    print(lst)
        
        
       
