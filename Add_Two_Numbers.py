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
        dummy_head = ListNode(0)  # Fixed typo: listNode -> ListNode
        current_node = dummy_head
        carry = 0

        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            total_sum = value1 + value2 + carry
            carry = total_sum // 10
            out_digit = total_sum % 10

            # Fixed typos: current -> current_node
            current_node.next = ListNode(out_digit)
            current_node = current_node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next  # Fixed typo: dummy_dummy -> dummy_head
