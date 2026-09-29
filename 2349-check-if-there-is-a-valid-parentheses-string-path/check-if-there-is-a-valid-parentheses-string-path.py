class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Length of every path must be even
        if (m + n - 1) % 2 != 0:
            return False

        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        # dp[i][j] stores possible balances at cell (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                # Get possible balances from top and left
                prev = set()

                if i > 0:
                    prev |= dp[i-1][j]

                if j > 0:
                    prev |= dp[i][j-1]

                # Process current bracket
                for balance in prev:
                    if grid[i][j] == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1

                    # Balance cannot become negative
                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

        return 0 in dp[m-1][n-1]