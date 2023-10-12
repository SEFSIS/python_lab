# Код у файлі main.py
from machine import Machine
from truck import Truck

if __name__ == "__main__":
    car = Machine("Toyota", "Camry", 2020)  # Створюємо екземпляр базового класу
    car.start()
    car.stop()

    truck = Truck("Ford", "F-150", 2022, 5000)  # Створюємо екземпляр похідного класу
    truck.start()
    truck.load()
    truck.unload()
    truck.stop()