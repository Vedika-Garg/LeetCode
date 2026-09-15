class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # Manacher: odd length palindromes
        d1 = [0] * n
        l = 0
        r = -1

        for i in range(n):
            if i > r:
                j = 1
            else:
                j = min(d1[l + r - i], r - i + 1)

            while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
                j += 1

            d1[i] = j

            if i + j - 1 > r:
                l = i - j + 1
                r = i + j - 1

        # Manacher: even length palindromes
        d2 = [0] * n
        l = 0
        r = -1

        for i in range(n):
            if i > r:
                j = 0
            else:
                j = min(d2[l + r - i + 1], r - i + 1)

            while i - j - 1 >= 0 and i + j < n and s[i - j - 1] == s[i + j]:
                j += 1

            d2[i] = j

            if i + j - 1 > r:
                l = i - j
                r = i + j - 1

        # dp[i] = max palindromes using s[0:i]
        dp = [0] * (n + 1)

        for end in range(n):
            # Don't select a palindrome ending at end
            dp[end + 1] = dp[end]

            for start in range(end + 1):
                length = end - start + 1

                if length < k:
                    continue

                # Check palindrome using Manacher
                if length % 2 == 1:
                    center = (start + end) // 2
                    radius = length // 2 + 1

                    if d1[center] >= radius:
                        dp[end + 1] = max(dp[end + 1], dp[start] + 1)

                else:
                    center = (start + end + 1) // 2
                    radius = length // 2

                    if d2[center] >= radius:
                        dp[end + 1] = max(dp[end + 1], dp[start] + 1)

        return dp[n]