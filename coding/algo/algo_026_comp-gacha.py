n=int(input())
ans=0
for i in range(1,n+1):
	ans+=1.0*n/i
# 小数点以下12桁まで出力
print("%.12f" % ans)

# 詳しい解説は下記
# https://manabitimes.jp/math/1053