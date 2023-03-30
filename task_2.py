# Функция slicer() на вход принимает кортеж и случайный элемент. Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно. Если элемента нет вовсе – вернуть пустой кортеж. Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идет до конца исходного.
def slicer(a, random):
    if a.count(random) == 1:
        return a[a.index(random):]
    elif a.count (random) > 1:
        first_ind = a.index(random)
        second_ind = a.index(random, first_ind + 1)
        return a[first_ind:second_ind + 1]
    else:
        return tuple()
a = (10,1,6,7,3,2,4,5,7,8)
print(slicer(a=a,random=3))