class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if abs(self.helpermax(root) - self.helpermin(root)) > 1:
            return False
        else:
            return True

    def helpermin(self, root: TreeNode) -> int:
        if root is None:
            return 0

        # 先檢查左右子樹是否為 None
        if root.right is None and root.left is None:
            return 1
        if root.right is None:
            return self.helpermin(root.left) + 1
        if root.left is None:
            return self.helpermin(root.right) + 1

        min1 = min(self.helpermin(root.right), self.helpermin(root.left)) + 1
        return min1

    def helpermax(self, root: TreeNode) -> int:
        if root is None:
            return 0

        # 先檢查左右子樹是否為 None
        if root.right is None and root.left is None:
            return 1
        if root.right is None:
            return self.helpermax(root.left) + 1
        if root.left is None:
            return self.helpermax(root.right) + 1

        max1 = max(self.helpermax(root.right), self.helpermax(root.left)) + 1
        return max1
