from block_2_two_pointers.problem_125_valid_palindrome import Solution

fixtures: list[tuple[str, bool]] = [
    (" ", True),
    ("aa", True),
    ("ab", False),
    ("A a", True),
    ("A 1B b1a", True),
    ("Xyx.", True),
    ("race a car", False),
    ("A man, a plan, a canal: Panama", True),
]


def test_is_palindrome(debug=False):
    for s, expected in fixtures:
        if debug:
            print()
            print(s, '->', expected)
        assert Solution().isPalindrome(s) == expected
