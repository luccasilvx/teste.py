class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0 #média calculada por meio das notas, usúario não insere

    def calcula_media(self):
        self.media = (self.nota1 + self.nota2 / 2)
        return self.media
    
    def mostrar_dados(self):
        print('Nome: ', self.nome)
        print('Nota 1:', self.nota1)
        print('Nota 2:', self.nota2)
        print('Média:', self.media)

    def resultado(self):
        if self.media >= 6.0:
            print('Aprovado')
        else:
            print('Reprovado')
    
a1 = Aluno("Lucas", 8.8, 9.6)
a1.mostrar_dados()
a1.resultado()
media1 = a1.calcula_media()
print(media1)

a2 = Aluno("Jorge", 8.7, 9.3)
a2.mostrar_dados()
a2.resultado()
media2 = a2.calcula_media()
print(media2)
