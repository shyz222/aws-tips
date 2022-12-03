def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n=int(input())
ans=[]
for i in range(2,n+1):
    if isPrime(i)==True:
        ans.append(i)
print(*ans) # *を付けない場合[n,n,n,n]の形で出力。*を付けた場合n n n nの形で出力。アンパックというらしい。