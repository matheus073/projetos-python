n = int(input())

for i in range(n):
    x = input().split()
    
    try:
        y = int(x[0])/int(x[1])
        print(y)

    except:
        print("divisao impossivel")
    
     
