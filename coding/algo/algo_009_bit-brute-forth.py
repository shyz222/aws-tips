n,s=map(int,input().split())
a=list(map(int,input().split()))
ans="No"

# bit全探索
for i in range(0,1<<n):     # 1<<nは2のn乗
    sum=0
    for j in range(0,n):
		# (i&(1<<j))!=0の場合、iの2進法表記の下からj+1桁目が1
		# 1<<jは2のj乗
        if (i&(1<<j))!=0:   # iの2進数表記と2のj乗の2進数表記の論理積が0でないとき。つまりiの2進数表記のどこかに1がある場合
            sum+=a[j]       # sumはiの2進数表記がで1になっていたカードの総和
    if sum==s:
        ans="Yes"
        break
        
print(ans)

# 動的計画法での解放は3.7節を解く際に実施する