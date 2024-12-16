'''
#Forma 1


# Classe Funcionário representa um funcionario da empresa
class Funcionario:
    # Método construtor serve para criar funcionários
    def __init__(self):
        self.nome = None
        self.idade = None
        self.cargo = None
        self.salario = None

#Getters e Setters (métodos para ir buscar(get) e para salvar(set))
    def setNome(self, nome):
        self.nome = nome
#Getters do nome
    def getNome(self):
        return self.nome
       
#Criar lista com Funcionarios da empresa
empresa = []
#Acabou a classe funcionario
#Criar outro funcionario
func2 = Funcionario()
func2.setNome("Ronaldo")
print(func2.getNome())

#Criar um funcionario
func1 = Funcionario()
func1.setNome("Ana")
nomeFuncionario1 = func1.getNome()
print(nomeFuncionario1)
#print(type(func1))
empresa.append(func1)
empresa.append(func2)
'''


#Forma 2

# Classe Funcionário representa um funcionario da empresa
class Funcionario:
    # Método construtor serve para criar funcionários
    def __init__(self, nome, idade, cargo, salario):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario

#Getters e Setters (métodos para ir buscar(get) e para salvar(set))
    def setNome(self,nome):
        self.nome = nome
#Getters do nome
    def getNome(self):
        return self.nome
    
    #Importado para Appstart.py
    from funcionario import Funcionario

#Acabou a classe funcionario
'''empresa = []
#Criar outro funcionario
func2 = Funcionario("Gabriel",45,"Gerente",825.55)
#func2.setNome("Ronaldo")
print(func2.getNome())
func1 = Funcionario("Daniel",45, "Vendedor", 1250.44)
#func1.setNome("Ana")
nomeFuncionario1 = func1.getNome()
print(nomeFuncionario1)
#print(type(func1))
empresa.append(func1)
empresa.append(func2)
'''