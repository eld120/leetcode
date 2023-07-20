# given 3 integers print a list of all possible coordinates
# where the sum of all inegers in increasing order are not equal to n

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print(
        [
            [a, b, c]
            for a in range(0, x + 1)
            for b in range(0, y + 1)
            for c in range(0, z + 1)
            if a + b + c != n
        ]
    )

    # didn't solve but found : [[a,b,c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0,z+1) if a+b+c < n]
