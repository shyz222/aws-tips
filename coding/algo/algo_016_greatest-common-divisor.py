def getGcd(n,m):
    while n>=1 and m>=1:    # ユークリッドの互除法
        if n<m:
            m=m%n
        else:
            n=n%m
    if n>=1:
        return n
    return m

n=int(input())
a=list(map(int,input().split()))
ans=getGcd(a[0],a[1])
for i in range(2,n):
    ans=getGcd(ans,a[i])
print(ans)