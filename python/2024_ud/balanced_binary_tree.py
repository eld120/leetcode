

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'val: {self.val} - left: {self.left} - right: {self.right}'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, value: object) -> bool:
        return self.__str__() == value.__str__()


def is_balanced(root: TreeNode) -> bool:
    '''
    Given a binary tree, determine if it is 
    height-balanced
    .'''
    # tree is alance l + r within depth 1

    # counter = 0
    counter = 0
    # recurse(node, counter)
    def recurse(node, counter):
        breakpoint()
        # if node has left or right
        if node:
        # recurse(node.left, counter + 1), same with right
            left =  recurse(node.left, counter + 1)
            right = recurse(node.right, counter + 1)
        # if node doesn't have l/r , return counter
            return max(left, right)
        
        return counter
    left, right = 0,0
    # left = recurse(root.left, counter+1), same right
    if root:
        left = recurse(root.left, counter + 1)
        right = recurse(root.right, counter + 1)
    # return abs(left - right) <= 1
    return abs(left-right) <= 1

from collections import deque

def tree_builder(array: list[int]) -> TreeNode:
    queue = deque()
    root = TreeNode()
    current = root
    for val in array:
        if not current.val:
            current.val = val
        elif not current.left:
            current.left = TreeNode(val)
            queue.append(current.left)
        elif not current.right:
            current.right = TreeNode(val)
            queue.append(current.right)
        else:
            current = queue.popleft()

    return root

def test_tree_builder():
    assert tree_builder([1,2,3]) == TreeNode(1, TreeNode(2), TreeNode(3))


def test_empty_tree():
    assert is_balanced(tree_builder([])) is True

def test_no_children():
    assert is_balanced(tree_builder([1])) is True

def test_unbalanced_tree():
    assert is_balanced(tree_builder([1,2,2,3,None,None,3,4,None,None,4])) is False