# given a year determine whether it's a leap year(boolean)
def is_divisible_by_4(year: int) -> bool:
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 100):
        return True
    return False


def is_leap(year) -> bool:
    leap: bool = False
    return is_divisible_by_4(year)


try:
    year = int(input())
except ValueError:
    print("Your input must be an int\n")
    year = int(input())
print(is_leap(year))
