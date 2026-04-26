import sys
input = sys.stdin.readline
s = str(input().strip())
t = str(input().strip())
m, n = len(s), len(t)

# longest common subsequence of s and t
# can del chars from s and t

# dp[i][j] can be the lcs with the first i of s and j of t
# dp[0][0] is 1 if their first two chars match, 0 else
# dp[i][j] = dp[i-1][j-1] + 1 if s[i] == t[j] else dp[i-1][j-1]
dp = [["" for _ in range(n)] for _ in range(m)]
dp[0][0] = s[0] if s[0] == t[0] else ""
for j in range(n):

    dp[0][j] = str(t[j]) if s[0] == t[j] else str(dp[0][j-1])
for i in range(m):
    dp[i][0] = str(s[i]) if t[0] == s[i] else str(dp[i-1][0])

for i in range(m):
    for j in range(n):
        dp[i][j] = str(dp[i-1][j-1]) + s[i] if s[i] == t[j] else str(max(dp[i-1][j], dp[i][j-1], key=len))
print(str(dp[m-1][n-1]))