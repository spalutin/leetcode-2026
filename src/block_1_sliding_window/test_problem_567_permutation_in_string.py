from problem_567_permutation_in_string import Solution

"""
s1 = "ab", s2 = "eidbaooo" -> True
s1 = "ab", s2 = "eidboaoo" -> False
"""
fixtures = [["ab", "eidbaooo", True], ["ab", "eidboaoo", False]]


def test_check_inclusion():
    print()
    for [s1, s2, expected] in fixtures:
        print(s1, s2, expected)
        assert Solution().checkInclusion(s1, s2) == expected
