nota = float(input("Digete a nota do 1º aluno: "))
num = 1
notas = []
soma = media = 0.0
aprovados = reprovados = 0
while nota != -1:
    num += 1
    notas.append(nota)
    nota = float(input("Digete a nota do %iº aluno: " % num))

print("foram listados %i numeros" % (num - 1))
print("Ordem normal:", notas)
print("Ordem inverça:", notas[::-1])

for ele in notas:
    soma += ele

media = soma / len(notas)

print("A soma das notas: %2g" % soma)
print("A media das notas: %2g" % media)

for i in notas:
    if i >= 7:
        aprovados += 1
    else:
        reprovados += 1

print("%i alunos ficaram aprovados" % aprovados)
print("%i alunos ficaram reprovados" % reprovados)
