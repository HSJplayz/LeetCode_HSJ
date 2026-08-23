class Solution:
    def sumGame(self, num: str) -> bool:
        diff=0
        q1=q2=0
        n=len(num)
        for i in range(n//2):
            if num[i]=='?':
                q1=q1+1
            else:
                diff+=int(num[i])
        for i in range(n//2,n):
            if num[i]=='?':
                q2=q2+1
            else:
                diff-=int(num[i])
        q_diff=q2-q1
        if q_diff%2==0 and diff==9*q_diff//2:
            return False
        return True