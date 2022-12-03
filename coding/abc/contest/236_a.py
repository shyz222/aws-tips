from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES


s=list(input())
a,b=map(int,input().split())
a-=1
b-=1
s[a],s[b]=s[b],s[a]
ans="".join(s)
print(ans)

# listの文字列を連結させて出力するには、ans="".join(s)