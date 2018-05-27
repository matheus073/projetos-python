import random

sorte = random.randint(1, 100)

cont = 0

while True:
    cont += 1
    num = int(input("Digete seu palpite: "))
    if num < sorte:
        print("Você deve chutar mais alto")
    elif num > sorte:
        print("Você deve chutar mais baixo")
    else:
        print("Parabens! O numero escolhido fou %i" % num)
        print("Você usou %i chutes" % cont)
        break
