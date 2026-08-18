class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        pos={}
        ans=-1
        last=n-k

        for i in range(n):
            x=nums[i]
            if x not in pos:
                pos[x]=[]
            pos[x].append(i)
        for x in pos:
            positions=pos[x]
            intervals=[]
            for p in positions:
                L=max(0,p-k+1)
                R=min(p,last)
                if L<=R:
                    intervals.append((L,R))
            intervals.sort()
            covered=0
            if len(intervals)>0:
                curL=intervals[0][0]
                curR=intervals[0][1]
                for j in range(1,len(intervals)):
                    L=intervals[j][0]
                    R=intervals[j][1]
                    if L<=curR+1:
                        curR=max(curR,R)
                    else:
                        covered+=curR-curL+1
                        curL=L
                        curR=R
                covered+=curR-curL+1
            if covered==1:
                ans=max(ans,x)
        return ans