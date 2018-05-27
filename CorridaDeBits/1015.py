x = input()
y = input()

x = x.split()
y = y.split()

x1,y1 = float(x[0]),float(x[1])
x2,y2 = float(y[0]),float(y[1])

d = ((x2-x1)**2+(y2-y1)**2)**(0.5)

print("%.4f"%d)