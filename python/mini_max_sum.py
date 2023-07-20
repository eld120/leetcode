def mini_max_sum(arr):
    arr.sort()
    arr2 = arr[1:]
    arr3 = arr[:4]
    print(f"{sum(arr3)} {sum(arr2)}")


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    mini_max_sum(arr)
