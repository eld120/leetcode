

def binary_tree_postorder(root):
    answer = []
    def recurse(node):
        if node:
            recurse(node.left)
            recurse(node.right)
            answer.append(node.val)
        return answer
    return recurse(root)