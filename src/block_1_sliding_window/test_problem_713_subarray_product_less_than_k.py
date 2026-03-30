from .problem_713_subarray_product_less_than_k import Solution

fixtures = [
    [[10, 5, 2, 6], 100, 8],
    [[1, 2, 3], 0, 0],
    [[1,2,3,4,5], 1, 0]
]


def test_num_subarray_product_less_than_k():
    # print()
    for nums, k, expected in fixtures:
        # print(nums, k, expected)
        assert Solution().numSubarrayProductLessThanK(nums, k) == expected
