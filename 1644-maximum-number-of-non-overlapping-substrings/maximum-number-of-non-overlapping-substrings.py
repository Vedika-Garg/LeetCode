class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        # First and last occurrence of each character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Find the smallest valid interval starting at each character's first occurrence
        for c in range(26):
            if first[c] == n:
                continue

            l = first[c]
            r = last[c]
            i = l
            valid = True

            while i <= r:
                idx = ord(s[i]) - ord('a')

                # This character appeared before l,
                # so we cannot make a valid substring starting at l.
                if first[idx] < l:
                    valid = False
                    break

                # Include all occurrences of this character
                r = max(r, last[idx])
                i += 1

            if valid:
                intervals.append((l, r))

        # Take intervals in increasing order of their ending position
        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for l, r in intervals:
            if l > prev_end:
                ans.append(s[l:r + 1])
                prev_end = r

        return ans