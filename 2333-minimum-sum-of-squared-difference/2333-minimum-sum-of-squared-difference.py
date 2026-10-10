
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)

        left, right = 0, diff[0]

        while left < right:
            mid = (left + right) // 2
            needed = sum(max(0, d - mid) for d in diff)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        ans = 0
        used = 0

        for d in diff:
            reduced = min(d, level)
            used += d - reduced
            ans += reduced * reduced
        remaining = k - used

        for d in diff:
            if remaining == 0:
                break
            if d >= level:
                ans -= level * level
                ans += (level - 1) * (level - 1)
                remaining -= 1

        return ans
