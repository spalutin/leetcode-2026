from b_2_two_pointers.problem_344_reverse_string import Solution

fixtures = [
    [["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]],
    [["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]],
]


def test_solution():
    for s, expected in fixtures:
        Solution().reverseString(s)
        assert s == expected
