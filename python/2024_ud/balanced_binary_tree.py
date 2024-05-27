class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"val: {self.val} - left: {self.left} - right: {self.right}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, value: object) -> bool:
        return self.__str__() == value.__str__()


def is_balanced(root: TreeNode) -> bool:
    """
    Given a binary tree, determine if it is
    height-balanced
    ."""
    # tree is alance l + r within depth 1

    # counter = 0
    counter = 0
    
    # recurse(node, counter)
    def recurse(node, counter):
        
        # if node has left or right
        if node:
            # recurse(node.left, counter + 1), same with right

            left, left_balance = recurse(node.left,  counter + 1)
            right, right_balance = recurse(node.right,  counter +1)
            # if node doesn't have l/r , return counter
            
            return max(left, right), abs(left-right) < 1

        return counter, True

    left, right = 0, 0
    # left = recurse(root.left, counter+1), same right
    if root:
        left, left_balance = recurse(root.left,  1)
        right, right_balance = recurse(root.right,  1)
    # return abs(left - right) <= 1
        
        if left_balance is False or right_balance is False:
            return False
    
    return abs(left - right) <= 1


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


def balanced_again_w_alex(root):
    def recurse(node):
        if not node:
            return 0 , True
        left_height, left_is_balanced = recurse(node.left)
        right_height, right_is_balanced = recurse(node.right)
        return 1+ max(left_height, right_height), abs(left_height - right_height) <= 1 and left_is_balanced and right_is_balanced
    return recurse(root)[1]


def test_tree_builder():
    assert tree_builder([1, 2, 3]) == TreeNode(1, TreeNode(2), TreeNode(3))


def test_empty_tree():
    assert balanced_again_w_alex(tree_builder([])) is True


def test_no_children():
    assert balanced_again_w_alex(tree_builder([1])) is True

def test_one():
    '''
        3
      /   \\
     9     20
          /  \\
         15   7 
    '''
    assert balanced_again_w_alex(tree_builder([3,9,20,None,None,15,7])) == True
#test_one()
def test_unbalanced_tree():
    """
         1
       /   \\
      2     2
     / \\  / \\
    3  N  N   3
   / \\       /
  4   N      4
    """
    assert (
        balanced_again_w_alex(tree_builder([1, 2, 2, 3, None, None, 3, 4, None, None, 4]))
        is False
    )

def test_209():
    '''
            1
          /    \\
        2        3
      /  \\    /   \\
    4      5  6     None
   //
  8
    '''
    assert balanced_again_w_alex(tree_builder([1,2,3,4,5,6,None,8])) == True