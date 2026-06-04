from b_3_hare_tortoise.problem_287_find_the_duplicate_number import Solution

fixtures: list[tuple[list[int], int]] = [
    ([1, 1], 1),
    ([1, 1, 2], 1),
    ([1, 2, 1], 1),
    ([1, 2, 2], 2),
    ([2, 2, 2], 2),
    ([1, 2, 3, 3], 3),
    ([1, 2, 3, 2], 2),
    ([1, 3, 4, 2, 2], 2),
    ([3, 1, 3, 4, 2], 3),
    ([3, 3, 3, 3, 3], 3),
]


def test_find_duplicate():
    for nums, expected in fixtures:
        assert expected == Solution().findDuplicate(nums)
