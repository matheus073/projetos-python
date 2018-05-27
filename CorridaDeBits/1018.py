num=int(input())

n100,n50,n20,n10,n5,n2=0,0,0,0,0,0

print(num)

if num>=100:
    n100=(num//100)
    num=num-n100*100

print(n100,"nota(s) de R$ 100,00")

if num >=50:
    n50=num//50
    num=num-n50*50

print(n50,"nota(s) de R$ 50,00")

if num >=20:
    n20=num//20
    num=num-n20*20

print(n20,"nota(s) de R$ 20,00")

if num>=10:
    n10=num//10
    num=num-n10*10

print(n10,"nota(s) de R$ 10,00")

if num>=5:
    n5=num//5
    num=num-n5*5

print(n5,"nota(s) de R$ 5,00")

if num>=2:
    n2=num//2
    num=num-n2*2

print(n2,"nota(s) de R$ 2,00")

print(num,"nota(s) de R$ 1,00")
