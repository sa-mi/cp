import sys
import math
import os
def solve():
    if os.path.exists('input.txt'):
        sys.stdin = open('input.txt', 'r')
    inputdata = sys.stdin.read().split('\n')
    inputdata.pop()
    if not inputdata:
        return
    n = int(inputdata[0])
    inputdata = inputdata[1:]
    cost = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        #print(f'{i} node: {inputdata[i]}')
        pricefloor = int(inputdata[i][2])
        for j in range(n):
            dist = int(inputdata[j][0]) - int(inputdata[i][0])
            cost[i][j] = max(pricefloor, dist)
            cost[i][i] = float('inf')
    
    
    # wish to find cheapest hamiltonian cycle starting at node 0 in weighted directional complete graph
    # bitmask dp? mark 1 if visited 0 else, path of len n-1, if all 1 AND we are at node 0 then we have finished a cycle
solve()