class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common=min(need1,need2)
        cost=common*min(costBoth,cost1+cost2)
        remaining1=need1-common
        remaining2=need2-common
        cost+=remaining1*min(cost1,costBoth)
        cost+=remaining2*min(cost2,costBoth)
        return min(cost,max(need1,need2)*costBoth)