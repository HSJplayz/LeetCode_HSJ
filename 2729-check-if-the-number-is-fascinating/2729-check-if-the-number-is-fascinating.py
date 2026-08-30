class Solution:
    def isFascinating(self, n: int) -> bool:
        s=str(n)+str(n*2)+str(n*3)
        return len(s)==9 and set(s)==set("123456789")