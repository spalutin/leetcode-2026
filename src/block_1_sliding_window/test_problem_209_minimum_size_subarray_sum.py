from .problem_209_minimum_size_subarray_sum import Solution

fixtures = [
    [7, [2, 3, 1, 2, 4, 3], 2],
    [4, [1, 4, 4], 1],
    [11, [1, 1, 1, 1, 1, 1, 1, 1], 0],

]


def test_min_sub_array_len():
    # print()
    for target, nums, expected in fixtures:
        # print(target, nums, expected)
        assert Solution().minSubArrayLen(target, nums) == expected
