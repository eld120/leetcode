from collections import deque
from data_structures import  tree_builder_list # pylint: disable=E0401


def level_order_traversal(root):
    queue = deque()
    answer = []
    if root:
        queue.append(root)
    while queue:
        

        temp = []
        for _ in range(len(queue)):
            current = queue.popleft()
            if current:
                temp.append(current.val)
                
                queue.append(current.left)
                queue.append(current.right)
        if temp:
            answer.append(temp)
        
    return answer

def test_one():
    assert level_order_traversal(tree_builder_list([1,2,3,4,5,6,7])) == [[1], [2,3], [4,5,6,7]]