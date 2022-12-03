def getDivisor(n):
    ans=[]
    l=int(n**0.5)
    for i in range(1,l+1):
        if n%i==0:
            ans.append(i)
            if i!=n//i: # //は切り捨て除算
                ans.append(n//i)
    ans.sort()
    return ans

n=int(input())
ans=getDivisor(n)
print(*ans)

# first my solution
# n=int(input())
# ans=[]
# m=int(n**0.5)
# for i in range(1,m+1):
#     if n%i==0:
#         ans.append(i)
#         j=int(n/i)
#         if j!=i:
#             ans.append(j)
# ans.sort()
# print(*ans)