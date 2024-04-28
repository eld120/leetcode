

def find_teh_judge(n: int, trust:list[list[int]]) -> int:
    '''
    Example 1:

    Input: n = 2, trust = [[1,2]]
    Output: 2
    Example 2:

    Input: n = 3, trust = [[1,3],[2,3]]
    Output: 3
    Example 3:

    Input: n = 3, trust = [[1,3],[2,3],[3,1]]
    Output: -1
    '''                   
    # suspect the judge trust[1] but not if found in trust[0]

    # people, potential judges
    people = set()
    judges = set()

    # and add trust[1] to judges 
    for tup in trust:
        judges.add(tup[1])
        people.add(tup[0])
    # for every pair people, add trust[0] to people 
        # if trust[0] in people, then remove trust[0] from judges
        if tup[1] in people and tup[1] in judges:
            judges.remove(tup[0])
        if tup[0] in people and tup[0] in judges:
            judges.remove(tup[1])

    # if not judges: return -1 otherwise return judges[0]
    if not judges:
        return -1
    return list(judges)[0]

