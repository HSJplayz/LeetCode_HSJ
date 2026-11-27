class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for _, price in items)
        dp = [0] * (budget + 1)

        for i in range(n):
            f_i, p_i = items[i]
            val = 1 + sum(1 for j in range(n) if i != j and items[j][0] % f_i == 0)
            for b in range(budget, p_i - 1, -1):
                if dp[b - p_i] + val > dp[b]:
                    dp[b] = dp[b - p_i] + val

        return max(dp[b] + (budget - b) // min_price for b in range(budget + 1))