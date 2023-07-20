if __name__ == "__main__":
    s = input()
    alphanum = False
    for i in range(0, len(s) + 1):
        if s[0 + i : i + 1].isalnum():
            alphanum = True
            break
    print(alphanum)

    alpha = False
    for i in range(0, len(s) + 1):
        if s[0 + i : i + 1].isalpha():
            alpha = True
            break
    print(alpha)

    digits = False
    for i in range(0, len(s) + 1):
        if s[0 + i : i + 1].isdigit():
            digits = True
            break
    print(digits)

    lowercase = False
    for i in range(0, len(s) + 1):
        if s[0 + i : i + 1].islower():
            lowercase = True
            break
    print(lowercase)

    uppercase = False
    for i in range(0, len(s) + 1):
        if s[0 + i : i + 1].isupper():
            uppercase = True
            break
    print(uppercase)
