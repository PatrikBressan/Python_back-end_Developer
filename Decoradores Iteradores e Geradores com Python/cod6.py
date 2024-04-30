'''
- Funções de decoraçao com argumentos:
    Podemos usar *args e **kwargs na função interna, com isso ela
    aceitará um número arbitrário de argumentos posicionais e de palavras-chave.
'''

def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return envelope

@duplicar
def aprender(tecnologia):
    print(f'Estou aprendendo {tecnologia}')
    return tecnologia.upper()


tecnologia = aprender('Python')
print(tecnologia)
print(aprender.__name__)