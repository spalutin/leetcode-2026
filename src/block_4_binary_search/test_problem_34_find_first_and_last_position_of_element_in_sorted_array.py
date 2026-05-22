from block_4_binary_search.problem_34_find_first_and_last_position_of_element_in_sorted_array import Solution

fixtures: list[tuple[list[int], int, list[int]]] = [
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
    ([], 0, [-1, -1]),
]


def test_search_range(debug=False):
    if debug: print()
    for nums, target, expected in fixtures:
        if debug: print(f'{nums}, {target} -> {expected}')
        assert Solution().searchRange(nums, target) == expected
