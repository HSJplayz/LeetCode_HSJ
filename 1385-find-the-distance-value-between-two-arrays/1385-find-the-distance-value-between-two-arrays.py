class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        cnt=0
        for i in arr1:
            flag=True
            for j in arr2:
                if abs(i-j)<=d:
                    flag=False
                    break
            if flag:
                cnt+=1
        return cnt