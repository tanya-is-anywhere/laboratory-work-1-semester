# Лабораторная работа №1: Работа с структурами данных, циклами и условными операторами в Python

# Цель работы: Освоить работу со структурами данных, циклами и условными операторами в языке программирования Python.

print("Задание 1")
n = int(input("Введите число: "))
for i in range(1, n+1):
    print(i)

print("\nЗадание 2")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    print(f"Большее число: {a}.")
elif a == b:
    print(f"Данные числа a и b равны.")
else:
    print(f"Большее число: {b}.")


