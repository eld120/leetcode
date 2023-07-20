def staricase(n: int):
    counter = 1
    while n > 0:
        print(" " * (n - 1) + "#" * counter)
        counter += 1
        n -= 1


if __name__ == "__main__":
    n = int(input().strip())
