# OK
h,w=map(int,input().split()) 
a=[list(map(int,input().split())) for _ in range(h)]
ans = []
for i in range(w):
    ans_row = []
    for j in a:
        ans_row.append(j[i])
    ans.append(ans_row)    
for i in range(w):
    print(*ans[i])

# import numpy as np
# import sys
# sys.stdin.readline()
# A = np.loadtxt(sys.stdin, dtype=int, ndmin=2)
# np.savetxt(sys.stdout, A.T, fmt='%d')