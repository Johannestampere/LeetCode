# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = []
        num2 = []

        p = l1
        while p:
            num1.append(str(p.val))
            p = p.next

        q = l2
        while q:
            num2.append(str(q.val))
            q = q.next

        num1 = int(''.join(num1[::-1]))
        num2 = int(''.join(num2[::-1]))

        number = str(num1 + num2)
        digits = list(number[::-1])

        newList = ListNode(int(digits[0]))
        dummy = newList

        for digit in digits[1:]:
            dummy.next = ListNode(int(digit))
            dummy = dummy.next

        return newList