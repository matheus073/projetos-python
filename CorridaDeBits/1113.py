n = input()

n = n.split()

x = int(n[0])
y = int(n[1])

while x!= y:
    
    if x < y:
        print("Crescente")
    
    elif x > y:
        print("Decrescente")   

    n = input()

    n = n.split()

    x = int(n[0])
    y = int(n[1])
