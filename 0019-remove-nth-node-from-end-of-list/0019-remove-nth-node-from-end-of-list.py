# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy=[]
        if not head:
            return None
        while head:
            dummy.append(head.val)
            head=head.next
        dummy.pop(-n)
        l=len(dummy)
        result=ListNode()
        final=result
        for i in dummy:
            result.next=ListNode()
            result.next.val=i
            result=result.next
        return final.next



