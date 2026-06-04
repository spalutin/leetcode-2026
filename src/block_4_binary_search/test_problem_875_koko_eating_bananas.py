from block_4_binary_search.problem_875_koko_eating_bananas import Solution

fixtures: list[tuple[list[int], int, int]] = [
    ([3, 6, 7, 11], 8, 4),
    ([30, 11, 23, 4, 20], 5, 30),
    ([30, 11, 23, 4, 20], 6, 23),
]


def test_min_eating_speed(debug=False):
    if debug: print()
    for piles, h, expected in fixtures:
        if debug:
            print(f"Testing with piles={piles}, h={h}, expected={expected}")
        result = Solution().minEatingSpeed(piles, h)
        assert result == expected, f"Expected {expected}, got {result}"
