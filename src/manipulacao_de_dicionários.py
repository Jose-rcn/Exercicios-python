from copy import deepcopy
products = [
    {'nome': 'Pineapple', 'price': 10.00},
    {'nome': 'Meat', 'price': 22.32},
    {'nome': 'Banana', 'price': 10.11},
    {'nome': 'Chocolate', 'price': 105.87},
    {'nome': 'Wine', 'price': 69.90},
]


new_products = deepcopy(products)
for items in new_products:
    items['price'] = round(items['price'] * 1.1,2)

products_ordered_by_name = deepcopy(products)
products_ordered_by_name = sorted(products,key=lambda *produtos: [itens['nome']for itens in produtos])

products_ordered_by_value = deepcopy(products)
products_ordered_by_value = sorted(products,key=lambda *produtos: [itens['price']for itens in produtos], reverse=True)

# print(*products)
# print(*products_ordered_by_name)
# print(products_ordered_by_value)

#Another way to solve the problem without using the sorted method
# def order_dicts(list_of_dicts,key):
#     ordered_list = deepcopy(produtos)
#     '''Recebe uma lista com dicionarios e uma chave, e os ordena conforme a chave. Todos os dicionarios presentes na lista precisam ter a chave'''
#     for i in range(0, len(list_of_dicts)):
#         for t in range(i +1 ,len(list_of_dicts)):
#             if ordered_list[i][key] > ordered_list[t][key]:
#                 ordered_list[i], ordered_list[t] = ordered_list[t], ordered_list[i]
#     return ordered_list




