class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        max_num=-1
        min_num=float('inf')
        for i in range(n):
            max_num=max(max_num,nums[i])
            min_num=min(nums[i:n])
            if (max_num-min_num)<=k:
                return i
        return -1

