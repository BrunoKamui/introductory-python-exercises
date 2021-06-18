#Ex013: Considerando o seguinte dicionário:  alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5} Crie uma estrutura de repetição para percorrer cada elemento do dicionário
#para gravar cada aluno em um novo arquivo de texto. - Cada aluno deve ocupar uma linha do novo arquivo de texto. - O formato deve ser: nome,nota (Pedro,8.0).
#- Após a criação do arquivo de texto, faça a leitura do arquivo e mostre todos os alunos.

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open("Nota dos alunos.txt", "w") as relatorio:
    for aluno, nota in alunos.items():
        relatorio.write(f"{aluno}, {nota}\n")

with open("Nota dos alunos.txt") as relatorio:
    for linha in relatorio:
        print(linha)
