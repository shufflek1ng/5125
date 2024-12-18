class Veiculo:
    '''
    atributos de instâancia privados
    cilindrada
    peso
    anoFabrico
    velocidade Máxima
    '''

    #Método construtor
    def __init__(self,cilindrada=1500,peso=100):
            self.__cilindrada = cilindrada
            self.__peso = peso
            self.__anoFabrico = None
            self.__velocidadeMaxima = None


    # setters 
    def setCilindrada(self, novaCilindrada):
          self.__cilindrada = novaCilindrada
    def setPeso(self, novoPeso):
          self.__peso = novoPeso
    def setAnoFabrico(self,novoAnoFabrico):
          self.__anoFabrico=novoAnoFabrico
    def setVelocidadeMaxima(self, novaVelocidadeMaxima):
          self.__velocidadeMaxima=novaVelocidadeMaxima

    # getters
    def getCilindrada(self):
          return self.__cilindrada
    def getPeso(self):
          return self.__peso
    def getAnoFabrico(self):
          return self.__anoFabrico
    def getVelocidadeMaxima(self):
          return self.__velocidadeMaxima


    # Redefinir o método 'toString'
    def __str__(self):
          return f"Cilindrada:{self.__cilindrada}, peso: {self.__peso}, Ano de Fabrico: {self.__anoFabrico}, Velocidade Máxima: {self.__velocidadeMaxima}" 