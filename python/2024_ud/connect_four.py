

# implement check_win() - checks four diff ways to win

def check_vertical_win(board: list[list[int]], last_move: tuple[int]) -> bool:
    ''' board is 6x7 and last_move is the y,x coord of the last move'''
    last_move_row, last_move_col = last_move
    color = board[last_move_row][last_move_col]
    row = last_move_row
    connect_four = True
    for _ in range(0,4):
        if row >= len(board) or  board[row][last_move_col] != color:
            connect_four = False
            break
        row += 1

    return connect_four



board_vertical_win = [
    [1 , None, None, None, None, None, None],
    [1 , None, None, None, None, None, None],
    [1 , None, None, None, None, None, None],
    [1 , None, None, None, None, None, None],
    [0 , None, None, None, None, None, None],
    [0 , None, None, None, None, None, None],
   
]


board_vertical_loss_too_few = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None , None, None, None, None, None, None],
    [1 , None, None, None, None, None, None],
    [1 , None, None, None, None, None, None],
    [1 , None, None, None, None, None, None],
   
]

board_vertical_loss_non_contiguous = [
    [None, None, None, None, None, None, None],
    [1, None, None, None, None, None, None],
    [1 , None, None, None, None, None, None],
    [0, None, None, None, None, None, None],
    [1 , None, None, None, None, None, None],
    [1 , None, None, None, None, None, None],
   
]


def test_vertical_win():
    assert check_vertical_win(board_vertical_win, (0,0)) == True

def test_vertical_loss_too_few():
    assert check_vertical_win(board_vertical_loss_too_few, (3,0)) == False

def test_vertical_loss_non_contiguous():
    assert check_vertical_win(board_vertical_loss_non_contiguous, (1,0)) == False