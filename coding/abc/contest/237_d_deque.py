from collections import deque

n=int(input())
s=list(input())
ans=deque([n])
for i in reversed(range(0,n)):
    if s[i]=="L":
        ans.append(i)
    else:
        ans.appendleft(i)
print(*ans)

# ans=deque(n)だと、type errorになってしまうので注意。Iterable[int]で入れるよう定義に記載あり。

# deque(両端キュー)とは
# Pythonのコンテナデータ型の１種。
# データの追加を先頭、末尾両方に対してO(1)のコストで実施できる。
# 通常のlistだと先頭に追加する場合にO(n)のコストで実施できる。

# TLE
# n=int(input())
# s=list(input())
# ans=[]
# ans.append(n)
# for i in reversed(range(0,n)):
#     if s[i]=="L":
#         ans.append(i)
#     else:
#         ans.insert(0,i)   # listだと先頭に入れる際に計算量がO(n)となってしまう
# print(*ans)

# TLE
# n=int(input()) 
# s=list(input())
# a=[]
# a.append(0)
# for i in range(1,n+1):
#     m=a.index(i-1)
#     if s[i-1]=="L":
#         a.insert(m,i)
#     else:
#         a.insert(m+1,i)
# print(*a)