from collections import deque



def dijkstra(n: int, edges: list[list[int]], src: int) -> dict[int, int]:

    graph = dict()
    path = {src: 0}
    for arr in edges:
        
        if arr[0] in graph:
            graph[arr[0]].append((arr[1], arr[2]))
        else:
            graph[arr[0]] = [(arr[1], arr[2])]
        
    def recurse(node, distance):
        
        if node not in graph:
            return
        for nd, weight  in graph[node]:
            if nd not in path:
                path[nd] = weight + distance
            if nd in path and path[nd] > weight + distance:
                path[nd] = weight + distance
            recurse(nd, weight + distance)
    recurse(src, 0)
    return path



def test_one():
    assert dijkstra(5,[[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]], 0 ) == {0:0, 1:7, 2:3, 3:9, 4:5}

#test_one()

def test_two():
    '''
    0  3>  1  1-> 2
    
    '''
    assert dijkstra(3, [[0,1,3],[1,2,1],[2,0,4]], 0) == {0:0, 1:3, 2:4}