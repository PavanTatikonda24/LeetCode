# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1=[]
        result=ListNode()
        final=result
        while head:
            head1.append(head.val)
            head=head.next
        n=-1
        for i in range(len(head1)):
            result.next=ListNode()
            result.next.val=head1[n]
            result=result.next
            n-=1
        return final.next