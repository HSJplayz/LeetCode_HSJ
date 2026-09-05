class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        max_idx=float('-inf')
        suffix_min=[0]*n
        suffix_min[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suffix_min[i]=min(nums[i],suffix_min[i+1])
        for i in range(n):
            max_idx = max(max_idx, nums[i])
            if max_idx-suffix_min[i]<=k:
                return i
        return -1