pluviosidade = [30.55, 44.5, 20.5, 18.5, 60.45, 45.44]

total_pluviosidade = sum(pluviosidade)

media_pluviosidade = total_pluviosidade / len(pluviosidade)

max_pluviosidade = max(pluviosidade)

print(f"Total: {total_pluviosidade:.2f} mm")
print(f"Média: {media_pluviosidade:.2f} mm")
print(f"Máximo: {max_pluviosidade:.2f} mm")