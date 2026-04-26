import sys
input = sys.stdin.readline

n, weight = [int(x) for x in input().split()]
weights, values = [0] * n, [0] * n
for i in range(n):
    weights[i], values[i] = [int(x) for x in input().split()]

# sum of taken weights must be <= w
# sum items taken <= n
# maximimize sum values


# need to keep track of total value and weight ending with having taken item i 
# dp[i][w] is the best possible value we can do with weight capacity?
dp = [[0 for _ in range(weight + 1)] for _ in range(n)]

for w in range(0, weight + 1):
    dp[0][w] = 0 if weights[0] > w else values[0]

for i in range(1, n):
    for w in range(0, weight + 1):
        if w - weights[i] < 0:
            # cannot take ith
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w - weights[i]] + values[i], dp[i-1][w])

        
print(dp[n-1][weight])