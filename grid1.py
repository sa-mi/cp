import sys
input = sys.stdin.readline
m, n = [int(x) for x in input().split()]
grid = [0 for _ in range(m)]
for i in range(m):
    row = [str(x) for x in input().strip()]
    grid[i] = row
# num of ways from 0,0 to (m-1,n-1)
# 2d dp array, dp[i][j] is num ways to reach i, j
dp = [[0 for _ in range(n)] for _ in range(m)]
dp[0][0] = 1
for i in range(m):
    for j in range(n):
        if i + 1 < m and grid[i+1][j] != '#':
            dp[i+1][j] +=  dp[i][j]
        if j + 1 < n and grid[i][j + 1] != '#':
            dp[i][j + 1] += dp[i][j]
print(dp[m-1][n-1] % (10**9+7))