n,x=map(int,input().split())
a=map(int,input().split())
ans=[i for i in a if i != x]
# ans=list(filter((x).__ne__, a))
print(*ans)