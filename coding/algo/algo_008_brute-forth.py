n,s=map(int,input().split())
c=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j<=s:
            c+=1
print(c)