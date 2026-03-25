# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 or l2 or carry:
            if l1:
                x = l1.val
            else:
                x = 0
            
            if l2:
                y = l2.val
            else:
                y = 0

            total = x + y + carry

            carry = total // 10
            digit = total % 10

            print(f"Carry: {carry}")
            print(f"Digit: {digit}")
            print(f"L1: {x} L2: {y}")
            print(f"Total: {total}\n")

            curr.next = ListNode(digit)
            curr = curr.next

            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next

        return dummy.next
