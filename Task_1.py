#Создайте функцию calculate, которая принимает у пользователя два числа и операцию, а выдает результат операции. Обязательно: воспользуйтесь функциями exec или eval
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
operator = input("Введите операцию (+, -, *, /): ")
def calculate(num1, num2, operator):
    try:
        result = eval(f"{num1} {operator} {num2}")
        print(f"Результат: {result}")
    except ZeroDivisionError:
        print("Деление на ноль невозможно")