from itertools import zip_longest

lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Washington', 'Berlim', 'Cairo']
lista_2 = ['BA', 'SP', 'MG', 'DC']
lista_3 = ['Brasil', 'Brasil', 'Brasil', 'EUA', 'Alemanha']


def my_zip_longest(*args):
    def stop_flag(val):
        for valores in val:
            if valores is not None:
                return False
        return True     
    listas = [*args]
    result = []
    count = 0
    while True:
        val = []
        for lista in listas:
            try:
                a = lista[count]
            except IndexError:
                a = None
            val.append(a)
        if stop_flag(val):
            break
        result.append(val)
        count += 1
    return result
print(my_zip_longest(lista_1, lista_2, lista_3))

z = zip_longest(lista_1, lista_2, lista_3, fillvalue= None)
print(list(z))