class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bal=0
        add=0
        for ch in s:
            if ch=='(':
                bal+=1
            else:
                if bal>0:
                    bal-=1
                else:
                    add+=1
        return add+bal