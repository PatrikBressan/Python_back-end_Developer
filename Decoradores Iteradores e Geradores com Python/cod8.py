'''
- Iteradores e Geradores em Python:
    conceitos que nos permitem trabalhar com sequências de maneira eficiente.

- Iterador:
    o protocolo do iterador é uma maneira do Python fazer a iteração de um objeto, que
    consiste em dois métodos especiais "__iter__()" e "__next__()"

    Economizar memória evitando carregar todas as linhas do arquivo.

    Iterar linha a linha do arquivo

'''

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros=[2, 7, 9]):
    print(i)