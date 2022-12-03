def isPrime(n):
    m=int(n**0.5)   # intをつけることで少数を切り捨てて整数化できる。ex)7.33→7
    for i in range(2,m+1):
        if n%i==0:  # ここはn%iなの注意。m%iじゃない。
            return False
    return True

n=int(input())
ans="Yes"
if isPrime(n)==False:
    ans="No"
print(ans)