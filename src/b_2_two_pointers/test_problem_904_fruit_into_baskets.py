from b_2_two_pointers.problem_904_fruit_into_baskets import Solution

fixtures: list[tuple[list[int], int]] = [
    ([0], 1),
    ([0, 0], 2),
    ([0, 1], 2),
    ([0, 0, 1], 3),
    ([0, 1, 0], 3),
    ([0, 1, 1], 3),
    ([1, 2, 1], 3),
    ([0, 1, 2, 2], 3),
    ([1, 2, 3, 2, 2], 4),
    ([1, 0, 1, 4, 1, 4, 1, 2, 3], 5),
    ([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5),
]


def test_solution(debug=True):
    if debug: print()

    for fruits, expected in fixtures:
        if debug: print(fruits, '->', expected)
        assert Solution().totalFruit(fruits) == expected
