class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_size = 0
        most_frequent = 0
        frequencies: dict[str, int] = dict()
        left, right = 0, 0

        for right in range(len(s)):
            y = s[right]

            if y not in frequencies:
                frequencies[y] = 0

            frequencies[y] += 1

            most_frequent = max(most_frequent, frequencies[y])

            if right - left - most_frequent >= k:
                frequencies[s[left]] -= 1
                left += 1

            max_size = max(max_size, right - left + 1)

        return max_size
