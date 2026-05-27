from block_4_binary_search.problem_33_search_in_rotated_sorted_array import Solution

fixtures: list[tuple[list[int], int, int]] = [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([1], 0, -1),
]


def test_search(debug=False):
    if debug: print()
    for nums, target, expected in fixtures:
        if debug: print(f'{nums}, {target} -> {expected}')
        assert Solution().search(nums, target) == expected
