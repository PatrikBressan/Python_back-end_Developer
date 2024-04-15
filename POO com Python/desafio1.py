'''
João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas.
Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida.

Uma bicicleta pode:
- buzinar;
- parar;
- correr;

Adicione esses comportamentos.
'''
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, marcha):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1

    def buzinar(self):
        print('Plim plim...')
    
    def parar(self):
        print('Bike parada!')

    def correr(self):
        print('Bike correndo!')
    
    def trocar_marcha(self, nro_marcha):
        print('Trocando marcha')

        def _trocar_marcha():
            if nro_marcha > self.marcha:
                print('Marcha trocada...')
            else:
                print('Não foi possível trocar de marcha...')

    # Retornar as informações da classe
    # def __str__(self):
    #     return f'Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}'
    
    # Outra forma de retornar as informações da classe
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
        


bike1 = Bicicleta('Preta', 'Caloi', 2023, 700, 1)
bike1.buzinar()
bike1.parar()
bike1.correr()
bike1.trocar_marcha(1)
print(bike1.cor, bike1.modelo, bike1.ano, bike1.valor)

bike2 = Bicicleta('Verde', 'Chingling', 2000, 150, 1)
# bike2.buzinar() é equivalente a Bicicleta.buzinar(bike2)
bike2.buzinar()
Bicicleta.buzinar(bike2)
print(bike2)
bike2.trocar_marcha(3)