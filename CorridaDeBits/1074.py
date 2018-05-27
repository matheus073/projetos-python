num = int(input())

for i in range(num):
    x = int(input())
    if x % 2 == 0 and x != 0:
        print("EVEN", end=" ")
        if x > 0:
            print("POSITIVE")

        else:
            print("NEGATIVE")

    elif x == 0:
        print("NULL")

    else:
        print("ODD", end=" ")
        if x > 0:
            print("POSITIVE")

        else:
            print("NEGATIVE")
