# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        li1=[]
        li2=[]
        while l1:
            li1.append(l1.val)
            l1 = l1.next
        while l2:
            li2.append(l2.val)
            l2 = l2.next
        x=len(li1)
        y=len(li2)
        z1=''
        z2=''
        n=-1
        for i in range(x):
            z1+=str(li1[n])
            n-=1
        n=-1
        for j in range(y):
            z2+=str(li2[n])
            n-=1
        z=int(z1)+int(z2)
        dummy=ListNode()
        result=dummy
        resli=[]
        for d in str(z):
            resli.append(d)
        n=-1
        for a in range(len(resli)):
            result.next=ListNode(int(resli[n]))
            result=result.next
            n-=1
        return dummy.next


