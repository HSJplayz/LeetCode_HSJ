class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        pairs=sorted((val,idx) for idx,val in enumerate(nums))
        group=[]
        current=[pairs[0]]
        for i in range(1,len(pairs)):
            if pairs[i][0]-pairs[i-1][0]<=limit:
                current.append(pairs[i])
            else:
                group.append(current)
                current=[pairs[i]]
        group.append(current)
        ans=nums[:]
        for g in group:
            value=sorted(val for val,_ in g)
            index=sorted(idx for _,idx in g)
            for i,v in zip(index,value): 
                ans[i]=v
        return ans