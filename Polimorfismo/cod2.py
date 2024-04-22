'''
- Polimorfismo com herança
'''

class Passaro:
    def __init__(self):
        pass

    def voar(self):
        print('Voando...')


class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não voa.')

# FIXME: exemplo ruim do uso de polimorfismo com herança para 'ganhar' o método voar
class Aviao(Passaro):
    def voar(sefl):
        print('Avião decolando...')

def plano_de_voo(passaro):
    passaro.voar()


plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())

#p1 = Pardal()
#p2 = Avestruz()

# plano_de_voo(p1)
# plano_de_voo(p2)