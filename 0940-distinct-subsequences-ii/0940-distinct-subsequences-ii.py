class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9+7
        dp=1 #for distinct ''
        last=[0]*26
        for ch in s:
            i=ord(ch)-ord('a')
            dp2=(2*dp-last[i])%MOD
            last[i]=dp
            dp=dp2
        return (dp-1)%MOD