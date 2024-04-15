'''
- Classes: define as características e comportamentos de um objeto, porém não conseguimos
usá-las diretamente.

- Objetos: podemos usá-los diretamente, e eles possuem as características e comportamentos
que foram definidos nas classes.
'''

# Definição da classe
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print('Auau')

    def dormir(self):
        self.acordado = False
        print('Zzzzzz...')

# Definição dos objetos
cao_1 = Cachorro('Nina', 'branca', False)
cao_2 = Cachorro('Pipa', 'preta')

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print('\n',cao_2.acordado)