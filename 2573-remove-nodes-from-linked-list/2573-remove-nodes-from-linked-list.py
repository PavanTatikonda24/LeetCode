# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        nums = []
        while head:
            while nums and nums[-1].val<head.val:
                nums.pop()
            nums.append(head)
            head=head.next
        result = ListNode(0)
        dummy = result
        for i in nums:
            result.next = i
            result = result.next
        result.next = None
        return dummy.next




      