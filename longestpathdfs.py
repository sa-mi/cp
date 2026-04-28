import sys
from collections import defaultdict
input = sys.stdin.readline
n, m = [int(x) for x in input().split()]
edges = [(0,0)] * m
# key is outbound node, outbound to all vals
edgemap = defaultdict(list)
for i in range(m):
    x, y = [int(_) for _ in input().split()]
    edges[i] = (x, y)
    edgemap[x].append(y)

# dfs from every node, graph is acyclic so guranteed to end
# hashmap with key as source, value is longest path starting at source
memo = {}
def dfs(curnode):
    if curnode in memo:
        return memo[curnode]
    if not edgemap[curnode]:
        memo[curnode] = 0
        return memo[curnode]
    else:
        best = max([1 + dfs(neigh) for neigh in edgemap[curnode]])
        memo[curnode] = best
    return best

print(max([dfs(x) for x in range(1, n+1)]))

    