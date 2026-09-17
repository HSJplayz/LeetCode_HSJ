class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)
        best=[10**9]*n
        ans=10**9
        s=j=0
        for i,x in enumerate(arr):
            s+=x
            while s>target:
                s-=arr[j]
                j+=1
            if s==target:
                l=i-j+1
                if j:
                    ans=min(ans,l+best[j-1])
                best[i]=min(l,best[i-1] if i else 10**9)
            elif i:
                best[i]=best[i-1]
        return -1 if ans==10**9 else ans