# Код у файлі truck.py
from machine import Machine  # Імпортуємо базовий клас

class Truck(Machine):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)  # Викликаємо конструктор базового класу
        self.payload_capacity = payload_capacity  # Вантажопідйомність

    def load(self):
        print(f"Вантажна машина з вантажопідйомністю {self.payload_capacity} кг завантажується.")

    def unload(self):
        print("Розвантаження вантажної машини.")