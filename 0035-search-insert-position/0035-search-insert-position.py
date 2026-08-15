class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        mid=(left+right)//2
        while right>=left:
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                right=mid-1
                mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
                mid=(left+right)//2
        return mid+1
            