from b_4_binary_search.problem_35_search_insert_position import Solution

fixtures: list[tuple[list[int], int, int]] = [
    ([1, 3, 5, 6], 0, 0),
    ([1, 3, 5, 6], 1, 0),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 3, 1),
    ([1, 3, 5, 6], 4, 2),
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 6, 3),
    ([1, 3, 5, 6], 7, 4),
]


def test_search_insert(debug=False):
    if debug: print()
    for nums, target, expected in fixtures:
        if debug: print(f'{nums}, {target} -> {expected}')
        assert Solution().searchInsert(nums, target) == expected
