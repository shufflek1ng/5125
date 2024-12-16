from contaBancaria import ContaBancaria

conta1 = ContaBancaria("Ana", 111.10)

# Saber o saldo da conta1
var = conta1.getSaldo()
#Creditar o valor na conta (deposito)
print(var)

conta1.deposito(1000)

print(conta1.getSaldo())

#Débito
conta1.debito(200)

print(conta1.getSaldo())

#Criar 2a Conta
conta2 = ContaBancaria("Bruno",2000)

conta2.verificacaoInternaBancaria()