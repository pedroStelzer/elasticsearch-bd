from elastic_client import es
from data.products import produtos
from data.users import usuarios
from data.orders import pedidos
from data.reviews import reviews

def inserir_dados():
    for doc in produtos:
        es.index(index="produtos", document=doc)

    for doc in usuarios:
        es.index(index="usuarios", document=doc)

    for doc in pedidos:
        es.index(index="pedidos", document=doc)

    for doc in reviews:
        es.index(index="reviews", document=doc)

    print("Dados inseridos com sucesso.")
