from b_5_monotonic_stack.p_503_next_greater_element_ii import Solution

fixtures = [
    ([1, 2, 1], [2, -1, 2]),
    ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4])
]


def test_solution():
    for nums, expected in fixtures:
        assert Solution().nextGreaterElements(nums) == expected
