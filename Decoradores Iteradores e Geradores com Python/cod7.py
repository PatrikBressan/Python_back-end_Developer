'''
- Instrospecção:
    capacidade de um objeto saber sobre seus próprios atributos em tempo de execução.
'''

import functools

def duplicar(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    
    return envelope

@duplicar
def aprender(tecnologia):
    print(f'Estou aprendendo {tecnologia}')
    return tecnologia.upper()

#tecnologia = aprender("Python")
print(aprender.__name__)
