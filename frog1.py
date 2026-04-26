import sys
input = sys.stdin.readline
nandk = [int(x) for x in input().split()]
n, k = nandk[0], nandk[1]
h = [int(x) for x in input().split()]

dp = [0] * n
dp[0] = 0
dp[1] = abs(h[1] - h[0])
for i in range(2, n):
    dp[i] = min([abs(h[j] - h[i]) + dp[j] for j in range(max(0, i-k),i)])
       
print(dp[n-1])
