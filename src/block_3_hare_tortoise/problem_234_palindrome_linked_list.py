"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/description/
"""
from typing import Optional

from block_3_hare_tortoise.list_node import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        tortoise = hare = head

        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next

        is_even = not hare

        hare = None
        while head != tortoise:
            tmp = head.next
            head.next = hare
            hare = head
            head = tmp

        if not is_even:
            tortoise = tortoise.next

        while tortoise and hare:
            if hare.val != tortoise.val:
                return False
            tortoise = tortoise.next
            hare = hare.next

        return True
