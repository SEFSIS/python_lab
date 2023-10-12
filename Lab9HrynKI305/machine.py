# Код у файлі machine.py
class Machine:
    def __init__(self, make, model, year):
        self.make = make  # Виробник
        self.model = model  # Модель
        self.year = year  # Рік випуску

    def start(self):
        print(f"{self.year} {self.make} {self.model} почала рух.")

    def stop(self):
        print(f"{self.year} {self.make} {self.model} зупинилася.")