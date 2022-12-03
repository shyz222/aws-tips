s=input()
n=len(s)
l=0
r=n-1
while l<r and s[l]==s[r]=="a":
    l+=1
    r-=1
while l<r and s[r]=="a":
    r-=1
while l<r and s[l]==s[r]:
    l+=1
    r-=1
if l>=r:
    print("Yes")
else:
    print("No")


# 回文判定方法
# 解1)文字列リバースして一緒かどうか
# 解2)先頭(l)と末端(r)にカーソル用意して判定

# 今回の考え方
# 解2)を用いてかつ計算量が少なくなるよう実装する
# 1)l<rかつ両端がaならlとrを進める
# 2)l<rかつ末端がaならrを進める
# 3)l<rかつ両端が同じならlとrを進める
# 4)3)を続けていきl>=rとなればYes。l<rであればNo


# TLE
# s=list(input())
# n=len(s)
# ans="No"
# flag=1

# for j in range(n//2+1):
#     if s[j]!=s[n-j-1]:
#         flag=0
# if flag==1:
#     ans="Yes"

# flag=1
# for i in range(n):
#     s.insert(0,"a")
#     n+=1
#     for j in range(n//2+1):
#         if s[j]!=s[n-j-1]:
#             flag=0
#     if flag==1:
#         ans="Yes"
#         break
# print(ans)