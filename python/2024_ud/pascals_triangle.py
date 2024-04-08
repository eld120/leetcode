

def generate_pascals_triangle(number_of_rows: int) -> list[list[int]]:
    def calculate(arr):
        #breakpoint()
        if len(arr) == 0:
            return [1]
        else:
            something = [1]
            index = 1
            while index < len(arr):
                something.append(arr[index] + arr[index-1])
                index += 1
            something.append(1)
            return something
    ans = [[1]]
    while number_of_rows-1 > 0:
        
        temp = ans[-1]
        ans.append(calculate(temp))
        number_of_rows -= 1

    return ans

def test_one():
    assert generate_pascals_triangle(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]