#Ex012: Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada um dos valores nas primeiras posições da lista 
#(o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). Faça a divisão dos dois valores e trate as seguintes exceções:
#- ValueError: se o usuário digitar um caracter. - ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão.
#- IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista. - KeyboardInterrupt: caso o usuário interrompa a execução.
#Mostre uma mensagem personalizada na ocorrência de cada um desses erros.

lista = []

try:
  lista.append(float(input("Digite o primeiro valor: ")))
  lista.append(float(input("Digite o segundo valor: ")))
  divisao = lista[0] / lista[1]
except ZeroDivisionError:
  print("Erro! Divisão por zero.")
except ValueError:
  print("Erro! Valor inválido.")
except IndexError:
  print("Erro! Índice inválido.")
except KeyboardInterrupt:
  print("O usuário interrompeu o programa.")
else:
  print(f"O resultado da divisão é {divisao}.")
