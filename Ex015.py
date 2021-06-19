#Ex015: Crie uma classe chamada aluno com os seguintes atributos: - Nome - Nota 1 - Nota 2 - Crie um construtor para a classe (__init__)
#Crie as seguintes funções (métodos): - Calcula média, retornando a média aritmética entre as notas - Mostra dados, que somente imprime o valor de todos os atributos
#- Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior ou igual a 6.0, o aluno está aprovado)
#Crie dois objetos (aluno1 e aluno2) e teste as funções.


class aluno:
  def __init__(self, nome, nota1, nota2):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2
    self.media = 0.0
  
  def tirar_media(self):
    self.media = (self.nota1 + self.nota2) / 2
    return self.media

  def mostrar(self):
    print("Nome: ", self.nome)
    print("Nota 1: ", self.nota1)
    print("Nota 2: ", self.nota2)
    print("Média: ", self.media, "\n")

  def resultado(self):
    if self.media >= 6.0:
      print("O aluno está aprovado.\n")
    else:
      print("O aluno está reprovado.\n")


a1 = aluno("Roger", 4.5, 5.0)
a1.tirar_media()
a1.mostrar()
a1.resultado()

a2 = aluno("Ana Luiza", 9.5, 7.5)
a2.tirar_media()
a2.mostrar()
a2.resultado()
