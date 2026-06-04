from .problem_1011_capacity_to_ship_packages_within_d_days import Solution

fixtures = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
    ([3, 2, 2, 4, 1, 4], 3, 6),
    ([1, 2, 3, 1, 1], 4, 3),
]


def test_ship_within_days(debug=False):
    if debug: print()
    for weights, days, expected in fixtures:
        if debug:
            print(f"weights={weights}, days={days}, expected={expected}")
        assert Solution().shipWithinDays(weights, days) == expected
