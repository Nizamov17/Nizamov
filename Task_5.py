#Создайте функцию countdown, которая принимает список рандомных чисел от 0 до 10, а возвращает каждый элемент этого списка в порядке обратного отсчета, а после 0 - слово " Пуск!".
def countdown(numbers):
    for num in numbers[::-1]:
        print(num)
    print("Пуск!")


numbers = [0, 1, 2, 3, 4, 5]
countdown(numbers)