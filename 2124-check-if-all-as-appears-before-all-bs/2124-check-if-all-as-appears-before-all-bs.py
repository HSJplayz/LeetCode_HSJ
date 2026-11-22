class Solution:
    def checkString(self, s: str) -> bool:
        start_a=False
        has_b=False
        for ch in s:
            if ch=='a' and has_b:
                return False
            elif ch=='a':
                start_a=True
            elif ch=='b':
                has_b=True
            elif ch=='b' and not start_a:
                return False
        return True