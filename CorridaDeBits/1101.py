while True:
    
    m = input().split()
    m.sort()
    n = 0
    
    if int(m[0]) <= 0:
        break
    
    for i in range(int(m[0]),int(m[1])+1,1):
        n += i
        print(i,end=" ")
    
    print("Sum=%i"%n)
    