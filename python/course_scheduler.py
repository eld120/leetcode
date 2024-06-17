

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    
    graph = dict()
    # start with 
    
    visited = set()
    
    for key, val in prerequisites:
        if key not in graph:
            graph[key] = [val]
        else:
            graph[key].append(val)
    # 
    def recurse(node, is_dup=set()):
        if node in is_dup:
            return False
        is_dup.add(node)
        # base case
        if node not in visited:
            visited.add(node)
            
            return True
        
        if node in graph:
            for val in graph[node]:
                return recurse(val, is_dup)


    for course, prereq in prerequisites:
        if recurse(course) is False:
            return False
    return True













def top_sort(num_courses: int, prereq: list[list[int]]) -> bool:

    '''
    prereq = [[1,1]]
    1 -> 0
   /    /
  3--> 2

    {1: [0],
    2: [0], 
    3: [1,2]}
    '''
    # graph : dict of courses : prereqs
    graph = dict()
    for c, p in prereq:
        
        if c in graph:
            graph[c].append(p)
        else:
            graph[c] = [p]

    cycle = set()
    visited =  set()

    # def recurse(course)
    def recurse(course: int) -> bool:
        if course in cycle:
            return False
        if course not in graph or course in visited:
            return True
        # cycle set
        # add course to cycle
        cycle.add(course) # 3
        # for prereq in graph[course]
        
        
        for prereq in graph[course]:
            # if  recurse(prereq) is false return false
            if recurse(prereq) is False:
                return False
        cycle.remove(course)
        visited.add(course) # 1, 2, 3
        return True
        # return true

    # for course in graph call recurse(course)
    for c in graph:
        if recurse(c) is False:
            return False
    return True











def test_four_prereqs():
    '''
    1 -> 0
   /    /
  3--> 2

    {1: [0],
    2: [0], 
    3: [1,2]}
    '''
    assert top_sort(4,[[1,0],[2,0],[3,1],[3,2]] ) == True


def test_one_prereq():
    '''
    0 -> 1

    {1: 0}
    '''
    assert top_sort(2, [[1,0]]) == True

def test_cycle():
    assert top_sort(1, [[1,0], [0,1]]) == False