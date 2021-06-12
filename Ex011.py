#Ex011: Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. 
#Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula
#DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12.
#O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.
#- Função para ler os valores (não recebe parâmetro e retorna os dois valores) - Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
#- Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros) 
#- Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)

def dados():
  tempo_viagem = float(input("Quanto tempo irá durar sua viagem? "))
  vel_media = float(input("Qual será sua velocidade média? "))
  return (tempo_viagem, vel_media)

def cacl_distancia(t, v):
  distancia = t * v
  return distancia

def calc_litros(d):
  litros = d / 12
  return litros

def exibir_resultado(l):
  print(f"Você irá gastar {l} litros de combustível em sua viagem.")

t, v = dados()
d = cacl_distancia(t, v)
l = calc_litros(d)
exibir_resultado(l)
