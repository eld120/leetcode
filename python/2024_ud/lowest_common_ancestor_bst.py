from data_structures import TreeNode

def lowest_ancestor(root: TreeNode, p : TreeNode, q : TreeNode) -> TreeNode:
    def recurse(node):
        # if p is on the left and q is on the right or p is right q is left

        if p.val < node.val and q.val > node.val or p.val > node.val and q.val < node.val:
            return node
        # if root is p or root is q
        if node.val == p.val or node.val == q.val:
            return node
        if  p.val < node.val:
            return recurse(node.left)
        # if p less than root go left else go right       
        
            
        return recurse(node.right)
    return recurse(root)