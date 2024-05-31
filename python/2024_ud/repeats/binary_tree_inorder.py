from  collections import deque

class TreeNode:
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"val: {self.val}  left: {self.left}  right: {self.right} |"

    def __repr__(self) -> str:
        def traverse(root: TreeNode, level: int) -> str:
            if not root:
                return ''
            prefix = '  ' * level
            return f'{prefix}({root.val})\n' + traverse(root.left, level + 1) + traverse(root.right, level + 1)
        return str.rstrip(traverse(self, 0))

    def __eq__(self, value: object) -> bool:
        return self.__str__() == value.__str__()



def tree_builder_list(array: list[int]) -> TreeNode:
    if len(array) == 0:
        return None

    nodes = []

    val = array.pop(0)
    root = TreeNode(val)
    nodes.append(root)

    while len(array) > 0:
        curr = nodes.pop(0)

        left_val = array.pop(0)
        if left_val is not None:
            curr.left = TreeNode(left_val)
            nodes.append(curr.left)

        if len(array) > 0:
            right_val = array.pop(0)
            if right_val is not None:
                curr.right = TreeNode(right_val)
                nodes.append(curr.right)

    return root




def inorder_again(root):
    
    answer = []
    def recurse(node):
        if node:
            recurse(node.left)
            answer.append(node.val)
            recurse(node.right)
    recurse(root)
    return answer

def test_example_one():
    assert inorder_again(tree_builder_list([1, None, 2,3])) == [1,3,2]