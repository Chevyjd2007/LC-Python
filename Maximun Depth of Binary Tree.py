from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class solution:
    # DFS (recursively)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


    # BFS
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node20 = TreeNode(20, node15, node7)
    node9 = TreeNode(9)
    root = TreeNode(3, node9, node20)

    s = solution()
    print(s.maxDepth(root))