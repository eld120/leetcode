

def main():
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    answer_list = [max(arr), -100]
    
    for num in arr:
        if num == answer_list[0]:
            continue
        elif num > answer_list[1]:
            answer_list[1] = num
    
    if answer_list[1] == -100:
        print(answer_list[0])
    else:
        print(answer_list[1])
            





if __name__ == "__main__":
    main()
    
    