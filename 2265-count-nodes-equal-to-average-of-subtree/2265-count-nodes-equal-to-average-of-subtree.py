# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans=0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0,0
            l_sum,l_cnt=dfs(node.left)
            r_sum,r_cnt=dfs(node.right)
            total=l_sum+r_sum+node.val
            total2=l_cnt+r_cnt+1
            if total//total2==node.val:
                ans+=1
            return total,total2
        dfs(root)
        return ans