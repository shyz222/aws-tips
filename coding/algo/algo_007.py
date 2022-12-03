n,x,y=map(int,input().split())
c=0
for i in range(1,n+1):
    if i % x ==0 or i % y==0:
        c+=1
print(c)