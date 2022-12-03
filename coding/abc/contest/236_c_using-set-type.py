n,m=map(int,input().split())
s=list(map(str,input().split()))
t=set(map(str,input().split()))
for i in s:
    print("Yes" if i in t else "No")

# set型を用いることで、if i in t部分の計算量をO(1)にできる
# list型だと、if i in t部分の計算量がO(m)になってしまいTLE
# set型は重複しない要素（同じ値ではない要素、ユニークな要素）のコレクションで、和集合、積集合、差集合などの集合演算を行うことができる
# set型は順序をもたないので、生成時の順序は記憶されない

# TLE
# n,m=map(int,input().split())
# s=list(map(str,input().split()))
# t=list(map(str,input().split()))
# for i in s:
#     print("Yes" if i in t else "No")

# TLE １つ上と同義のコード
# n,m=map(int,input().split())
# s=list(map(str,input().split()))
# t=list(map(str,input().split()))
# ans=[]
# for i in s:
#     if i in t:
#         ans.append("Yes")
#     else:
#         ans.append("No")
# ans="\n".join(ans)
# print(ans)