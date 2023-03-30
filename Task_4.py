def del_from_tuple (tpl, element):
    if element in tpl:
        index = tpl.index(element)
        return tpl[:index] + tpl[index + 1:]
    else:
        return tpl

tpl = (1,4,7,9,2,5,7,8)
print(del_from_tuple(tpl=tpl, element=3))