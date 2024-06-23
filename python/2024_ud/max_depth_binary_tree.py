


def max_depth(root) -> int:
    counter = 0
    
    def recurse(node, count):
        left = right = 0
        if node:
            
            if node.left is None and node.right is None:
                return count + 1
            
            if node.left:
                left = recurse(node.left, count + 1)
            if node.right:
                right = recurse(node.right, count + 1)
        return left if left > right else right
    return recurse(root, counter)
