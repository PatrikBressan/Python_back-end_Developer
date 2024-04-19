'''
- Python é dinamicamente tipado, por isso não temos palavras reservadadas para definir o nível de acesso aos atributos e métodos da classe.
- Utilizamos convenções no nome do recurso, para definir se a variável é pública ou privada.
- Público pode ser acessado de fora da classe
- Privado só pode ser acessado pela classe: convenção utilizar o underline (_)
** Interpretador Python não garante a proteção do recurso: é apenas uma convenção.
'''

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        # Convenção: utilizar o _ no início da variável para indicar uma variável privada.
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo

conta = Conta('0001', 100)
conta.depositar(100)
# Por ser uma variável privada, não aconselha-se fazer esse acesso a seguir:
#print(conta._saldo)

# O correto é termos um método para mostrar isso para nós:
print(conta.mostrar_saldo())

print(conta.nro_agencia)