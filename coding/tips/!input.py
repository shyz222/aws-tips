#######
# 1*1 #
#######
# str型で受け取るとき
s=input() 
# int型で受け取るとき
s=int(input()) 
# float型(小数)で受け取るとき
s=float(input())

#######
# 1*n #
#######
# list型で受け取るとき
s=input().split()
# 文字列として複数個受け取るとき
a,b,c=input().split()
# 整数として複数個受け取るとき
a,b=map(int,input().split())
# 文字列と数字の複合
n,s=map(str,input().split())
# list型でn個を整数として受け取るとき
l=list(map(int,input().split()))

#######
# n*1 #
#######
# 空のリストを生成して上から順にリストへ格納することで、(N,1)行列を(1,N)行列に変換する
n=int(input())
a=[int(input()) for _ in range(n)]    # リスト内包表記

#######
# n*m #
#######
# N
# x1 x2 x3 .. xN
# y1 y2 y3 .. yN
n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
# N
# x1 y1
# x2 y2
# :
# xN yN
# x,yを独立に格納
n=int(input())
xy=[map(int,input().split()) for _ in range(n)]
x, y = [list(_) for _ in zip(*xy)]
# [xi,yi]として格納
n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
# int,str混合
n=int(input())
list=[]
for i in range(n):
    a,b=input().split()
    list.append([int(a), b])
