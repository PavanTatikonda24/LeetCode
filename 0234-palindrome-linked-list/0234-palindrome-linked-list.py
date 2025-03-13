# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        head1=[]
        while head:
            head1.append(head.val)
            head=head.next
        x=0
        y=-1
        for v in range(1+(len(head1)//2)):
            if head1[x]==head1[y]:
                x+=1
                y-=1
            else:
                return False
        return True