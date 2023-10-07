# Запит на введення розміру матриці
n = int(input("Введіть розмір квадратної матриці: "))

filler1 = ''
while len(filler1) != 1:
    # Запит на введення символів-заповнювачів
    filler1 = input("Введіть символ-заповнювач: ")
    if len(filler1) != 1:
        print("Символ-заповнювач має бути лише одним символом кожен.")

# Створення та заповнення матриці за допомогою зубчастого списку
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        if i >= j and i + j >= n - 1:
            row.append(filler1)
        elif i <= j and i + j <= n - 1:
            row.append(filler1)
        else:
            row.append(' ')
    matrix.append(row)

# Вивід матриці
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()