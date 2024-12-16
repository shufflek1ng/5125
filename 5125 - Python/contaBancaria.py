#Criar a Classe
class ContaBancaria:

#Criar o método construtor em python
    def __init__(self, titular, saldo_inicial):
        # Atributos da conta bancária
        self.titular = titular
        self.saldo = saldo_inicial
#Getters e Setters são públicos
    def getSaldo(self):
        return self.saldo
    
    def deposito(self,valor):
        self.saldo += valor

    def debito(self,valor):
        self.saldo -= valor

#Criar método Privado de verificação bancaria(dois underscores é método privado)

    def verificacaoInternaBancaria(self):
            print("Verificação Interna do Banco")            