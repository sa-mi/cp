import sys
import os
import math
def solve():
    if os.path.exists('sampleinput.txt'):
        sys.stdin = open('sampleinput.txt', 'r')
    inputdata = sys.stdin.read().split('\n')
    # print(inputdata)
    numtests = inputdata[0]
    inputdata.pop(0)
    for i in range(len(numtests)):
        n = inputdata[0].split(" ")[0]
        k = inputdata[0].split(" ")[1]
        inputdata.pop(0)
        q = inputdata[0]
        inputdata.pop(0)
        r = inputdata[0]
        inputdata.pop(0)

        # we seek x, y s.t y = q_i * x + r_j for 1 < x,y < k
        # notice r_j < x
        # does it matter which r_j and q_i we use?
        





solve()
