from typing import Optional

from block_3_hare_tortoise.list_node import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        should_move_slow = False
        while fast:
            fast = fast.next
            if slow and should_move_slow:
                slow = slow.next
            should_move_slow = not should_move_slow
            if fast == slow:
                return True
        return False
