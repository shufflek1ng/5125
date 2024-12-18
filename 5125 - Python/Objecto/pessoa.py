#Criar a classe "Pessoa"

class Pessoa:
    #Atributos publicos
    nome=None
    data_nascimento=None
    
    #Método Construtor
    def __init__(self,nome="Anonimo"):
        self.nome=nome

    def __str__(self):
        return f"O nome e {self.nome} e nasceu em {self.data_nascimento[0]}"
    #Método Público
    def setDataNascimento(self, ano, mes, dia):
        self.data_nascimento=(ano, mes, dia)


