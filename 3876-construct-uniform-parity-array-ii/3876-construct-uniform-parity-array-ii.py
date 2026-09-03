class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn=[float('inf'),float('inf')]
        for x in nums1:
            mn[x&1]=min(mn[x&1],x)
        for target in (0,1):
            if all((x&1)==target or mn[(x&1)^target]<x for x in nums1):
                return True
        return False