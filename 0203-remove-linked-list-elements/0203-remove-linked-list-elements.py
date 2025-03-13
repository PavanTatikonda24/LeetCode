# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        head1=ListNode()
        result=head1
        while head:                
            if head.val==val:
                head=head.next
            else:
                head1.next=ListNode()
                head1=head1.next
                head1.val=head.val
                head=head.next
        return result.next
