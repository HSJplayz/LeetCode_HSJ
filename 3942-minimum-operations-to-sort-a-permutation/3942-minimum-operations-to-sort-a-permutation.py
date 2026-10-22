from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        asc = all(nums[(i + 1) % n] == (nums[i] + 1) % n for i in range(n))
        desc = all(nums[(i + 1) % n] == (nums[i] - 1) % n for i in range(n))

        INF = float('inf')
        ans = INF

        if asc:
            k = nums[0]
            if k == 0:
                return 0
            ans = min(ans, n - k, k + 2)

        if desc:
            p = nums.index(n - 1)
            i0 = nums.index(0)
            ans = min(ans, p + 1, 1 + (n - 1 - i0))

        return -1 if ans == INF else ans