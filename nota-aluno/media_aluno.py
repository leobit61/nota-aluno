notas = [] 

for i in range(1, 5):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

if media >= 6:
    status = "aprovado"
else:
    status = "reprovado"

print(f"A média das notas é: {media:.2f}")
print(f"Você foi {status}.")