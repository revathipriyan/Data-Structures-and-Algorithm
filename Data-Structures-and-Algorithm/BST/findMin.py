class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def inorder(root):
    
    if not root.left:
        return root.data
    
    curr = root.left
    while curr.left:
        curr = curr.left
    
    return curr.data
    
if __name__ == "__main__":
  
    # Representation of input binary search tree
    #        5
    #       / \
    #      4   6
    #     /     \
    #    3       7
    #   /
    #  1
    root = Node(5)
    root.left = Node(4)
    root.right = Node(6)
    root.left.left = Node(3)
    root.right.right = Node(7)
    

    print(inorder(root))
        