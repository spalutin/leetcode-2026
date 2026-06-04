# [1] -> [1]
# [1, 2] -> [2]
# [1, 2, 3] -> [2, 3]
# [1, 2, 3, 4] -> [3, 4]
# [1, 2, 3, 4, 5] -> [3, 4, 5]
# [1, 2, 3, 4, 5, 6] -> [4, 5, 6]
from typing import Optional

from b_3_hare_tortoise.list_node import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
