numeros = []

print("Escreve números inteiros, para terminar escreve 'sair'")

while True:
        entrada = input("Escreve um número ou sair: ")
        if entrada == 'sair':
            break
        try:
            numeros.append(int(entrada))
        except ValueError:
            print("Inválido")
print(numeros)
print(sorted(numeros, reverse=True))

if numeros:
    print(f"Media: {sum(numeros) / len(numeros):.2f}")
