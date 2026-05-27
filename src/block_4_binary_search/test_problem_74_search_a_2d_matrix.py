from block_4_binary_search.problem_74_search_a_2d_matrix import Solution

fixtures: list[tuple[list[list[int]], int, bool]] = [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
]


def test_search_matrix(debug=False):
    if debug: print()
    for matrix, target, expected in fixtures:
        print(matrix, target, '->', expected)
        result = Solution().searchMatrix(matrix, target)
        assert result == expected
