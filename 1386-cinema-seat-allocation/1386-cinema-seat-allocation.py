class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows={}
        for row,seat in reservedSeats:
            rows.setdefault(row,set()).add(seat)
        ans=(n-len(rows))*2
        for seats in rows.values():
            l={2,3,4,5}
            m={4,5,6,7}
            r={6,7,8,9}
            if l.isdisjoint(seats) and r.isdisjoint(seats):
                ans+=2
            elif(l.isdisjoint(seats) or m.isdisjoint(seats) or r.isdisjoint(seats)):
                ans+=1
        return ans