# print the list of integers from 1 through n as a string without spaces
if __name__ == "__main__":
    n = int(input())
    string = ""
    for num in range(1, n + 1):
        string = string + str(num)

    print(string)
