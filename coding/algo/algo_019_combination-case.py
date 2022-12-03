# 実行時間1sのため、全探索はTLEとなる。組み合わせの総和から求める
n=int(input())
a=list(map(int,input().split()))
ans=0
cnt1=0
cnt2=0
cnt3=0
for i in range(0,n):
    if a[i]==1:
        cnt1+=1
    elif a[i]==2:
        cnt2+=1
    else:
        cnt3+=1
# 同じカードを2枚選ぶ場合の数
ans=cnt1*(cnt1-1)//2+cnt2*(cnt2-1)//2+cnt3*(cnt3-1)//2
print(ans)