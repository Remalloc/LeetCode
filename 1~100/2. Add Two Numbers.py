# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        flag = 0
        cnt = 0
        while l1 or l2 or flag:
            numsum = 0
            if l1:
                numsum += l1.val
                l1 = l1.next
            if l2:
                numsum += l2.val
                l2 = l2.next
            if cnt == 0:
                l3 = ListNode(numsum % 10)
                p = l3
            else:
                numsum+=flag
                temp = ListNode(numsum % 10)
                p.next = temp
                p = temp
            flag = numsum // 10
            cnt += 1
        return l3