# 両端キュー
from collections import deque

# 階乗取得
def getFactorial(x):
    r=1
    for x in range(1,x+1):
        r*=x
    return r

# 素数判定
def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

# 約数取得
def getDivisor(x):
    r=[]
    l=int(x**0.5)
    for i in range(1,l+1):
        if x%i==0:
            r.append(i)
            if i!=x//i: # //は切り捨て除算
                r.append(x//i)
    r.sort()
    return r

# 素因数分解
def getFcatorization(x):
    r=[]
    l=int(x**0.5)
    for i in range(2,l+1):
        while x%i==0:
            x/=i
            r.append(i)
    if x>=2:
        r.append(int(x))
    return r

# 最大公約数取得
def getGcd(x,y):
    # ユークリッドの互除法
    while x>=1 and y>=1:
        if x<y:
            y%=x
        else:
            x%=y
    if x>=1:
        return x
    else:
        return y

# 最小公倍数取得
def getLcm(x,y):
    return int(x*y/getGcd(x,y))

# パーミテーション取得
def getPermitation(x,y):
    r=getFactorial(x)//getFactorial(x-y)
    return r

# コンビネーション取得
def getCombination(x,y):
    r=getPermitation(x,y)//getFactorial(y)
    return r

# for文のリバース
# for i in reversed(range(0,n)):

# search algorithm