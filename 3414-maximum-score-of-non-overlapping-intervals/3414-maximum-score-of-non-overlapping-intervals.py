class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        from bisect import bisect_left

        a = sorted((r, l, w, i) for i, (l, r, w) in enumerate(intervals))
        e = [x[0] for x in a]
        n = len(a)

        p = [bisect_left(e, a[i][1], 0, i) for i in range(n)]
        dp = [[(-1, ()) for _ in range(5)] for _ in range(n + 1)]
        dp[0][0] = (0, ())

        for i, (r, l, w, idx) in enumerate(a, 1):
            dp[i] = dp[i - 1].copy()

            for k in range(1, 5):
                s, ids = dp[p[i - 1]][k - 1]
                if s >= 0:
                    t = (s + w, tuple(sorted(ids + (idx,))))
                    if t[0] > dp[i][k][0] or \
                       (t[0] == dp[i][k][0] and t[1] < dp[i][k][1]):
                        dp[i][k] = t

        ans = max(dp[n], key=lambda x: (x[0], tuple(-i for i in x[1])))
        return list(ans[1])