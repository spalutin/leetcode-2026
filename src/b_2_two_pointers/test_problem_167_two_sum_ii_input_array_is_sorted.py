from b_2_two_pointers.problem_167_two_sum_ii_input_array_is_sorted import Solution

fixtures: list[tuple[list[int], int, list[int]]] = [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2]),
]


def test_solution(debug=False):
    for numbers, target, expected in fixtures:
        if debug:
            print()
            print(numbers, target, '->', expected)
        assert Solution().twoSum(numbers, target) == expected
