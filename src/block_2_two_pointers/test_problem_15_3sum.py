from .problem_15_3sum import Solution

fixtures = [
    [[-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]],
    [[0, 1, 1], []],
    [[0, 0, 0], [[0, 0, 0]]],

    [[-1, 0, 1], [[-1, 0, 1]]],
    [[1, 2, -2, -1], []],
    [[-1, 0, 1, 0], [[-1, 0, 1]]],
]


def test_three_sum(debug=True):
    for [nums, expected] in fixtures:
        if debug: print()
        if debug: print(nums, '->', expected)
        assert sorted(sorted(xx) for xx in Solution().threeSum(nums)) == sorted(sorted(xx) for xx in expected)
