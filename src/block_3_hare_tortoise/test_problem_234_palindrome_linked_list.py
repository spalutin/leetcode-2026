from block_3_hare_tortoise.list_node import ListNode
from block_3_hare_tortoise.problem_234_palindrome_linked_list import Solution

fixtures: list[tuple[list[int], bool]] = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], False),
    ([1, 2, 3, 4, 5, 6, 7, 8], False),
    ([1], True),
    ([1, 1], True),
    ([1, 2], False),
    ([1, 2, 1], True),
    ([1, 2, 2], False),
    ([1, 2, 3], False),
    ([1, 1, 1, 1], True),
    ([1, 2, 2, 1], True),
    ([1, 2, 2, 2], False),
    ([1, 2, 3, 2, 1], True),
    ([1, 2, 3, 2, 4], False),
    ([1, 2, 3, 3, 2, 1], True),
]


def test_is_palindrome(debug=True):
    if debug: print()
    for xx, expected in fixtures:
        head = ListNode.from_list(xx)
        if debug: print(head, '=>', expected)
        assert Solution().isPalindrome(head) == expected
