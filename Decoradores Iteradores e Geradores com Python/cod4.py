'''
- Decoradores: colocar uma personalização de comportamento dentro de uma função/código.

- Açúcar Sintático:
    Python permite que você use decoradores de maneira mais simples com o símbolo @
'''

def meu_decorador(funcao):
    def envelope():
        print('Faz algo antes de executar a função.')
        funcao()
        print('Faz algo depois de executar a função.')

    return envelope

def ola_mundo():
    print('Olá Mundo!')

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()