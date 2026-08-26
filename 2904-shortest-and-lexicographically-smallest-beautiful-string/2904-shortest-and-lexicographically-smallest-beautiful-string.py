class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left=0
        ones=0
        best=""
        for right in range(len(s)):
            if s[right]=="1":
                ones+=1
            while ones>k:
                if s[left]=="1":
                    ones-=1
                left+=1
            if ones==k:
                while left<=right and s[left]=="0":
                    left+=1
                cur=s[left:right+1]
                if best=="" or len(cur)<len(best):
                    best=cur
                elif len(cur)==len(best) and cur<best:
                    best=cur
        return best