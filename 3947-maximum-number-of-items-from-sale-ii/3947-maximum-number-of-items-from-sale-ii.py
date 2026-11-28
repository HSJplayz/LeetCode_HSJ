class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        mx = max(f for f, _ in items)
        cnt = [0] * (mx + 1)
        for f, _ in items:
            cnt[f] += 1
        mul = [sum(cnt[m] for m in range(f, mx + 1, f)) if cnt[f] else 0 for f in range(mx + 1)]
        pmin = min(p for _, p in items)
        total = 0
        for p, g in sorted((p, mul[f] - 1) for f, p in items if mul[f] > 1 and p < 2 * pmin):
            k = min(g, budget // p)
            total += 2 * k
            budget -= k * p
            if k < g:
                break
        return total + budget // pmin