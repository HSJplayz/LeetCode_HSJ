class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        maxD=0
        for ch in s:
            if ch=='(':
                depth+=1
                maxD=max(maxD,depth)
            elif ch==')':
                depth-=1
        return maxD