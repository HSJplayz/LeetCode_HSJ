class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n=len(nums)
        result=0
        isZero=True
        for i in nums:
            result^=i
            if i !=0:
                isZero= False
        if isZero:
            return 0
        return n-1 if result==0 else n