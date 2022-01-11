def count_substring(string, sub_string):
    length = len(string)
    sub_length = len(sub_string)
    count = 0
    for i in range(0, length +1):
        try:
            if sub_string in string[0+i:sub_length+i]:
                count += 1
        except IndexError:
            break
    return count




if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)