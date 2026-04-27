from .problem_11_container_with_most_water import Solution

fixtures = [
    [[1, 9, 6, 2, 5, 4, 8, 3, 7], 49],
    [[1, 1], 1],
    [[1, 2, 1, 1, 15, 15, 1, 1, 2, 1], 15]
]


def test_max_area():
    for heights, expected in fixtures:
        assert Solution().maxArea(heights) == expected
