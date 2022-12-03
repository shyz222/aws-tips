n=int(input())
ans=[]
m=int(n**0.5)
for i in range(2,m+1):
    while n%i==0:
        n/=i
        ans.append(i)
if n>=2:
    ans.append(int(n))
print(*ans)
