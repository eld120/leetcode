# implement check_win() - checks four diff ways to win


def check_vertical_win(board: list[list[int]], last_move: tuple[int]) -> bool:
    """board is 6x7 and last_move is the y,x coord of the last move"""
    last_move_row, last_move_col = last_move
    color = board[last_move_row][last_move_col]
    row = last_move_row
    connect_four = True
    for _ in range(0, 4):
        if row >= len(board) or board[row][last_move_col] != color:
            connect_four = False
            break
        row += 1

    return connect_four


def check_diagonal_win_positive_slope(
    board: list[list[int]], last_move: tuple[int]
) -> bool:
    # count_matches, row, col = last_move
    count_matches = 0
    row, col = last_move
    last_move_color = board[row][col]
    # iterate up/right until diagonal no longer matches or outside of matrix
    # for _ in range(3)
    while row >= 0 and col < len(board[0]) and board[row][col] == last_move_color:
        count_matches += 1
        row -= 1
        col += 1

    row, col = last_move
    row += 1
    col -= 1
    while row < len(board) and col > 0 and board[row][col] == last_move_color:
        count_matches += 1
        row += 1
        col -= 1

    return count_matches >= 4

    # iterate down/left until diagonal no longer matches or outside of matrix
    # given the position and value of our last move, check up + right also check down + left

    # checking diagonal positive slope is current index = (row, col), next = (row + 1, col -1) or (row - 1, col + 1)

    # traverse matrix, ensure up/right or down/left is within matrix ~ if row in range(board) and col in range(board[0])


board_diagonal_win_positive_slope = [
    [None, None, None, None, None, None, 1],
    [None, None, None, None, None, 1, None],
    [None, None, None, None, 1, None, None],
    [None, None, None, 1, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
]

board_diagonal_loss_positive_slope = [
    [None, None, None, None, None, None, 1],
    [None, None, None, None, None, 1, None],
    [None, None, None, None, 0, None, None],
    [None, None, None, 1, None, None, None],
    [None, None, 1, None, None, None, None],
    [None, 1, None, None, None, None, None],
]
board_diagonal_loss_positive_slope_three_in_row = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, 1, None, None, None, None],
    [None, 1, None, None, None, None, None],
    [1, None, None, None, None, None, None],
]


board_vertical_win = [
    [1, None, None, None, None, None, None],
    [1, None, None, None, None, None, None],
    [1, None, None, None, None, None, None],
    [1, None, None, None, None, None, None],
    [0, None, None, None, None, None, None],
    [0, None, None, None, None, None, None],
]


board_vertical_loss_too_few = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [1, None, None, None, None, None, None],
    [1, None, None, None, None, None, None],
    [1, None, None, None, None, None, None],
]

board_vertical_loss_non_contiguous = [
    [None, None, None, None, None, None, None],
    [1, None, None, None, None, None, None],
    [1, None, None, None, None, None, None],
    [0, None, None, None, None, None, None],
    [1, None, None, None, None, None, None],
    [1, None, None, None, None, None, None],
]


def test_vertical_win():
    assert check_vertical_win(board_vertical_win, (0, 0)) == True


def test_vertical_loss_too_few():
    assert check_vertical_win(board_vertical_loss_too_few, (3, 0)) == False


def test_vertical_loss_non_contiguous():
    assert check_vertical_win(board_vertical_loss_non_contiguous, (1, 0)) == False


def test_diagonal_win_positive_slope():
    assert (
        check_diagonal_win_positive_slope(board_diagonal_win_positive_slope, (1, 5))
        == True
    )


def test_diagonal_loss_positive_slope():
    assert (
        check_diagonal_win_positive_slope(board_diagonal_loss_positive_slope, (4, 2))
        == False
    )


def test_diagonal_loss_three_values():
    assert (
        check_diagonal_win_positive_slope(
            board_diagonal_loss_positive_slope_three_in_row, (4, 1)
        )
        == False
    )
