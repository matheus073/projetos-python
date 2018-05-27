pro1 = input()
pro2 = input()

p1 = pro1.split()
p2 = pro2.split()

uni1,val1 = int(p1[1]),float(p1[2])
uni2,val2 = int(p2[1]),float(p2[2])

total = ((uni1*val1)+(uni2*val2))

print("VALOR A PAGAR: R$ %.2f"% total)