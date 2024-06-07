

def binary_tree_preorder_traversal(root):
    answer = []
    def recurse(node):
        
        if node:
            answer.append(node.val)
            recurse(node.left)
            recurse(node.right)
        return answer
    return recurse(root)