from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(root):
            cur = root.val if root else None
            if not root or root == p or root == q:
                return root

            left = dfs(root.left)
            left_val = left.val if left else None
            right = dfs(root.right)
            right_val = right.val if right else None

            if not left:
                right_val = right.val if right else None
                return right
            elif not right:
                return left
            else:
                r_now = root.val if root else None
                return root

        return dfs(root)


# ---------- Helper functions for testing ----------

def build_tree(arr):
    """Build binary tree from level-order array (None = null)."""
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1

    return root


def find_node(root, val):
    """Find node by value (values are unique)."""
    if not root:
        return None
    q = deque([root])
    while q:
        node = q.popleft()
        if node.val == val:
            return node
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return None


# ---------- Test ----------

def main():
    root_arr = [3,5,1,6,2,0,8,None,None,7,4]
    p_val = 5
    q_val = 4

    root = build_tree(root_arr)
    p = find_node(root, p_val)
    q = find_node(root, q_val)

    sol = Solution()
    lca = sol.lowestCommonAncestor(root, p, q)

    print("LCA:", lca.val)  


if __name__ == "__main__":
    main()
