






def birthday_cake_candles(candles):
    temp_highest = 0
    count_result = 0
    for thing in candles:
        if thing > temp_highest:
            temp_highest = thing
            count_result = 1
            
        elif thing == temp_highest:
            count_result += 1
    print(count_result)


if __name__ == '__main__':
    candles_count = int(input().strip())
    
    candles = list(map(int, input().rstrip().split()))
    
    result = birthday_cake_candles(candles)
    
    