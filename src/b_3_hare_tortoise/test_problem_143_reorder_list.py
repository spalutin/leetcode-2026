from b_3_hare_tortoise.list_node import ListNode
from b_3_hare_tortoise.problem_143_reorder_list import Solution

fixtures = [
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([1, 2, 3], [1, 3, 2]),
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
    ([1, 2, 3, 4, 5, 6, 7], [1, 7, 2, 6, 3, 5, 4]),
    ([1, 2, 3, 4, 5, 6, 7, 8], [1, 8, 2, 7, 3, 6, 4, 5]),
]


def test_reorder_list(debug=False):
    if debug: print()
    for fixture, expected in fixtures:
        if debug: print(fixture, '->', expected)
        head = ListNode.from_list(fixture)
        Solution().reorderList(head)
        assert ListNode.to_list(head) == expected
