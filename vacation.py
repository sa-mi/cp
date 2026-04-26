# n days, 3 arrays a, b, c, max possible happiness, cannot pick from two arrays twice in a row
import sys
input = sys.stdin.readline
n = int(input())
a, b, c = [0] * n, [0] * n, [0] * n
for i in range(n):
    ai, bi, ci = [int(x) for x in input().split()]
    a[i], b[i], c[i] = ai, bi, ci

# dp[i][a] represents the max happiness on the ith day given we took a[i]
# let a = 0, b = 1, c = 2
dp = [[0 for _ in range(3)] for _ in range(n)]
dp[0][0], dp[0][1], dp[0][2] = a[0], b[0], c[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a[i]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + b[i]
    dp[i][2] = max(dp[i-1][1], dp[i-1][0]) + c[i]

print(max(dp[n-1]))
