# longest path in dag via kahns
# use bfs, enqueue nodes with indegree 0
from collections import defaultdict, deque
import sys
n, m = [int(x) for x in input().split()]
indegree = [0] * (n + 1)

# key is outbound node, outbound to all vals
edgemap = defaultdict(list)
for i in range(m):
    x, y = [int(_) for _ in input().split()]
    edgemap[x].append(y)
    indegree[y] += 1
dq = deque([])

# enqueue all source nodes
for i in range(1, n+1):
    if indegree[i] == 0:
        dq.append(i)
        
# dp array, dp[i] is longest path endingx at i
dp = [0] * (n + 1)

while dq:
    cur = dq.popleft()
    for neigh in edgemap[cur]:
        dp[neigh] = max(dp[neigh], dp[cur] + 1)
        indegree[neigh] -= 1
        if indegree[neigh] == 0:
            dq.append(neigh)

print(max(dp))

