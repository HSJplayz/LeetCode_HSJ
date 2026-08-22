class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum1=0
        n1=n
        product=1
        while n1>0:
            t=n1%10
            sum1+=t
            product*=t
            n1//=10
        return n%(product+sum1)==0