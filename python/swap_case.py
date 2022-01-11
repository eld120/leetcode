


def swap_case(s):
    result = ''
    for sub in s:
        if sub.isupper():
            result = result + sub.lower()
        elif sub.islower():
            result = result + sub.upper()
        else:
            result = result + sub
            
    return result



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

