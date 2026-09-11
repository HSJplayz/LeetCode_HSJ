class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt=[0]*10
        for i in digits:
            cnt[i]+=1
        ans=0
        for i in range(100,1000,2):
            a=i//100
            b=(i//10)%10
            c=i%10
            need=[0]*10
            need[a]+=1
            need[b]+=1
            need[c]+=1
            if all(need[d]<=cnt[d] for d in range(10)):
                ans+=1
        return ans