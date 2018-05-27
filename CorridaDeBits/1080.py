maior=num=p=0
for i in range(100):
    num=int(input())
    if num>maior:
        maior=num
        p=i

print(maior)
print(p+1)