"""def num(i,n):
    if i<n:
        return
    num(i-1,n)
    print(i)
num(5,1)"""

def num2(j,m):
    if j>m:
        return
    num2(j+1,m)
    print(j)
num2(1,10)