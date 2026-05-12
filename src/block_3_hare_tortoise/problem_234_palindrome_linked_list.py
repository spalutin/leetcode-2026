"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/description/
"""
from typing import Optional

from block_3_hare_tortoise.list_node import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        tortoise = hare = head
        meet = []
        while hare and hare.next:
            hare = hare.next.next
            meet.append(tortoise.val)
            tortoise = tortoise.next

        if hare:
            tortoise = tortoise.next

        while tortoise:
            if tortoise.val != meet.pop():
                return False
            tortoise = tortoise.next

        return True
