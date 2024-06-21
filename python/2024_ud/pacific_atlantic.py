from collections import deque


def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    queue = deque()
    
    answer = []
    for row, array in enumerate(heights):
        for col, cell in enumerate(array):
            atlantic = False
            pacific = False
            queue.append((row, col))
            visited = set()
            while queue:
                # redo all of this again as x, y coords
                r, c = queue.popleft()
                current = heights[r][c]
                
                if r == 0 or c == 0:
                    # at the pacific
                    pacific = True
                if r == len(heights[0]) - 1 or c == len(heights) - 1:
                    # at the atlantic
                    atlantic = True
                
                if (row - 1, col) not in visited and row > 0 and current >= heights[row - 1][col] :
                    queue.append((row - 1, col))
                    visited.add((row - 1, col))
                
                if (row,col - 1) not in visited and col > 0 and  current >= heights[row][col - 1] :
                    queue.append((row,col - 1))
                    visited.add((row,col - 1))
                if (row,col + 1) not in visited and col < len(heights) -1 and current >= heights[row][col + 1] :
                    queue.append((row,col + 1))
                    visited.add((row,col + 1))
                if (row + 1,col) not in visited and row < len(heights[0])-1 and  current >= heights[row + 1][col] :
                    queue.append((row + 1,col))
                    visited.add((row + 1,col))
                
            if pacific and atlantic:
                answer.append([row, col])
    return answer




# [1,4], [3,0]
def pacific_atlantic_again(heights: list[list[int]]) -> list[list[int]]:
    stack = deque()
    
    answer = []
    visited = {
        'pacific'  : set(),
        'atlantic' : set(),
        'both' : set()
    }
    def recurse(row, col) -> tuple[bool, str]:
        if (row,col) == (1,4) or (row,col) == (3,0):
            breakpoint()
        if (row, col) in visited['both']:
            return (True, 'both')
        if row == 0 or col == 0: 
            visited['pacific'].add((row,col))
            
        if row == len(heights[0])-1 or col == len(heights)-1:
            visited['atlantic'].add((row,col))
        if (row, col) in visited['atlantic'] and (row, col) in visited['pacific']:
            visited['both'].add((row,col))
            answer.append([row,col])
            return (True, 'both')

        
        
        else:
            
            if row > 0 and heights[row][col] >= heights[row-1][col]:
                top, ocean = recurse(row -1, col)
                if top:
                    visited[ocean].add((row,col))
            if col < len(heights) - 1 and heights[row][col] >= heights[row][col+1]:
                right, ocean = recurse(row, col + 1)
                if right:
                    visited[ocean].add((row,col))
            if col > 0 and heights[row][col] >= heights[row][col-1]:
                left, ocean = recurse(row, col - 1)
                
                if left:
                    visited[ocean].add((row,col))
            if row < len(heights[0]) - 1 and heights[row][col] >= heights[row+1][col]:
                
                bottom, ocean = recurse(row + 1, col)
                if bottom:
                    visited[ocean].add((row,col))
            if (row,col) in visited['atlantic'] and (row,col) in visited['pacific']:
                visited['both'].add((row,col))
                answer.append([row,col])

        return (True, 'both') if (row,col) in visited['both'] else (True,'atlantic') if (row,col) in visited['atlantic'] else (True, 'pacific') if (row,col) in visited['pacific'] else (False, '')
    for r, val in enumerate(heights):
        for c, v in enumerate(val):
            recurse(r,c)
    return answer





def pac_atl(heights: list[list[int]]) -> list[list[int]]:
    '''
    [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    '''
    
    pacific = set()
    atlantic = set()
    
    def recurse(row, col, visited):
        if row == 0 or col == 0:
            pacific.add((row, col))
        if row == len(heights)-1 or col == len(heights[0])-1:
            atlantic.add((row, col))

        if row > 0 and heights[row][col] <= heights[row - 1][col] and (row-1, col) not in visited:
            visited.add((row-1, col))
            recurse(row-1, col, visited)
        if row < len(heights)-1 and heights[row][col] <= heights[row + 1][col] and (row+1, col) not in visited:
            visited.add((row + 1, col))
            recurse(row + 1, col, visited)
        if col > 0 and heights[row][col] <= heights[row][col -1] and (row, col - 1) not in visited:
            visited.add((row, col - 1))
            recurse(row, col  - 1, visited)
        if col < len(heights[0])-1 and heights[row][col] <= heights[row ][col + 1] and (row, col + 1) not in visited:
            visited.add((row, col + 1))
            recurse(row, col + 1, visited)
            



    for i, _ in enumerate(heights[0]):
        recurse(0, i, pacific)
        recurse(len(heights)-1, i, atlantic)
    for i, _ in enumerate(heights):
        recurse( i, 0, pacific)
        recurse( i, len(heights[0])-1, atlantic)
    return [list(x) for x in list(atlantic & pacific) ]




def test_ex_one():
    assert pac_atl(
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    ) == [[4, 0], [0, 4], [3, 1], [1, 4], [3, 0], [2, 2], [1, 3]]