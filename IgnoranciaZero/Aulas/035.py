def Max(*num):
    maior=num[0]
    for x in num:
        if x>=maior:
            maior=x
    return maior
