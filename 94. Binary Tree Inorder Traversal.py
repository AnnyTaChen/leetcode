class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return
        self.helper(root.left, result)
        result.append(root.val)
        self.helper(root.right, result)
