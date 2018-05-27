n=int(input())
num=''
m=[]
media=0.0

for i in range(n):
    num=(input())
    m=num.split()
    media=((float(m[0])*2)+(float(m[1])*3)+(float(m[2])*5))/10
    print("%.1f"%media)