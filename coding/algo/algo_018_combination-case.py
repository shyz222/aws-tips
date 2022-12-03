n=int(input())
a=list(map(int,input().split()))
ans=0
# 合計500円になる組み合わせは(100,400)(200,300)の2通りのみなので、それらをパターンを考える
cnt1=0
cnt2=0
cnt3=0
cnt4=0
for i in range(0,n):
    if a[i]==100:
        cnt1+=1
    elif a[i]==200:
        cnt2+=1
    elif a[i]==300:
        cnt3+=1
    else:
        cnt4+=1
ans=cnt1*cnt4+cnt2*cnt3
print(ans)

# 実行時間1sに対し、2<=n<=200000なので全探索O(n^2)はTLEとなりダメ
# 1秒間に処理できるfor文ループ回数は10**8が目安

# n=int(input())
# a=list(map(int,input().split()))
# ans=0
# for i in range(0,n):
#     for j in range(i+1,n):
#         if a[i]+a[j]==500:
#             ans+=1
# print(ans)