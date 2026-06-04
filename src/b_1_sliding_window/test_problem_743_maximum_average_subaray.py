from .problem_743_maximum_average_subaray import Solution

fixtures = [
    [[1, 12, -5, -6, 50, 3], 4, 12.75000],
    [[5], 1, 5.0],
]


def test_find_max_average():
    # print()
    for nums, k, expected in fixtures:
        # print(nums, k, expected)
        assert round(Solution().findMaxAverage(nums, k), 5) == round(expected, 5)
