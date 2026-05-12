"""
143. Reorder List
https://leetcode.com/problems/reorder-list/description/
"""
from typing import Optional

from block_3_hare_tortoise.list_node import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        hercules = tortoise = ListNode(next=head)
        is_even = True

        while tortoise:
            is_even = not is_even
            tortoise = tortoise.next
            if is_even:
                hercules = hercules.next

        tail = hercules.next
        hercules.next = None
        tortoise = None

        while tail:
            hare = tail
            tail = tail.next
            hare.next = tortoise
            tortoise = hare

        hercules = head

        while hercules:
            hare = hercules.next
            hercules.next = tortoise
            hercules = tortoise
            tortoise = hare
