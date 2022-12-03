def getGcd(n,m):
    while n>=1 and m>=1:    # ユークリッドの互除法
        if n<m:
            m=m%n
        else:
            n=n%m
    if n>=1:
        return n
    return m

a,b=map(int,input().split())
print(getGcd(a,b))