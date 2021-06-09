#Ex001: Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

print (f"A soma de {n1} e {n2} é {soma}.")
print (f"A subtração de {n1} e {n2} é {sub}.")
print (f"A multiplicação de {n1} e {n2} é {mult}.")
print (f"A divisão de {n1} e {n2} é {div}.")
