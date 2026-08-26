class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        nums2_set=set(nums2)
        for i in nums1:
            if i in nums2_set:
                ans.append(i)
                nums2_set.remove(i)
        return ans

