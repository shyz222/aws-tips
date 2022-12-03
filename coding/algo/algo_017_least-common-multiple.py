def getGcd(n,m):
    while n>=1 and m>=1:    # ユークリッドの互除法
        if n<m:
            m=m%n
        else:
            n=n%m
    if n>=1:
        return n
    return m

def getLcm(n,m):
    return int(n*m/getGcd(n,m))

n=int(input())
a=list(map(int,input().split()))
lcm=getLcm(a[0],a[1])
for i in range(2,n):
    lcm=getLcm(lcm,a[i])
print(lcm)