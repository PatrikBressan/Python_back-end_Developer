# Definição da classe
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe... ')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print('Auau')

    def dormir(self):
        self.acordado = False
        print('Zzzzzz...')
    
    def __del__(self):
        print('Removendo a instância da classe.')

# Definição dos objetos
cao_1 = Cachorro('Nina', 'branca', False)
cao_2 = Cachorro('Pipa', 'preta')

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print('\n',cao_2.acordado)