# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        nums=[]
        result=head
        while head:
            nums.append(head)
            head=head.next
        b=nums[-k]
        a=nums[k-1]
        a.val, b.val=b.val, a.val
        return result