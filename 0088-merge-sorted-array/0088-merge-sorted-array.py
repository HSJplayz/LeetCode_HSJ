class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pointer=m+n-1
        l1=m-1
        l2=n-1
        while l1>=0 and l2>=0:
            if nums1[l1]>=nums2[l2]:
                nums1[pointer]=nums1[l1]
                l1-=1
            else:
                nums1[pointer]=nums2[l2]
                l2-=1
            pointer-=1
        while l2>=0:
            nums1[pointer]=nums2[l2]
            l2-=1
            pointer-=1
        