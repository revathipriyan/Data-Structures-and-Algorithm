class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        def is_leaf(node):
            return not node.left and not node.right

        res = [root.val]

        # 1. Left boundary (excluding leaves)
        cur = root.left
        while cur:
            p = cur.val

            if not is_leaf(cur):
                res.append(cur.val)
            cur = cur.left if cur.left else cur.right
            cur_val = cur.val if cur else None

        # 2. All leaf nodes
        def add_leaves(node):
            now = node.val if node else None
            if not node:
                return
            if is_leaf(node):
                res.append(node.val)
                return
            add_leaves(node.left)
            add_leaves(node.right)

        add_leaves(root)

        # 3. Right boundary (excluding leaves, bottom-up)
        stack = []
        cur = root.right
        while cur:
            if not is_leaf(cur):
                stack.append(cur.val)
            cur = cur.right if cur.right else cur.left

        res.extend(reversed(stack))
        return res


def main():
    """
            1
           / \
          2   3
         / \   \
        4   5   6
           / \
          7   8

    Boundary traversal:
    Root: 1
    Left boundary: 2
    Leaves: 4, 7, 8, 6
    Right boundary: 3
    Result = [1, 2, 4, 7, 8, 6, 3]
    """

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)
    root.right.right = TreeNode(6)

    sol = Solution()
    result = sol.boundaryOfBinaryTree(root)
    print("Boundary Traversal:", result)


if __name__ == "__main__":
    main()
