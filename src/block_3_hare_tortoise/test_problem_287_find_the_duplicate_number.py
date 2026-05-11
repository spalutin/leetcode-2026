from block_3_hare_tortoise.problem_287_find_the_duplicate_number import Solution

fixtures: list[tuple[list[int], int]] = [
    ([0, 1, 2, 2], 2),
    ([0, 1, 2, 1], 1),
    ([0, 0], 0),
    ([0, 0, 1], 0),
    ([0, 1, 1], 1),
    ([0, 1, 0], 0),
    ([1, 1, 1], 1),
    ([1, 3, 4, 2, 2], 2),
    ([3, 1, 3, 4, 2], 3),
    ([3, 3, 3, 3, 3], 3),
]


def test_find_duplicate():
    for nums, expected in fixtures:
        assert expected == Solution().findDuplicate(nums)
