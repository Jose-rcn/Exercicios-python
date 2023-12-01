#estudo sobre algoritmos de ordenação de arrays
lista = 10,8,12, 12, 1, 2, 44, 3, 2, 90, 12, 13, 2
aux = 0
requests = 0
for i in range(0, len(lista,),1):
    for t in range(i +1, len(lista), 1):
        if lista[i] > lista[t]:
            aux = lista[i]
            lista[i] = lista[t]
            lista[t] = aux
        requests +=1
print(lista)
print(requests)