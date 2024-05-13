from collections import deque



class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return f'val:{self.val} left:{self.left} right:{self.right}'
    
    def __repr__(self) -> str:
        def traverse(root: TreeNode, level: int) -> str:
            if not root:
                return ''
            prefix = '  ' * level
            return f'{prefix}({root.val})\n' + traverse(root.left, level + 1) + traverse(root.right, level + 1)
        return str.rstrip(traverse(self, 0))
    
    def __eq__(self, value: object) -> bool:
        return self.__str__() == value.__str__()

def build_tree(arr: list[int]) -> TreeNode | None:
    if len(arr) == 0:
        return None

    nodes = []

    val = arr.pop(0)
    root = TreeNode(val)
    nodes.append(root)

    while len(arr) > 0:
        curr = nodes.pop(0)

        left_val = arr.pop(0)
        if left_val is not None:
            curr.left = TreeNode(left_val)
            nodes.append(curr.left)

        if len(arr) > 0:
            right_val = arr.pop(0)
            if right_val is not None:
                curr.right = TreeNode(right_val)
                nodes.append(curr.right)
    return root


def inorder_traversal(root):
    '''
    ex: 1      -> 1, 3, 2
          2 
        3
    '''
    root = build_tree(root)
    current = root
    answer = []
    def recurse(current):
        if current:
            
            recurse(current.left)
            answer.append(current.val)
            recurse(current.right)
        return answer
         
    return recurse(current)


def test_buider():
    assert build_tree([1,None,2,3]) == TreeNode(1,None, TreeNode(2, TreeNode(3)))


def test_one():
    assert inorder_traversal([1,None,2,3]) == [1,3,2]