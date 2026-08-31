# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical=[]
        index=1
        min_dist=float('inf')
        max_dist=-1
        prev=head
        curr=head.next
        if not (curr and curr.next):
            return [-1,-1]
        while curr and curr.next:
            if (curr.val>prev.val and curr.val>curr.next.val) or (curr.val<prev.val and curr.val<curr.next.val):
                critical.append(index)
            prev=curr
            curr=curr.next
            index+=1
        if len(critical)<2:
            return [-1,-1]
        for i in range(1,len(critical)):
            min_dist=min(min_dist,critical[i]-critical[i-1])
        max_dist=critical[-1]-critical[0]
        return [min_dist,max_dist]
        