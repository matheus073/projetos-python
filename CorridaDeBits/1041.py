p=input()
q=p.split()

x,y=float(q[0]),float(q[1])

if x>0:
    if y>0:
        print("Q1")
    elif y<0:
        print("Q4")
    else:
        print("Eixo X")

elif x<0:
    if y>0:
        print("Q2")
    elif y<0:
        print("Q3")
    else:
        print("Eixo X")

elif x==0 and y!=0:
    print("Eixo Y")

else:
    print("Origem")