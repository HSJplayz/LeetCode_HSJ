from typing import List
from math import gcd
from functools import reduce
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def lcm(a,b):
            return a//gcd(a,b)*b
        def count(x):
            ans=0
            n=len(coins)
            for mask in range(1,1<<n):
                val=1
                bits=0
                for i in range(n):
                    if mask & (1<<i):
                        bits+=1
                        val=lcm(val,coins[i])
                        if val>x:
                            break
                if val<=x:
                    if bits%2:
                        ans+=x//val
                    else:
                        ans-=x//val
            return ans
        left=1
        right=min(coins)*k
        while left<right:
            mid=(left+right)//2
            if count(mid)>=k:
                right=mid
            else:
                left=mid+1
        return left