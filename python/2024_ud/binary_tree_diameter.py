from collections import deque
from data_structures import TreeNode, tree_builder_list

def diameter_of_tree(root) -> int:
    count = [0]
    def recurse(node):
        
        left = right = 0
        if node:
            left = recurse(node.left )
            right = recurse(node.right)
            count[0] = max(count[0], left+ right)
            return left + 1 if left > right else right + 1
        return 0
    
    recurse(root)
    return count[0]



def test_one():
    assert diameter_of_tree(tree_builder_list([1,2,3,4,5])) == 3