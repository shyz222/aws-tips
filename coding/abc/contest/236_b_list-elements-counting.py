# 3枚しかないカード番号が答えになるので、数えていく
n=int(input())
a=list(map(int,input().split()))
cnt=[0]*(n+1)
for i in a:
    cnt[i]+=1
for i in range(0,n+1):
    if cnt[i]==3:
        print(i)

# other solution

# 4*(1+・・・+N)からaのlistの総和を引けばよい
# n=int(input())
# a=list(map(int,input().split()))
# print(2*n*(n+1)-sum(a))