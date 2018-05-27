while True:
    
    n = input().split()

    x = int(n[0])
    y = int(n[1])

    if x > 0 and y > 0:
        print("primeiro")
    elif x > 0 and y < 0:
        print("quarto")
    elif x < 0 and y > 0:
        print("segundo")
    elif x < 0 and y < 0:
        print("terceiro")
    elif x == 0 or y == 0:
        break