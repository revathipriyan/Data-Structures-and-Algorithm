class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Note that it is not a generic inorder successor 
# function. It mainly works when the right child
# is not empty, which is  the case we need in BST
# delete.
def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

# This function deletes a given key x from the
# given BST and returns the modified root of the 
# BST (if it is modified).
def del_node(root, x):
  
    # Base case
    if root is None:
        return root

    # If key to be searched is in a subtree
    if root.key > x:
        root.left = del_node(root.left, x)
    elif root.key < x:
        root.right = del_node(root.right, x)
        
    else:
        # If root matches with the given key

        # Cases when root has 0 children or 
        # only right child
        if root.left is None:
            return root.right

        # When root has only left child
        if root.right is None:
            return root.left

        # When both children are present
        succ = get_successor(root)
        root.key = succ.key
        root.right = del_node(root.right, succ.key)
        
    return root

# Utility function to do inorder traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Driver code
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(18)
    x = 15

    root = del_node(root, x)
    inorder(root)
    print()
