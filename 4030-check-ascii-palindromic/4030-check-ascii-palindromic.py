class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary=""
        for i in s:
            binary+=format(ord(i),"08b")

        return binary==binary[::-1]