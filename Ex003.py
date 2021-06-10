#Ex003: Leia a idade do usuário e classifique-o em: - Criança – 0 a 12 anos - Adolescente – 13 a 17 anos - Adulto – acima de 18 anos
#-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida

idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
  print(f"Você tem {idade} anos. Você é uma criança.")
elif idade > 12 and idade <= 17:
    print(f"Você tem {idade} anos. Você é um adolescente.")
elif idade >= 18:
    print(f"Você tem {idade} anos. Você é um adulto.")
else:
    print("Sua idade não pode ser negativa. Digite novamente.")
