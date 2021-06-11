#Ex007: Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. 
#Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados.

lista = []
for c in range(1,6):
  num = int(input(f"Digite o {c}º número: "))
  lista.append(num)
print(f"A sua lista de números é: {lista}")

somar = 0
for t in lista:
  somar += t
print(f"A soma de todos os números de sua lista é: {somar}")


#Método de soma alternativo e simplificado
import numpy as np
np.array(lista).sum()
