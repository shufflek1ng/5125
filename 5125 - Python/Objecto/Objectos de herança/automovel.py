from veículo import Veiculo
class Automovel(Veiculo):
    '''
    marca
    combustivel
    cor
    velocidade
    '''

#Método Construtor
    def __init__(self, marca, combustivel, cor, velocidade, cilindrada, peso):
        super().__init__(cilindrada, peso)
        self.__marca = marca
        self.__combustivel = combustivel
        self.__cor = cor
        self.__velocidade = velocidade

# getters 
    def acelerar(self, aumentar):
        if (aumentar + self.__velocidade) <= self.getVelocidadeMaxima():
            self.__velocidade += aumentar
            print(f"Acelerei {aumentar} km/h para {self.__velocidade} km/h")
        else:
            print(f"Ultrapassou a velocidade máxima de {self.getVelocidadeMaxima()}")

    def __str__(self):
          variavel= super().__str__()
          return f"{variavel}, Marca: {self.__marca}, Combustível: {self.__combustivel}, Cor: {self.__cor}, Velocidade: {self.__velocidade}"