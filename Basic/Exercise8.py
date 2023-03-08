# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


# new_products = copy.deepcopy(produtos)

# for product in new_products:
#     product['preco'] = product['preco'] * 1.1

new_products = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

new_products_ordered_by_name = sorted(
    copy.deepcopy(new_products), key=lambda p: p['nome'], reverse=True)
new_products_ordered_by_highest_price = sorted(
    copy.deepcopy(new_products), key=lambda p: p['preco'])

print(produtos)
print(new_products)
print(new_products_ordered_by_name)
print(new_products_ordered_by_highest_price)
