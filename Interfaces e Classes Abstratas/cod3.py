'''
- Interfaces e Classes Abstratas:
    - aprender o conceito de contrato;
    - utilizar classes abstratas em Python e como implementá-las

- Interfaces:
    - definem o que uma classe deve fazer, mas não como;
    - Em Python, o conceito de interface é definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas;
    - Utilizamos classes abstratas para criar contratos: classes abstratas não podem/devem ser instanciadas.

ABC: abstract basic class
'''

# Criando classes abstratas com o módulo ABC
from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    # Dessa forma, com '@abstractmethod', toda classe que estender a classe ControleRemoto, deve obrigatoriamente implementar os métodos ligar e desligar.
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print('TV desligada')

    def desligar(self):
        print('TV desligada')

    @property
    def marca(self):
        return 'Samsung'


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ar condicionado ligado.')

    def desligar(self):
        print('Ar condicionado desligado.')

    @property
    def marca(self):
        return 'Gree'

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
print(controle_ar.marca)

