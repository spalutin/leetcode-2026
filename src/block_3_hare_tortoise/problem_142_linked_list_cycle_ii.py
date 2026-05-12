from typing import Optional

from block_3_hare_tortoise.list_node import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        else:
            return None

        fast = head
        while slow and fast and fast.next:
            fast = fast.next
            slow = slow.next
            if slow == fast:
                break
        return slow
