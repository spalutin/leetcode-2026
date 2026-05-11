from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        str_next = self.next and (' -> ' + str(self.next)) or ''
        return str(self.val) + str_next

    @staticmethod
    def from_list(xx: List[int]) -> ListNode | None:
        if not xx:
            return None

        head = ListNode(xx[0])
        head.next = ListNode.from_list(xx[1:])

        return head


if __name__ == '__main__':
    lst = ListNode.from_list([1, 2, 3, 4, 5])
    print(lst)
