class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = n + 1

        # best[i] = minimum length of a valid subarray
        # completely inside arr[0...i]
        best = [INF] * n

        left = 0
        curr_sum = 0
        ans = INF
        min_prev = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # If there is a previous non-overlapping subarray
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                # Store the best subarray seen up to 'right'
                min_prev = min(min_prev, length)

            # Best valid subarray ending anywhere up to right
            best[right] = min_prev

        return -1 if ans == INF else ans