class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n=len(nums)
        N=1
        while N<n:
            N<<=1
        st=[[1]+[0]*k for _ in range(2*N)]
        for i,x in enumerate(nums):
            x%=k
            st[N+i]=[x]+[int(j==x) for j in range(k)]
        def merge(a,b):
            p=a[0]
            c=[p*b[0]%k]+a[1:]
            for r in range(k):
                c[p*r%k+1]+=b[r+1]
            return c
        for i in range(N-1,0,-1):
            st[i]=merge(st[i<<1],st[i<<1|1])
        def update(i,x):
            x%=k
            i+=N
            st[i]=[x]+[int(j==x) for j in range(k)]
            while i>1:
                i>>=1
                st[i]=merge(st[i<<1],st[i<<1|1])
        def query(l):
            left=right=None
            l+=N
            r=N+n
            while l<r:
                if l & 1:
                    left=st[l] if left is None else merge(left,st[l])
                    l+=1
                if r & 1:
                    r-=1
                    right=st[r] if right is None else merge(st[r],right)
                l>>=1
                r>>=1
            if left is None:
                return right
            if right is None:
                return left
            return merge(left,right)
        ans=[]
        for idx,val,start,x in queries:
            update(idx,val)
            ans.append(query(start)[x + 1])
        return ans
