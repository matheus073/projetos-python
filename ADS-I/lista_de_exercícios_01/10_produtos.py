produtos = []
cont = 0
for i in range(2):
    produto = float(input("%iº Produto: "%(i+1)))
    produtos.append(produto)


for i in produtos:
    avista = i-(i*0.09)
    x5 = i/5
    x10 = (i+(i*0.17))/10
    print("\n-------------------------------------------------------------------------------------------\n valor da compra do %iº produto custa %.2f e você tem as sequintes formas de pagamento:\nÀ vista = %.2f, Em 5x = %.2f, Em 10x = %.2f"%(cont+1,i,avista,x5,x10))
    cont += 1