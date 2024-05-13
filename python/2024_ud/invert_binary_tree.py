from collections import deque


def invert_tree(root):
    '''
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
    '''
    # if root:
    def recurse(root):
        if root:
            # temp = root.left, set root.left = root.right, root.rigth = temp
            temp = root.left
            root.left = root.right
            root.right = temp
            

            # recurse(root.left) recurse(root.right)
            recurse(root.left)
            recurse(root.right)
            # return root
        return root
    return recurse(root)
            
        

def invert_tree_two(root):
    stack = deque()
    stack.append(root)

    while stack:
        current = stack.pop()

        if current:
            temp = current.left
            current.left = current.right
            current.right = temp
            stack.append(current.left)
            stack.append(current.right)
    return root