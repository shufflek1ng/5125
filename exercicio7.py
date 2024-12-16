lista_automovel = []

while True:
    marca = input("Digite a marca do automóvel (ou 's' para sair): ")

    if marca == 's':
        break

    valor = float(input("Digite o valor do automóvel: "))
    lista_automovel.append((marca, valor))

for marca, valor in lista_automovel:
    print(f"Marca: {marca}, Valor: {valor:.2f}")

total_valor = sum(valor for _, valor in lista_automovel)
print(f"Total de todos os valores: {total_valor:.2f}")