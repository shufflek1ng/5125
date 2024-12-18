#import veiculo
#import veiculo as v
from veículo import Veiculo 
from automovel import Automovel

def testarVeiculo():
    listaVeiculos=[]
    veiculo1 = Veiculo()      
    veiculo2 = Veiculo(2000,1000)
    veiculo3 = Veiculo(2500,1500)
    veiculo4 = Veiculo(1200,700)
    listaVeiculos.append(veiculo1)
    listaVeiculos.append(veiculo2)
    listaVeiculos.append(veiculo3)
    listaVeiculos.append(veiculo4)

#veiculo3 alterar anoFabrico
    veiculo3.setAnoFabrico(2005)


    for veiculo in listaVeiculos:
        print(veiculo)
def testarAutomovel():
    standAutomoveis = []
    auto1 = Automovel("Ferrari","Gasolina","Amarelo",0,3000,1800)
    auto1.setVelocidadeMaxima(300)
    auto1.acelerar(250)
    auto1.acelerar(50)
    auto1.acelerar(1)

    print(auto1)

    auto2 = Automovel("Toyota,","Gasolina","Azul",0,1300,800) 
    auto3 = Automovel("Audi","Gasóleo","Vermelho",0,3000,1700)
    auto4 = Automovel("Mercedes","Gasolina","Preto",50,2000,1200)
    standAutomoveis.append(auto1)
    standAutomoveis.append(auto2)
    standAutomoveis.append(auto3)
    standAutomoveis.append(auto4)
    for automovel in standAutomoveis:
        print(automovel)


def main():
    print("Inicio Programa")

    testarAutomovel()
    #testarVeiculo()

    print("Fim Programa")

   
if __name__ == "__main__":
    main()
    