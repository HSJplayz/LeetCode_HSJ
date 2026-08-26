class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[left]=nums[i]
                left+=1
        while left<len(nums):
            nums[left]=0
            left+=1
        