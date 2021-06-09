#Ex002: Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. 
#Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula
#DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12.
#O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.

tempo_de_viagem = float(input("Quanto tempo irá durar sua viagem? "))
velocidade_media = float(input("Qual será sua velocidade média? "))

distancia = tempo_de_viagem * velocidade_media
litros = distancia / 12

print(f"Sua viagem irá durar {tempo_de_viagem} e você irá viajar numa velocidade média de {velocidade_media}Km/h. Você vai percorrer uma distância de {distancia}Km e gastará {litros} litros de combustível.")
