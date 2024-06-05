from collections import deque



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




def delete_node(root: TreeNode, key) -> TreeNode:
    # find node
    queue = deque()
    if not root:
        return root
    queue.append(root)
    while queue:
        
        current = queue.popleft()
        #breakpoint()
        if current.val == key:
            #breakpoint()
            if not current.left and not current.right:
                current = None
            if current.left and current.right:
                # replace node w/ smallest node to the right if node has 2 children
                smallest_node = current.right
                while smallest_node.left:
                    if smallest_node.left:
                        smallest_node=smallest_node.left
                current.val = smallest_node.val
                if current.right:
                    current.right = None
                
            elif current.left or current.right:
                # if node has one child swap
                active_node = current.left if current.left else current.right
                current.val = active_node.val
                if active_node.left:
                    current.left = active_node.left
                elif active_node.right:
                    current.right = active_node.right
                del active_node
            elif not current.left and not current.right:
                return None
            else:
                #  if no children delete
                del current
            break
        elif current.left and current.val >= key:
            queue.append(current.left)
        elif current.right:
            queue.append(current.right)
    print(root)
    return root

def find_min_node(node):
    while node.left:
        node = node.left
    return node

def claude_deletes(root, key):
    if not root:
        return None
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:  # Node to delete found
        if not root.left and not root.right:  # Leaf node
            return None
        elif not root.left:  # Node with one right child
            return root.right
        elif not root.right:  # Node with one left child
            return root.left
        else:  # Node with two children
            successor = find_min_node(root.right)  # Find inorder successor
            root.val = successor.val        # Replace value
            root.right = delete_node(root.right, successor.val)  # Delete successor
    return root

def test_example():
    assert del_node_again(tree_builder_list([5,3,6,2,4,None,7]), 3) == TreeNode(5, TreeNode(4, TreeNode(2)), TreeNode(6, None, TreeNode(7)))

def test_claude():
    assert del_node_again(tree_builder_list([5,3,6,2,4,None,7]), 3) == TreeNode(5, TreeNode(4, TreeNode(2)), TreeNode(6, None, TreeNode(7)))




def delete_node(root: TreeNode, key: int) -> TreeNode:
    
    def recurse(node):
        if node is None:
                return None
        elif node.val == key:
            # if node.val is key
            if node.left and node.right:
                # node has two children
                    # find the smallest node in the node.right subtree
                current = node.right
                while current.left:
                    current = current.left
                return current
                    # while loop node.right but then look for node.left afterwards
                        # return min_node
                
            elif node.left or node.right:
                # node has one child
                if node.left:
                    return node.left
                else:
                    return node.right
                
                    # swap values between node and child, but del child
                # node has no children
            else:
                del node
                    # delete node and return none            
        # if node.val > key
        elif node.val > key:
            return recurse(node.left)
                 # search node.left
        # if node.val < key        
        else:
            # search node.right
            return recurse(node.right)
    return recurse(root)







def del_node_again(root: TreeNode, key: int) -> TreeNode:
    if not root:
        return None
    # if node.val is key
    elif root.val == key:
        # node has two children
        if root.left and root.right:
            # find the smallest node in the node.right subtree
            # while loop node.right but then look for node.left afterwards
            current = root.right
            while current.left:
                current = current.left
            temp = current
            root.val = temp.val
            root.right = del_node_again(root.right, temp.val)
                # return min_node
        # node has one child
        elif root.left or root.right:
            if root.left:
                root.left = del_node_again(root.left, key)
            else:
                root.right = del_node_again(root.right, key)
            # swap values between node and child, but del child
        # node has no children
        else:
            # delete node and return none            
            del root
            return None
    # if node.val > key
    elif root.val > key:
        # search node.left
        root.left = del_node_again(root.left, key)
    # if node.val < key      
    elif root.val < key:  
        # search node.right
        root.right = del_node_again(root.right, key)
    return root

