from funcionario import Funcionario

#Acabou a classe funcionario
empresa = []
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