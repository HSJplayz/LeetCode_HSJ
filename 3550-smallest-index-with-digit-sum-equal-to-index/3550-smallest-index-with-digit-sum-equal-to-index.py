class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n=nums[i]
            summed=0
            while n>0:
                summed+=n%10
                n//=10
            if summed==i:
                return i

        return -1