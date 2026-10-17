
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {num: i for i, num in enumerate(nums)}
        swaps = 0

        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                j = pos[sorted_nums[i]]

                pos[nums[i]] = j
                pos[nums[j]] = i

                nums[i], nums[j] = nums[j], nums[i]
                swaps += 1

        return swaps
