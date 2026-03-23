from .problem_567_permutation_in_string import Solution

fixtures = [
    ["adc", "dcda", True],
    ["ab", "eidbaooo", True],
    ["ab", "eidboaoo", False],
]


def test_check_inclusion():
    print()
    for [s1, s2, expected] in fixtures:
        print(s1, s2, expected)
        assert Solution().checkInclusion(s1, s2) == expected
