from datetime import datetime

pedidos = [
    {
        "id": "o1",
        "usuario_id": "u1",
        "produtos": [
            {"produto_id": "p1", "quantidade": 1, "preco_unitario": 4500.00},
            {"produto_id": "p2", "quantidade": 2, "preco_unitario": 299.90}
        ],
        "total": 5099.80,
        "status": "entregue",
        "data_pedido": datetime.now()
    },
    {
        "id": "o2",
        "usuario_id": "u2",
        "produtos": [
            {"produto_id": "p2", "quantidade": 1, "preco_unitario": 299.90}
        ],
        "total": 299.90,
        "status": "em andamento",
        "data_pedido": datetime.now()
    }
]
