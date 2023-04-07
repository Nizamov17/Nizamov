#Пусть дана функция, которая спрашивает имя пользователя.Создайте декоратор hello, который дополнительно будет выводить приветствие: "Привет, <имя>!"
def hello(a):
    def wrapper():
        name = a()
        print(f"Привет, {name}!")
    return wrapper
@hello
def get_name():
    name = input('Введите имя: ')
    return name
get_name()