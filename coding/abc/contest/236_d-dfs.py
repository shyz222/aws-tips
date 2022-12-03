import sys
sys.setrecursionlimit(10**6)    # pythonの再起呼び出し上限を1000(デフォルト)→10**6に変更

n = int(input())
a = [list(map(int, input().split())) for _ in range(2 * n - 1)]
used = [False] * (2 * n)
ans = 0

def dfs(i, tot):
    if i == n:
        global ans
        ans = max(ans, tot)
        return
    for j in range(2 * n):
        if not used[j]:
            used[j] = True
            break
    for k in range(j + 1, 2 * n):
        if not used[k]:
            used[k] = True
            dfs(i + 1, tot ^ a[j][k - j - 1])
            used[k] = False
    used[j] = False 


dfs(0, 0)
print(ans)

# explanation
# https://atcoder.jp/contests/abc236/editorial/3285
