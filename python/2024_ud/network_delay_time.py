import heapq


def network_delay_time(edges: list[list[int]], n: int, src: int) -> int:
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

    longest = 0
    for parent, child, length in edges:
        if parent not in visited or child not in visited or len(visited) < n:
            return -1
        longest = max(longest, visited[parent])
        longest = max(longest, visited[child])

    return longest


def test_one():
    assert network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2


def test_amillion():
    assert network_delay_time([[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]], 4, 1) == -1
