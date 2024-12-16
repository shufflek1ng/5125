numeros = [int(input(f"Número {i+1}: ")) for i in range(5)]

print("\nResultados:")
print(f"Valor total: {sum(numeros)}")
print(f"Média dos valores: {sum(numeros)/len(numeros):.2f}")
print(f"Valor máximo: {max(numeros)}")