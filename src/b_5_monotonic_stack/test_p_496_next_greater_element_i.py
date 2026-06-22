from b_5_monotonic_stack.p_496_next_greater_element_i import Solution

fixtures: list[tuple[list[int], list[int], list[int]]] = [
    ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
    ([2, 4], [1, 2, 3, 4], [3, -1]),
]


def test_next_greater_element():
    for nums1, nums2, expected in fixtures:
        assert Solution().nextGreaterElement(nums1, nums2) == expected
