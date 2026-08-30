class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        min_idx=nums.index(min(nums))
        max_idx=nums.index(max(nums))
        left = min(min_idx,max_idx)
        right=max(min_idx,max_idx)
        ans1=right+1
        ans2=n-left
        ans3=(left+1)+(n-right)
        return min(ans1,ans2,ans3)