class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root, target_sum: int) -> bool:
    """
    Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

    A leaf is a node with no children.
    constraints
        The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000
    """

    def recurse(node, counter, target_sum):
        if not node:
            return None
        # init recursive function, params: node, counter: int, target_sum
        if not node.left and not node.right:
            # base case: if not node.left and not node.right then return node.val + counter == target_sum
            return node.val + counter == target_sum
        # recursive case: elif node.left: val_left = recurse(node.left, counter + node.val) if node.right:  val_right = recurse(node.right, counter+ node.val)
        # if val_left or val_right: return True
        else:
            val_left = recurse(node.left, counter + node.val, target_sum)
            val_right = recurse(node.right, counter + node.val, target_sum)

            if val_left or val_right:
                return True
            return False

    return recurse(root, 0, target_sum)


def test_no_node():
    assert has_path_sum(None, 10) == False


def test_base_case():
    assert has_path_sum([1], 1) == True


def test_recursive_case():
    assert has_path_sum([1, 2, 3], 4) == True
