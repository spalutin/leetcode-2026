from typing import Optional

from b_3_hare_tortoise.list_node import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        zero = ListNode(-1)
        zero.next = head
        fast = slow = zero
        while n:
            fast = fast.next
            n -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return zero.next
