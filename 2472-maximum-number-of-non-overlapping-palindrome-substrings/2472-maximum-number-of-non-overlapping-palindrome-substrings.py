class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n=len(s)
        p=[[0]*n for _ in range(n)]
        dp=[0]*(n+1)
        for r in range(n):
            dp[r+1]=dp[r]
            for l in range(r,-1,-1):
                if s[l]==s[r] and (r-l<2 or p[l+1][r-1]):
                    p[l][r]=1
                    if r-l+1>=k:
                        dp[r+1]=max(dp[r+1],dp[l]+1)
        return dp[n]