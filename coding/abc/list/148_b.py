n=int(input())
s,t=map(str,input().split())
ans=[]
for i in range(0,n):
    ans.append(s[i])
    ans.append(t[i])
print(''.join(ans))