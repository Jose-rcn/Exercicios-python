from copy import deepcopy
produtos = [
    {'nome': 'Pineapple', 'preco': 10.00},
    {'nome': 'Meat', 'preco': 22.32},
    {'nome': 'Banana', 'preco': 10.11},
    {'nome': 'Chocolate', 'preco': 105.87},
    {'nome': 'Wine', 'preco': 69.90},
]
for itens in produtos:
    itens['preco'] = round(itens['preco'] * 1.1,2)
novos_produtos = deepcopy(produtos)
# def order_dicts(list_of_dicts):
#     ordered_list  = []
#     teste = sorted([itens['nome'] for itens in list_of_dicts])
#     for index, itens in enumerate(list_of_dicts):
#         list_of_dicts.index(itens)
#         ordered_list += list_of_dicts[teste[index]]
#     return ordered_list
# print(order_dicts(produtos))



