class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        n = len(target)
        prefix = []
        for i in range(n):
            t = ord(target[i]) - ord('a')
            if cnt[t] > 0:
                prefix.append(target[i])
                cnt[t] -= 1
                continue
            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    result = prefix + [chr(c + ord('a'))]
                    cnt[c] -= 1
                    for x in range(26):
                        result.extend([chr(x + ord('a'))] * cnt[x])
                    return ''.join(result)
            break
        for i in range(len(prefix) - 1, -1, -1):
            old = ord(prefix[i]) - ord('a')
            cnt[old] += 1
            for c in range(old + 1, 26):
                if cnt[c] > 0:
                    result = prefix[:i] + [chr(c + ord('a'))]
                    cnt[c] -= 1
                    for x in range(26):
                        result.extend([chr(x + ord('a'))] * cnt[x])
                    return ''.join(result)
        return ""