import heapq
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
        for nd, weight in graph[node]:
            if nd not in path:
                path[nd] = weight + distance
            if nd in path and path[nd] > weight + distance:
                path[nd] = weight + distance
            recurse(nd, weight + distance)

    recurse(src, 0)
    return path


def shortest_path(n: int, edges: list[list[int]], src: int) -> dict[int, int]:
    graph = dict()
    for node, neighbor, distance in edges:
        if node in edges:
            graph[node].append((neighbor, distance))
        else:
            graph[node] = [(neighbor, distance)]

    finished = set()
    result = dict()
    unvisited = []
    heapq.heapify(unvisited)
    heapq.heappush(unvisited, (0, src))
    distance = 0
    # while len(finished) < n:
    #     current_distance, current_node = heapq.heappop(unvisited)
    #     if current_node == 4:
    #         breakpoint()
    #     if current_node in graph:
    #         for neighbor, weight in graph[current_node]:
    #             heapq.heappush(unvisited, (weight + distance, neighbor))
    #     finished.add(current_node)
    #     if current_node not in result:
    #         result[current_node] = current_distance
    #     elif current_distance < result[current_node]:
    #         result[current_node] = current_distance

    # return result
    while unvisited:
        distance_one, neighbor = heapq.heappop(unvisited)
        if neighbor in finished:
            continue
        result[neighbor] = distance_one

        for node, weight in graph[neighbor]:
            if node not in result:
                heapq.heappush(unvisited, (weight, node))

    for i in range(n):
        if i not in result:
            result[i] = -1
    return result


def shortest_iterative(n: int, edges: list[list[int]], src: int) -> dict[int, int]:
    """
    Set all vertices distances = infinity except for the source vertex, set the source distance = 0

    Push the source vertex in a min-priority queue in the form (distance , vertex), as the comparison in the min-priority queue will be according to vertices distances.
    Pop the vertex with the minimum distance from the priority queue (at first the popped vertex = source).
    Update the distances of the connected vertices to the popped vertex in case of "current vertex distance + edge weight < next vertex distance", then push the vertex
    with the new distance to the priority queue.
    If the popped vertex is visited before, just continue without using it.
    Apply the same algorithm again until the priority queue is empty.
    """
    graph = dict()
    for origin, destination, weight in edges:
        if origin in graph:
            graph[origin].append((weight, destination))
        else:
            graph[origin] = [(weight, destination)]

    unvisited = []
    heapq.heapify(unvisited)
    visited = {src: 0}
    heapq.heappush(unvisited, (0, src))

    while unvisited:
        current_distance, node = heapq.heappop(unvisited)
        if node in graph:
            for dist, new_node in graph[node]:
                if new_node not in visited:
                    visited[new_node] = current_distance + dist
                    heapq.heappush(unvisited, (dist + current_distance, new_node))
                elif (
                    new_node in visited and current_distance + dist < visited[new_node]
                ):
                    visited[new_node] = current_distance + dist
                    heapq.heappush(unvisited, (dist + current_distance, new_node))

        if node not in visited:
            visited[node] = current_distance
        elif node in visited and current_distance < visited[node]:
            visited[node] = current_distance

    for i in range(n):
        if i not in visited:
            visited[i] = -1
    return visited


def shortest_recursive(n: int, edges: list[list[int]], src: int) -> dict:
    """
    Set all vertices distances = infinity except for the source vertex, set the source distance = 0

    Push the source vertex in a min-priority queue in the form (distance , vertex), as the comparison in the min-priority queue will be according to vertices distances.
    Pop the vertex with the minimum distance from the priority queue (at first the popped vertex = source).
    Update the distances of the connected vertices to the popped vertex in case of "current vertex distance + edge weight < next vertex distance", then push the vertex
    with the new distance to the priority queue.
    If the popped vertex is visited before, just continue without using it.
    Apply the same algorithm again until the priority queue is empty.
    """
    graph = dict()
    for origin, destination, weight in edges:
        if origin in graph:
            graph[origin].append((weight, destination))
        else:
            graph[origin] = [(weight, destination)]

    visited = {src: 0}
    unvisited = []
    heapq.heapify(unvisited)
    heapq.heappush(unvisited, (0, src))

    def recurse(node, distance):
        if node in graph:
            for added_distance, current_node in graph[node]:
                if (
                    current_node not in visited
                    or added_distance + distance < visited[current_node]
                ):
                    visited[current_node] = added_distance + distance
                    heapq.heappush(unvisited, (added_distance + distance, current_node))
        if unvisited:
            new_weight, new_node = heapq.heappop(unvisited)
            recurse(new_node, new_weight)

    recurse(src, 0)
    for i in range(n):
        if i not in visited:
            visited[i] = -1
    return visited


def test_one():
    assert shortest_recursive(
        5,
        [[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4], [2, 3, 8], [2, 4, 2], [3, 4, 5]],
        0,
    ) == {0: 0, 1: 7, 2: 3, 3: 9, 4: 5}


# test_one()


def test_two():
    """
    0  3>  1  1-> 2

    """
    assert shortest_recursive(3, [[0, 1, 3], [1, 2, 1], [2, 0, 4]], 0) == {
        0: 0,
        1: 3,
        2: 4,
    }


def test_three():
    assert shortest_recursive(
        4, [[0, 1, 5], [0, 2, 7], [1, 2, 2], [1, 3, 6], [2, 3, 4]], 1
    ) == {0: -1, 1: 0, 2: 2, 3: 6}
