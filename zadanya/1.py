#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Money:
    def __init__(self, rubles: int = 0, kopecks: int = 0):
        self.rubles: int = rubles
        self.kopecks: int = kopecks

    def read(self) -> None:
        self.rubles, self.kopecks = map(int, input("Введите количество рублей и копеек через пробел: ").split())

    def display(self) -> None:
        print(f"{self.rubles} руб. {int(self.kopecks):02d} коп.")

    def add(self, other: 'Money') -> 'Money':
        result: Money = Money()
        total_kopecks: int = self.rubles * 100 + self.kopecks + other.rubles * 100 + other.kopecks
        result.rubles, result.kopecks = divmod(total_kopecks, 100)
        return result

    def subtract(self, other: 'Money') -> 'Money':
        result: Money = Money()
        total_kopecks: int = self.rubles * 100 + self.kopecks - (other.rubles * 100 + other.kopecks)
        result.rubles, result.kopecks = divmod(total_kopecks, 100)
        return result

    def divide_sum(self, num: float) -> 'Money':
        result: Money = Money()
        total_kopecks: int = self.rubles * 100 + self.kopecks
        result_kopecks: int = int(total_kopecks / num * 100)  # Исправление типа
        result.rubles, result.kopecks = divmod(result_kopecks, 100)
        return result

    def divide_by_number(self, num: float) -> 'Money':
        result: Money = Money()
        total_kopecks: int = self.rubles * 100 + self.kopecks
        result_kopecks: int = int(total_kopecks / num * 100)  # Исправление типа
        result.rubles, result.kopecks = divmod(result_kopecks, 100)
        return result

    def multiply_by_number(self, num: float) -> 'Money':
        result: Money = Money()
        total_kopecks: int = self.rubles * 100 + self.kopecks
        result_kopecks: int = int(total_kopecks * num)  # Исправление типа
        result.rubles, result.kopecks = divmod(result_kopecks, 100)
        return result

    def compare(self, other: 'Money') -> bool:
        return (self.rubles == other.rubles) and (self.kopecks == other.kopecks)

    def is_less_than(self, other: 'Money') -> bool:
        return (self.rubles * 100 + self.kopecks) < (other.rubles * 100 + other.kopecks)


if __name__ == '__main__':
    money1: Money = Money()
    money1.read()
    money1.display()

    money2: Money = Money()
    money2.read()
    money2.display()

    sum_result: Money = money1.add(money2)
    print("Сумма:")
    sum_result.display()

    diff_result: Money = money1.subtract(money2)
    print("Разность:")
    diff_result.display()

    divide_sum_num: float = float(input("Введите число для деления суммы: "))
    div_sum_result: Money = money1.divide_sum(divide_sum_num)
    print("Деление суммы на число:")
    div_sum_result.display()

    divide_by_num: float = float(input("Введите число для деления: "))
    div_result: Money = money1.divide_by_number(divide_by_num)
    print("Деление на число:")
    div_result.display()

    multiply_by_num: float = float(input("Введите число для умножения: "))
    mul_result: Money = money1.multiply_by_number(multiply_by_num)
    print("Умножение на число:")
    mul_result.display()

    comparison_result: bool = money1.compare(money2)
    print(f"Сравнение: {comparison_result}")

    comparison_result_lt: bool = money1.is_less_than(money2)
    print(f"Сравнение меньше: {comparison_result_lt}")
