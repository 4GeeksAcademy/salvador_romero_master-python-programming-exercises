# Your code here
def list_and_tuple(*args):
    list=[]
    for i in args:
        list.append(str(i))
    return list,tuple(list)

lista, tupla = list_and_tuple(23,34,456)
print(lista)
print(tupla)