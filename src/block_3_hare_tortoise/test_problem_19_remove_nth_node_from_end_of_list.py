from .list_node import ListNode
from .problem_19_remove_nth_node_from_end_of_list import Solution

fixtures: list[tuple[list[int], int, list[int]]] = [
    ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ([1], 1, []),
    ([1, 2], 1, [1]),
]


def test_remove_nth_from_end(debug=False):
    if debug: print()
    for xx, n, expected in fixtures:
        if debug: print(xx, n, '->', expected)
        head = ListNode.from_list(xx)
        actual = Solution().removeNthFromEnd(head, n)
        assert ListNode.to_list(actual) == expected
