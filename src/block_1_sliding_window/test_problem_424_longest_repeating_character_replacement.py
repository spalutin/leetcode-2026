from .problem_424_longest_repeating_character_replacement import Solution

test_cases = [
    ["ABCDEDCBA", 1, 3],
    ["ABCDEDCBA", 0, 1],
    ["ABCDEDCBA", 2, 4],
    ["ABCDEDCBA", 3, 5],
    ["ABCBABCBA", 0, 1],
    ["ABCBACBA", 1, 3],
    ["ABCBACBA", 2, 4],
    ["ABCBACBA", 3, 6],
    ["ABAB", 2, 4],
    ["AABABBA", 1, 4],
    ["ABBB", 1, 4],
    ["BAAAB", 2, 5],
    ["A", 0, 1],
    ["A", 1, 1],
    ["AB", 0, 1],
    ["AB", 1, 2],
    ["AB", 2, 2],
    ["AA", 0, 2],
    ["AA", 1, 2],
    ["AA", 2, 2],
    ["ABC", 0, 1],
    ["ABC", 1, 2],
    ["ABC", 2, 3],
    ["ABC", 3, 3],
    ["AAB", 0, 2],
    ["AAB", 1, 3],
    ["ABA", 0, 1],
    ["ABA", 1, 3],
    ["ABA", 2, 3],
    ["ABB", 0, 2],
    ["ABB", 1, 3],
    ["ABB", 2, 3],
]


def test_character_replacement():
    # print()
    for [s, k, expected] in test_cases:
        # print('solving "{s}", {k} -> {expected}'.format(s=s, k=k, expected=expected))
        assert Solution().characterReplacement(s, k) == expected
