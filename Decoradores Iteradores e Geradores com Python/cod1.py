'''
- Decoradores:
    Funções em python são objetos de primeira classe: posso passar essas funções como argumentos para outras funções.
    Bem como retornar uma função dentro de outra função.

- Inner functions: definir funções dentro de outras funções.

'''

def mensagem(nome):
    print('Executando mesagem.')
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('Executando mensagem longa')
    return f'Olá, tudo bem com você {nome}?'

def executar(funcao, nome):
    print('Executando executar.')
    return funcao(nome)

#executar(mensagem)
print(executar(mensagem_longa,'José'))