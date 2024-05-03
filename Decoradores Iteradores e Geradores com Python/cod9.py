'''
- Geradores:
    São tipos especiais de iteradores, ao contrário das listas ou outros iteráveis, não armazenam todos os seus valores na memória.
    São definidos usando funções regulares, mas, ao invés de retornar valores usando 'return', utilizam 'yield'.
    - uma vez que um item gerado é consumido, ele é esquecido e não pode ser acessado novamente;
    - o estado interno de um gerador é mantido entre chamadas;
    - a execução de um gerador é pausada na declaração 'yield' e retomada daí na próxima vez que ele for chamado.
'''

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2
    

for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)