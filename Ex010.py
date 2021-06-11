#Ex010: Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é F = (9 * C + 160) / 5, 
#na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius. - Função para ler e retorna o valor da temperatura (não recebe parâmetro).
#- Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius). - Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão.

def digite():
  c = int(input("Digite a temperatura em celcius: "))
  return c

def calcular_temperatura(c):
  f = (9 * c + 160) / 5
  return f

def resultado(F):
  print(f"Na conversão, {c}º Celcius são {f}º Fahrenheit.")

c = digite()
f = calcular_temperatura(c)
resultado(f)
