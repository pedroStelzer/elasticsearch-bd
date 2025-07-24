from elastic_client import es

def buscar_produtos_por_tag(tag):
    query = {
        "query": {
            "term": {
                "tags": tag
            }
        }
    }
    return es.search(index="produtos", body=query)

def buscar_usuarios_por_cidade(nome_cidade):
    query = {
        "query": {
            "match": {
                "cidade": nome_cidade
            }
        }
    }
    return es.search(index="usuarios", body=query)