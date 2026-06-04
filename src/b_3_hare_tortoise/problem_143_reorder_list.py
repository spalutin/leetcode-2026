"""
143. Reorder List
https://leetcode.com/problems/reorder-list/description/
"""
from typing import Optional

from b_3_hare_tortoise.list_node import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        tortoise = hare = head

        while hare.next and hare.next.next:
            hare = hare.next.next
            tortoise = tortoise.next

        tail = tortoise.next
        tortoise.next = None

        tortoise = None
        while tail:
            tmp = tail
            tail = tail.next
            tmp.next = tortoise
            tortoise = tmp

        hare = head

        while hare:
            tmp = hare.next
            hare.next = tortoise
            hare = tortoise
            tortoise = tmp
