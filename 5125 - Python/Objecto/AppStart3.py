from pessoa import Pessoa

# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("Joao")
pessoa2 = Pessoa("Marta")
pessoa3 = Pessoa("Ronaldo")

# Exibindo as informações da pessoa
pessoa1.setDataNascimento(2002,4,14)
pessoa2.setDataNascimento(2005,9,18)
pessoa3.setDataNascimento(1985,2,5)

lista_convidados = []

lista_convidados.append(pessoa1)
lista_convidados.append(pessoa2)
lista_convidados.append(pessoa3)

#Verificar o tipo da variável "data_nascimento"
print(type(pessoa1.data_nascimento))

for convidado in lista_convidados:
    print(convidado)