import os
import struct
import sys
import math

# Функція для запису результату у текстовий файл
def writeResTxt(fName, result):
    with open(fName, 'w') as f:
        f.write(str(result))

# Функція для зчитування результату з текстового файлу
def readResTxt(fName):
    result = 0.0
    try:
        if os.path.exists(fName):
            with open(fName, 'r') as f:
                result = float(f.read())
        else:
            raise FileNotFoundError(f"File {fName} not found.")
    except FileNotFoundError as e:
        print(e)
    return result

# Функція для запису результату у бінарний файл
def writeResBin(fName, result):
    with open(fName, 'wb') as f:
        f.write(struct.pack('d', result))

# Функція для зчитування результату з  бінарного файлу
def readResBin(fName):
    result = 0.0
    try:
        if os.path.exists(fName):
            with open(fName, 'rb') as f:
                result = struct.unpack('d', f.read())[0]
        else:
            raise FileNotFoundError(f"File {fName} not found.")
    except FileNotFoundError as e:
        print(e)
    return result

# Функція для обчислення результату виразу
def calculate(x):
    try:
        rad = x * math.pi / 180.0  # Перетворення градусів в радіани
        result = 2 * x / math.sin(rad)
        return result
    except ZeroDivisionError:
        print("Error: Division by zero (sin(x) == 0)")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid input value for x")
        sys.exit(1)

if __name__ == "__main__":
    try:
        data = float(input("Enter data: "))  # Введення даних від користувача
        result = calculate(data)
        print(f"Result is: {result}")

        # Запис результату в текстовий та бінарний файли
        writeResTxt("textRes.txt", result)
        writeResBin("binRes.bin", result)

        # Зчитування результату з бінарного файлу та текстового файлу
        print("Result from binary file: {0}".format(readResBin("binRes.bin")))
        print("Result from text file: {0}".format(readResTxt("textRes.txt")))
    except ValueError as e:
        print(e)
        sys.exit(1)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)