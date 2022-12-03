n=int(input())
pq=[map(int,input().split()) for _ in range(n)]
p, q = [list(_) for _ in zip(*pq)]
ans=0
for i in range(n):
    ans+=q[i]/p[i]
print(ans)