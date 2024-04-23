'''
Todos os objetos nascem com o mesmo número de atributos de classe e de instância.

- Atributos de classes: são compartilhados entre os objetos.

- Atributos de instâncias: são diferentes para cada objeto (cada objeto tem uma cópia).
    - o self aponta para a instância, e não para a classe.
'''

class Estudante:
    escola = 'IFMS'

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f'{self.nome} ({self.numero}) - {self.escola}'

def mostrar_valores(*objetos):
    for obj in objetos:
        print(obj)

aluno_1 = Estudante('Patrik', 1)
aluno_2 = Estudante ('Lorenzo', 2)
mostrar_valores(aluno_1, aluno_2)

# Mostrando a diferença de atributos de instâncias, alteramos de um objeto e não influencia no outro objeto
# Contudo, ao alterarmos um atributo de classe, alteramos para todos os objetos instanciados desta classe
aluno_1.numero = 3
Estudante.escola = 'Python'
mostrar_valores(aluno_1, aluno_2)