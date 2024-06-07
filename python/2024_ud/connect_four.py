import random, pytest


class ConnectFour:
    """
    Represents the Connect Four game instance
    """

    def __init__(self) -> None:
        # initialized game board with None to represent empty space
        self.game_board: list[list[int]] = [
            [None for inner in range(7)] for outer in range(6)
        ]
        self.red_coin = 0
        self.yellow_coin = 1
        self.player_turn = self.who_goes_first()
        self.last_move: tuple = (None, None)  # attribute to check for a winning move

    def who_goes_first(self) -> int:
        """flips a coin to see who goes first"""
        return random.randint(0, 1)

    def switch_turns(self) -> None:
        """switches player turn during gameplay"""
        self.player_turn = 1 if self.player_turn == 0 else 0

    def drop_coin(self, column: int) -> None:
        """
        facilitates each turn of gameplay

        column: int - the column with which a player may choose to drop their coin

        raises ValueError if the column is full, defined as all values are the integers 0 or 1
        """
        index = len(self.game_board) - 1  # initializes an index to track
        for row in reversed(
            self.game_board
        ):  # iterates through board from the bottom up
            if row[column] is None:
                self.last_move = (index, column)  # records first valid move
                self.game_board[index][column] = (
                    1 if self.player_turn == 1 else 0
                )  # automatically assigns the correct color coin
                self.switch_turns()
                break
            # raises error if the current column is full
            if index == 0 and row[column] is not None:
                raise ValueError("Column is full please choose again")
            index -= 1

    def check_vertical_win(self) -> bool:
        """checks self.game_board to see if the last move was a winner"""
        (
            last_move_row,
            last_move_col,
        ) = self.last_move  # destructures the last valid move
        color = self.game_board[last_move_row][
            last_move_col
        ]  # determines the color/value of the last move
        row = last_move_row
        connect_four = True
        for _ in range(
            0, 4
        ):  # only checks the last move and the next three values for a match
            if (
                row >= len(self.game_board)
                or self.game_board[row][last_move_col] != color
            ):
                connect_four = (
                    False  # if the series of values do not match break and return False
                )
                break
            row += 1

        return connect_four


"""

def test_vertical_win():
    assert check_vertical_win(board_vertical_win, (0, 0)) == True


def test_vertical_loss_too_few():
    assert check_vertical_win(board_vertical_loss_too_few, (3, 0)) == False


def test_vertical_loss_non_contiguous():
    assert check_vertical_win(board_vertical_loss_non_contiguous, (1, 0)) == False
"""


def test_conn_vertical_win():
    """
    tests that a series of four identical vertical values in self.game_board
    check_vertical_win is expected to return True
    """
    conn_four = ConnectFour()
    conn_four.game_board = [
        [1, None, None, None, None, None, None],
        [1, None, None, None, None, None, None],
        [1, None, None, None, None, None, None],
        [1, None, None, None, None, None, None],
        [0, None, None, None, None, None, None],
        [0, None, None, None, None, None, None],
    ]
    conn_four.last_move = (0, 0)
    assert conn_four.check_vertical_win() is True


def test_conn_vertical_loss_too_few():
    """
    tests 3 identical values in a column within self.game_board
    check_vertical_win is expected to return False
    """
    conn_four = ConnectFour()
    conn_four.last_move = (3, 0)
    conn_four.game_board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [1, None, None, None, None, None, None],
        [1, None, None, None, None, None, None],
        [1, None, None, None, None, None, None],
    ]
    assert conn_four.check_vertical_win() is False


def test_conn_vertical_loss_non_contiguous():
    """
    tests whether a non-contiguous series of four identical values in a column
    within self.game_board returns False when check_vertical_win is called
    """
    conn_four = ConnectFour()
    conn_four.game_board = [
        [None, None, None, None, None, None, None],
        [1, None, None, None, None, None, None],
        [1, None, None, None, None, None, None],
        [0, None, None, None, None, None, None],
        [1, None, None, None, None, None, None],
        [1, None, None, None, None, None, None],
    ]
    conn_four.last_move = (1, 0)
    assert conn_four.check_vertical_win() is False


def test_full_column():
    """
    tests whether the self.game_board is full of values
    """
    conn_four = ConnectFour()
    if conn_four.player_turn == 1:
        conn_four.game_board = [
            [1, None, None, None, None, None, None],
            [1, None, None, None, None, None, None],
            [0, None, None, None, None, None, None],
            [1, None, None, None, None, None, None],
            [1, None, None, None, None, None, None],
            [1, None, None, None, None, None, None],
        ]
        with pytest.raises(ValueError):
            conn_four.drop_coin(0)

    else:
        conn_four.game_board = [
            [0, None, None, None, None, None, None],
            [1, None, None, None, None, None, None],
            [0, None, None, None, None, None, None],
            [1, None, None, None, None, None, None],
            [0, None, None, None, None, None, None],
            [0, None, None, None, None, None, None],
        ]
        with pytest.raises(ValueError):
            conn_four.drop_coin(0)


def test_drop_coin():
    """
    tests that the drop_coin method inserts the correct value within the game board
    """
    conn_four = ConnectFour()
    assert len(conn_four.game_board) == 6
    assert len(conn_four.game_board[0]) == 7

    if conn_four.player_turn == 1:
        conn_four.drop_coin(0)
        assert conn_four.game_board == [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [1, None, None, None, None, None, None],
        ]
        conn_four.drop_coin(0)
        assert conn_four.game_board == [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [0, None, None, None, None, None, None],
            [1, None, None, None, None, None, None],
        ]
    else:
        conn_four.drop_coin(0)
        assert conn_four.game_board == [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [0, None, None, None, None, None, None],
        ]
        conn_four.drop_coin(0)
        assert conn_four.game_board == [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [1, None, None, None, None, None, None],
            [0, None, None, None, None, None, None],
        ]


def test_connect_four_game_state():
    """testing Connect Four game state after initialization"""
    conn_four = ConnectFour()
    assert len(conn_four.game_board) == 6
    assert len(conn_four.game_board[0]) == 7

    if conn_four.player_turn == 1:
        conn_four.switch_turns()
        assert conn_four.player_turn == 0
        conn_four.switch_turns()
        assert conn_four.player_turn == 1
    else:
        conn_four.switch_turns()
        assert conn_four.player_turn == 1
        conn_four.switch_turns()
        assert conn_four.player_turn == 0


# implement check_win() - checks four diff ways to win


def check_vertical_win(board: list[list[int]], last_move: tuple[int, int]) -> bool:
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


t_board = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
]
