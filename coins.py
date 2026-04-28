import sys
input = sys.stdin.readline
n = int(input())
prob = [0] * n
prob =[float(x) for x in input().split()]

dp = [[0 for _ in range(n + 1)] for _ in range(n+1)]
# define dp[i]][j] to be prob of exactly j heads in the first i coins
dp[0][0] = 1
dp[0][1] = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i][j-1] += (1 - prob[i-1]) * dp[i-1][j-1]
        dp[i][j] += prob[i-1] * dp[i-1][j-1]
total = 0
for j in range(n+1):
    if j > n//2:
        total += dp[n][j]
print(total)
