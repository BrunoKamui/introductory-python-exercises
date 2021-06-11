#Ex008: Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição.
#Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média.

resultados = {}
for a in range(1,4):
  aluno = str(input(f"Digite a nome do {a}º aluno: "))
  nota = float(input(f"Digite a nota do {a}º aluno: "))
  resultados[aluno] = nota

for al, nt in resultados.items():
  print(f"{al} está com nota {nt}.")

somatoria = 0
for s in resultados.values():
  somatoria += s
  media_alunos = somatoria /  3
print(f"A média das notas dos alunos é {media_alunos}.")
