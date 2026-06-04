from .problem_3_longest_substring_without_repeating_characters import Solution

test_cases = [
    ['', 0],
    ['a', 1],
    ['bb', 1],
    ['bc', 2],
    ['ddd', 1],
    ['dee', 2],
    ['dde', 2],
    ['def', 3],
    ['gggg', 1],
    ['ghhh', 2],
    ['ghgh', 2],
    ['ghhi', 2],
    ['ghii', 3],
    ['gghi', 3],
    ['ghij', 4],
    ['ab cd', 5],
    ['abcabcbb', 3],
    ['bbbbb', 1],
    ['pwwkew', 3],
    ['tmmzuxt', 5],
]


def test_length_of_longest_substring():
    # print()
    for [s, expected] in test_cases:
        # print('solving "{s}" -> {expected}'.format(s=s, expected=expected))
        assert Solution().lengthOfLongestSubstring(s) == expected
