class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1
        odd = [i for i in range(26) if cnt[i] & 1]
        if len(odd) > 1:
            return ""
        mid = chr(97 + odd[0]) if odd else ""
        half = [x // 2 for x in cnt]
        n = len(s) // 2
        def build(left, rem):
            for i in range(26):
                left += chr(i + 97) * rem[i]
            left = ''.join(left)
            return left + mid + left[::-1]
        left = []
        for i in range(n):
            t = ord(target[i]) - 97
            if half[t]:
                half[t] -= 1
                left.append(chr(t + 97))
                continue
            for c in range(t + 1, 26):
                if half[c]:
                    half[c] -= 1
                    return build(left + [chr(c + 97)], half)
            break
        ans = build(left[:], half[:])
        if ans > target:
            return ans
        for i in range(len(left) - 1, -1, -1):
            old = ord(left[i]) - 97
            half[old] += 1

            for c in range(old + 1, 26):
                if half[c]:
                    half[c] -= 1
                    return build(left[:i] + [chr(c + 97)], half)
            left.pop()
        return ""