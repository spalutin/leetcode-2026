from b_2_two_pointers.problem_16_3sum_closest import Solution

fixtures = [
    [[-1, 2, 1, -4], 1, 2],
    [[0, 0, 0], 1, 0]
]


def test_three_sum_closest(debug=False):
    for nums, target, expected in fixtures:
        if debug: print()
        if debug: print(nums, '->', expected)
        assert Solution().threeSumClosest(nums, target) == expected
