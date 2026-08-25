class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen=set(nums)
        mul=k
        while mul in seen:
            mul+=k
        return mul