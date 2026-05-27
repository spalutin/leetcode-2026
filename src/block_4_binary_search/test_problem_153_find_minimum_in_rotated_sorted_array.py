from block_4_binary_search.problem_153_find_minimum_in_rotated_sorted_array import Solution

fixtures: list[tuple[list[int], int]] = [
    ([1], 1),
    ([1, 2], 1),
    ([2, 1], 1),
    ([1, 2, 3], 1),
    ([4, 2, 3], 2),
    ([4, 5, 3], 3),
    ([1, 2, 3, 4], 1),
    ([8, 5, 6, 7], 5),
    ([11, 12, 9, 10], 9),
    ([14, 15, 16, 13], 13),
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([11, 13, 15, 17], 11),
]


def test_find_min(debug=False):
    for nums, expected in fixtures:
        if debug: print(f'{nums} -> {expected}')
        assert Solution().findMin(nums) == expected
