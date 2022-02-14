

def time_conversion(s):
    
    am_pm = s[-2:]
    if am_pm == 'AM':
        if s[0:2] == '12':
            result = '00' + s[2:8]
        result = s[:8]
    else:
        if s[0:2] == '12':
            result = f'{s[0:8]}'
            
        else:   
            conv = int(s[0:2]) + 12
        
            result = f'{conv}{s[2:8]}' 
        
        
        
    print(result)
    
    
    #print(result)
    
if __name__ == '__main__':
    s = input()
    
    time_conversion(s)
    