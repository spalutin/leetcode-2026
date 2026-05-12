from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        str_next = self.next and ('->' + str(self.next)) or ''
        return str(self.val) + str_next

    @staticmethod
    def to_list(head: ListNode | None) -> list:
        if not head:
            return []
        return [head.val] + ListNode.to_list(head.next)

    @staticmethod
    def from_list(xx: List[int]) -> ListNode | None:
        if not xx:
            return None
        return ListNode(xx[0], ListNode.from_list(xx[1:]))


if __name__ == '__main__':
    lst = ListNode.from_list([1, 2, 3, 4, 5])
    print(lst)
    print(ListNode.to_list(lst))
