from elastic_client import es

def criar_indices():
    indices = {
        "produtos": {
            "mappings": {
                "properties": {
                    "nome": {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
                    "descricao": {"type": "text"},
                    "preco": {"type": "float"},
                    "tags": {"type": "keyword"},
                    "data_cadastro": {"type": "date"}
                }
            }
        },
        "usuarios": {
            "mappings": {
                "properties": {
                    "nome": {"type": "text"},
                    "email": {"type": "keyword"},
                    "cidade": {"type": "text"},
                    "ativo": {"type": "boolean"}
                }
            }
        },
        "pedidos": {
            "mappings": {
                "properties": {
                    "usuario_id": {"type": "keyword"},
                    "produto_id": {"type": "keyword"},
                    "quantidade": {"type": "integer"},
                    "total": {"type": "float"},
                    "data_pedido": {"type": "date"}
                }
            }
        },
        "reviews": {
            "mappings": {
                "properties": {
                    "produto_id": {"type": "keyword"},
                    "usuario_id": {"type": "keyword"},
                    "avaliacao": {"type": "integer"},
                    "comentario": {"type": "text"}
                }
            }
        }
    }

    for nome, body in indices.items():
        if not es.indices.exists(index=nome):
            es.indices.create(index=nome, body=body)
            print(f"Índice '{nome}' criado.")
        else:
            print(f"Índice '{nome}' já existe.")
