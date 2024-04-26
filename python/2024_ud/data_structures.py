from collections import deque



class ListNode:
    def __init__(self, val=None, next_node=None) -> None:
        self.val = val
        self.next_node = next_node

    def __str__(self) -> str:
        return f'val: {self.val}, | next: {self.next_node}'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, value: object) -> bool:
        return self.__str__() == value.__str__()
    
    
def ll_builder(array: list) -> ListNode:
    head = ListNode()
    current = head
    for index, val in enumerate(array):
        current.val = val
        if index == len(array) -1:
            return head
        current.next_node = ListNode()
        current = current.next_node



class TreeNode:
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'val: {self.val} | left: {self.left} | right: {self.right} '
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, value: object) -> bool:
        return self.__str__() == value.__str__()
    
def tree_builder_adj_list(matrix: list[list[int]]) -> TreeNode:
    queue = deque()
    root = TreeNode()
    current = root
    queue.append(current)
    for index, array in enumerate(matrix):
        if index % 2 == 0:
            current = queue.popleft()
            if not current.val:
                current.val = array[0]
            current.left = TreeNode(array[1])
            queue.append(current.left)
        else:
            current.right = TreeNode(array[1])
            
            queue.append(current.right)
    return root


def test_tree_builder_thing():
    assert tree_builder_adj_list([[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]) == TreeNode(0, TreeNode(1, TreeNode(4), TreeNode(5)), TreeNode(2, TreeNode(3), TreeNode(6)))