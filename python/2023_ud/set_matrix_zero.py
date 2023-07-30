from typing import List

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.


case_one = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]  # -> [[1,0,1],[0,0,0],[1,0,1]]
case_two = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5],
]  # -> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

case_one_test = ((1, 1),)
case_two_test = ((0, 0), (0, 3))


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    zerod_indices = tuple()
    for list_index, list in enumerate(matrix):
        # determine where zero is found in list
        for inner_index, inner_value in enumerate(list):
            if inner_value == 0:
                # save those indices in a tuple
                zerod_indices += ((list_index, inner_index),)

    for row, col in zerod_indices:
        set_col_to_nil(matrix, col)
        set_row_to_nil(matrix, row)
    # return matrix


def set_col_to_nil(matrix, col: int):
    # set columns values to zero by iterating through tuples
    counter = 0
    while counter < len(matrix):
        matrix[counter][col] = 0
        counter += 1
    return matrix


def set_row_to_nil(matrix, row):
    # set row values to zero
    index = 0
    while index < len(matrix[row]):
        matrix[row][index] = 0
        index += 1
    return matrix


# def test_rows_case_one():
#     _case_one = [[1,1,1],[1,0,1],[1,1,1]]
#     assert set_row_to_nil(_case_one, case_one_test[0][1]) == [[1,1,1],[0,0,0],[1,1,1]]

# def test_rows_case_two():
#     _case_two = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#     assert set_row_to_nil(_case_two, case_two_test[0][1]) == [[0,0,0,0],[3,4,5,2],[1,3,1,5]]

# def test_col_case_one():
#     _case_one = [[1,1,1],[1,0,1],[1,1,1]]
#     assert set_col_to_nil(_case_one, case_one_test[0][1]) == [[1,0,1],[1,0,1],[1,0,1]]

# def test_col_case_two():
#     _case_two = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#     assert set_col_to_nil(_case_two, case_two_test[0][1]) == [[0,1,2,0],[0,4,5,2],[0,3,1,5]]

# def test_col_case_three():
#     _case_two = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#     assert set_col_to_nil(_case_two, case_two_test[1][1]) == [[0,1,2,0],[3,4,5,0],[1,3,1,0]]


# if __name__ == '__main__':
#     set_row_to_nil([[0,1,2,0],[3,4,5,2],[1,3,1,5]], 0)

# def test_matrix_one():
#     assert setZeroes(case_one) == [[1,0,1],[0,0,0],[1,0,1]]

# def test_matrix_twod():
#     assert setZeroes(case_two) == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
