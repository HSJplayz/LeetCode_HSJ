from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n=len(nums)
        vals=sorted(set(nums))
        m=len(vals)
        rank={v:i+1 for i,v in enumerate(vals)}
        cnt=[0]*(m+1)
        sm=[0]*(m+1)
        def update(i,dc,ds):
            while i<=m:
                cnt[i]+=dc
                sm[i]+=ds
                i+=i & -i
        def query(i):
            c=s=0
            while i>0:
                c+=cnt[i]
                s+=sm[i]
                i-=i & -i
            return c,s
        LOG=m.bit_length()
        def kth(kk):
            pos=0
            for b in range(LOG,-1,-1):
                np_=pos+(1<<b)
                if np_ <= m and cnt[np_]<kk:
                    pos=np_
                    kk-=cnt[np_]
            return pos+1
        cost=[0]*(n-x+1)
        total=0
        for i in range(n):
            update(rank[nums[i]],1,nums[i])
            total+=nums[i]
            if i>=x:
                out = nums[i-x]
                update(rank[out],-1,-out)
                total-=out
            if i>=x-1:
                r=kth((x+1)//2)
                med=vals[r-1]
                c,s=query(r)
                cost[i-x+1]=med*c-s+(total-s)-med*(x-c)
        INF=float('inf')
        prev=[0]*(n+1)
        for j in range(1,k+1):
            cur=[INF]*(n+1)
            for i in range(x,n+1):
                cur[i]=min(cur[i-1],prev[i-x]+cost[i-x])
            prev=cur
        return prev[n]