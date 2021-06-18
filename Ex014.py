#Ex014: Crie expressões regulares para extrair as seguintes informações de um texto (use a função findall): - Números - CEPs - URLs

import re

frase = "Enviaram 12 cartas para Rua das Flores, 23. Cep: 45220-010 e cada uma delas citava um destes 3 sites: https://www.google.com.br https://www.youtube.com https://www.facebook.com"

numeros = re.findall("\d+", frase)

cep = re.findall("\d{5}-\d{3}", frase)

url = re.findall("https?://[A-Za-z0-9.]+", frase)

print(numeros)
print(cep)
print(url)
