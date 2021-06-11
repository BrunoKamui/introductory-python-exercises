#Ex005: Usar as estruturas FOR e WHILE para ler 5 notas e informar a média

#FOR

soma = 0

for i in range(1,6):
  nota = float(input(f"Digite a nota da prova {i}: "))
  soma += nota

media = soma / 5

print(f"A média do aluno foi {media}.")


#WHILE

provas = 1
soma = 0

while provas <= 5:
  nota = float(input(f"Digite a nota da prova {provas}: "))
  soma += nota
  provas += 1

media = soma / 5

print(f"A média do aluno foi {media}.")
