class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # @todo solve again
        size = len(s)

        max_size = 0
        sizes: dict[str, int] = dict()
        left, right = 0, 0

        while right < size:
            y = s[right]
            if y not in sizes:
                sizes[y] = k
            sizes[y] += 1

            max_size = max(max_size, sizes[y])

            while right - left >= max_size:
                x = s[left]
                sizes[x] -= 1
                left += 1

            right += 1

        return min(size, max_size)
