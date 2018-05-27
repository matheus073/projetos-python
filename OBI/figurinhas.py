n = input().split()
c = input().split()
p = input().split()

x = len(c)
cont=0

for a in p:
    if 1 != p.count(a):
        del(p[cont])
    cont += 1

for i in c:
    for j in p:
        if i in j:         
            x -= 1

print(x)