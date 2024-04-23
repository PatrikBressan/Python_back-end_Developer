'''
- Entender as diferenças entre métodos de classe e métodos estáticos

- Métodos de classe estão ligados à classe e não ao objeto. Eles têm acesso ao estado da classe, porque recebem um parâmetro
que aponta para a classe e não para a instância do objeto.
    - O self aponta para a instância.
    - Método de classe geralmente são utilizados para criar métodos de fábrica.

- Métodos estáticos não recebem um primeiro argumento explícito. É um método vinculado à classe e não ao objeto da classe.
Este método não pode acessar ou modificar o estado da classe. Ele está presente em uma classe porque faz sentido que o método
esteja presente na classe.
    - Métodos estáticos geralmente são utilizados para criar funções utilitárias.
'''

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # Caso eu precise ter acesso ao contexto da classe, utilizo Métodos de Classe
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        # cls refere-se a própria classe, ou seja, método de classe e não de instância (como o self que é para instância)
        print(cls)
        idade = 2024 - ano
        return cls(nome, idade)
    
    # Não preciso ter acesso ao contexto da classe e nem à instância do objeto, posso utilizar Métodos Estáticos.
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa.criar_de_data_nascimento(1988, 6, 19, 'Patrik')
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(15))