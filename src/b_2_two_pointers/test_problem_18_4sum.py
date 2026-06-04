from b_2_two_pointers.problem_18_4sum import Solution

fixtures: list[tuple[list[int], int, list[list[int]]]] = [
    ([-3, -1, 0, 2, 4, 5], 2, [[-3, -1, 2, 4]]),
    ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
    ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
]


def test_four_sum(debug=False):
    for nums, target, expected in fixtures:
        if debug: print()
        if debug: print(nums, target, '->', expected)
        assert sorted(sorted(xx) for xx in Solution().fourSum(nums, target)) == sorted(sorted(xx) for xx in expected)
