import re


def main():
    N = int(input())

    count = 0
    lst = []

    while count < N:
        count += 1
        ans = input()
        if "insert" in ans:
            end = re.search(r"(?<=insert\s\d\s).+", ans)
            middle = re.search(r"(?<=insert\s)\d{1,2}", ans)
            lst.insert(int(middle.group(0)), int(end.group(0)))
        elif "print" in ans:
            print(lst)
        elif "remove" in ans:
            end = re.search(r"(?<=remove\s).+", ans)
            lst.remove(int(end.group(0)))
        elif "append" in ans:
            end = re.search(r"(?<=append\s).+", ans)
            lst.append(int(end.group(0)))
        elif "sort" in ans:
            lst.sort()
        elif "pop" in ans:
            lst.pop()
        elif "reverse" in ans:
            lst.reverse()


if __name__ == "__main__":
    main()
