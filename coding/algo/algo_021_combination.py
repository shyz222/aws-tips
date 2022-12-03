def getFactorial(x):
    r=1
    for x in range(1,x+1):
        r*=x
    return r

def getPermitation(x,y):
    r=getFactorial(x)//getFactorial(x-y)
    return r

def getCombination(x,y):
    r=getPermitation(x,y)//getFactorial(y)
    return r

n,r=map(int,input().split())
print(getCombination(n,r))