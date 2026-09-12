class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        import bisect

        n = len(intervals)

        # Store: (start, end, weight, original_index)
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort by starting point
        arr.sort()

        starts = [x[0] for x in arr]

        # next_idx[i] = first interval whose start > arr[i].end
        next_idx = [0] * n

        for i in range(n):
            r = arr[i][1]
            next_idx[i] = bisect.bisect_right(starts, r)

        # dp[i][k] = (maximum score using intervals from i onward,
        #             lexicographically smallest indices achieving it)
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l, r, w, idx = arr[i]
            nxt = next_idx[i]

            for k in range(1, 5):

                # Option 1: Don't take this interval
                skip_score, skip_indices = dp[i + 1][k]

                # Option 2: Take this interval
                take_score, take_indices = dp[nxt][k - 1]

                take_score += w
                take_indices = tuple(sorted((idx,) + take_indices))

                # Choose better score
                if take_score > skip_score:
                    dp[i][k] = (take_score, take_indices)

                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_indices)

                else:
                    # Same score -> lexicographically smaller indices
                    if take_indices < skip_indices:
                        dp[i][k] = (take_score, take_indices)
                    else:
                        dp[i][k] = (skip_score, skip_indices)

        return list(dp[0][4][1])