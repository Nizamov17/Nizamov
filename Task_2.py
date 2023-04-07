#Пусть дан список имен пользователлей s. Создайте функцию, которая: a) Преобразует имена так, чтобы имена начинались с заглавной буквы. б) Удаляет недопустимые символы (пробелы, цифры и спецсимволы)
import re
def clean_name(name):
    name = re.sub(r'[^a-zA-Zа-яА-ЯёЁ]', '', name)
    name = name.capitalize()
    return name
def clean_names(names):
    cleaned_names = []
    for name in names:
        cleaned_names.append(clean_name(name))
    return cleaned_names
s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']
cleaned_s = clean_names(s)
print(cleaned_s) 