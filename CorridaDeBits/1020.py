dia=int(input())

ano = dia//365
dia -= ano*365

mes = dia//30
dia -= mes*30

print(ano,"ano(s)")
print(mes,"mes(es)")
print(dia,"dia(s)")