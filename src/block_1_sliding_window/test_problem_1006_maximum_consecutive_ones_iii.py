from .problem_1006_maximum_consecutive_ones_iii import Solution

fixtures = [
    [[1], 0, 1],
    [[1, 0], 0, 1],
    [[1, 0], 1, 2],
    [[1, 0, 1], 1, 3],
    [[1, 0, 1], 2, 3],
    [[0, 1, 0], 1, 2],
    [[0, 1, 0], 2, 3],
    [[0, 1, 0, 1], 1, 3],
    [[0, 1, 0, 1], 2, 4],
    [[1, 0, 0, 1], 1, 2],
    [[1, 0, 0, 1], 2, 4],
    [[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6],
    [[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10]
]


def test_longest_ones():
    # print()
    for nums, k, expected in fixtures:
        # print(nums, k, expected)
        assert Solution().longestOnes(nums, k) == expected
