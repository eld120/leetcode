

def main():
    
    # n = int(input())
    arr = map(int, "2564567")
    
    lst = [max(arr), -100]
    for num in arr:
        if num == lst[0]:
            continue
        elif num > lst[1]:
            lst[1] = num
            
    if lst[1] == -100:
        print(lst[0])
    else:
        print(lst[1])



if __name__ == "__main__":
    main()
    
    