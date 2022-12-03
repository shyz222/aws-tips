# 組み合わせの総和から求める
n=int(input())
a=list(map(int,input().split()))

# 0-99999の箱を用意
# （0の箱も作っているが1<=a<=99999なので0の箱をカウントアップするパターンはない）
cnt = [0 for i in range(100000)]
# 箱の番号と一致するaの値があれば、カウントアップ
for i in range(n):
    cnt[a[i]]+=1
ans=0
for i in range(1,50000):            # 1-49999まで
    ans+=cnt[i]*cnt[100000-i]       # (1,99999)-(49999,50001)の組み合わせの総和を求める
ans+=cnt[50000]*(cnt[50000]-1)//2   # (50000,50000)の組み合わせを求める
print(ans)

# TLE
# n=int(input())
# a=list(map(int,input().split()))
# ans=0
# for i in range(0,n):
#     for j in range(i+1,n):  
#         if a[i]+a[j]==100000:
#             ans+=1
# print(ans)