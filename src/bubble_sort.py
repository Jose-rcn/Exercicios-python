#estudo sobre algoritmos de ordenação de arrays
lista = [10,8,12, 12, 1, 2, 44, 3, 2, 90, 12, 13, 2]

def bubble_sort(lista:list) -> list:
    lista_ordenada = lista.copy()
    for i in range(0, len(lista_ordenada,)):
        for t in range(i +1, len(lista_ordenada)):
            if lista_ordenada[i] > lista_ordenada[t]:
                lista_ordenada[i], lista_ordenada[t] = lista_ordenada[t], lista_ordenada[i]
    return lista_ordenada

print(bubble_sort(lista))
print(lista)