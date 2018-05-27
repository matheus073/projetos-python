def SomaTodos(n):
    if n<0:
        return n+1
    return SomaTodos(n-1)+n
"""""
print(SomaTodos(9))
print(1+2+3+4+5+6+7+8+9)"""

def DeXAY(x,y):
    if x<=y:
        print(x)
        DeXAY(x+1,y)

    return x,y

DeXAY(1,5)