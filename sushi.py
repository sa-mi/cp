import sys
input = sys.stdin.readline
n = int(input())
a = [int(x) for x in input().split()]

# count of plates with 1, 2, and 3 pieces respectively
c1, c2, c3 = 0, 0, 0
for i in range(n):
    if a[i] == 1:
        c1 += 1
    elif a[i] == 2:
        c2 += 1
    else:
        c3 += 1
# plates can range from 1 to 3 in size
# define dp[i][j][k] to be expected number of rolls left with i plates w/ 1 pieces and so on
# answer is dp[c1][c2][c3]
# iterate via k,j,i due to the recurrence

dp = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]

for k in range(n+1):
    for j in range(n+1):
        for i in range(n+1):
            # skip 0 case for division by zero
            if i == 0 and j == 0 and k == 0:
                continue
            # if there are more plates than possible
            if i + j + k > n:
                continue
            
            erolls = n
            
            if k > 0:
                erolls += k * dp[i][j+1][k-1]
            if j > 0:
                erolls += j * dp[i+1][j-1][k]
            if i > 0:
                erolls += i * dp[i-1][j][k]
            
            dp[i][j][k] = (erolls) / (i+j+k)

print(dp[c1][c2][c3])
            