data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in data:
    for number in row:
        if number % 2 == 0:
            print(number)