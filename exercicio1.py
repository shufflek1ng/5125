tamanho = int(input("Insira o tamanho da lista: "))

lista = []
for i in range(tamanho):
    while True:
        numero = int(input(f"Insira um número entre 1 e 50 ({i+1}/{tamanho}): "))
        if 1 <= numero <= 50:
            lista.append(numero)
            break
        print("Número inválido. Tente novamente.")

print("Os valores inseridos foram:")
print(lista)
