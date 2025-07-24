from elastic_client import es
from datetime import datetime, timedelta

def buscar_produtos_por_tag(tag):
    query = {
        "query": {
            "term": {
                "tags": tag
            }
        }
    }
    return es.search(index="produtos", body=query)

def buscar_por_descricao(texto):
    query = {
        "query": {
            "match": {
                "descricao": texto
            }
        }
    }
    return es.search(index="produtos", body=query)

def buscar_fuzzy_por_nome(texto):
    query = {
        "query": {
            "match": {
                "nome": {
                    "query": texto,
                    "fuzziness": "AUTO"
                }
            }
        }
    }
    return es.search(index="produtos", body=query)

def buscar_por_tag_exata(tag):
    query = {
        "query": {
            "term": {
                "tags": tag
            }
        }
    }
    return es.search(index="produtos", body=query)

def buscar_produtos_ativos_com_preco_maximo(palavra_chave, preco_maximo):
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"nome": palavra_chave}},
                    {"range": {"preco": {"lte": preco_maximo}}}
                ]
            }
        }
    }
    return es.search(index="produtos", body=query)

def buscar_por_data_ultimos_dias(dias):
    data_limite = (datetime.now() - timedelta(days=dias)).isoformat()
    query = {
        "query": {
            "range": {
                "data_cadastro": {
                    "gte": data_limite
                }
            }
        }
    }
    return es.search(index="produtos", body=query)

def buscar_multiplos_indices(termo, indices=["produtos", "reviews"]):
    query = {
        "query": {
            "multi_match": {
                "query": termo,
                "fields": ["nome", "descricao"]
            }
        }
    }
    return es.search(index=",".join(indices), body=query)

def buscar_usuarios_por_cidade(nome_cidade):
    query = {
        "query": {
            "match": {
                "cidade": nome_cidade
            }
        }
    }
    return es.search(index="usuarios", body=query)