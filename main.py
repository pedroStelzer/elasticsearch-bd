from elasticsearch import Elasticsearch

# Conectando ao Elasticsearch local
es = Elasticsearch("http://localhost:9200")

# Verificando se o servidor está online
if es.ping():
    print("🟢 Elasticsearch conectado com sucesso!")
else:
    print("🔴 Erro ao conectar ao Elasticsearch")

# Criando um índice (com mapeamento simples)
index_name = "produtos"

mapeamento = {
    "mappings": {
        "properties": {
            "nome": {"type": "text"},
            "categoria": {"type": "keyword"},
            "preco": {"type": "float"},
            "em_estoque": {"type": "boolean"}
        }
    }
}

# Criar índice se não existir
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body=mapeamento)
    print(f"✅ Índice '{index_name}' criado.")
else:
    print(f"ℹ️ Índice '{index_name}' já existe.")

# Inserindo documentos
produtos = [
    {"nome": "Notebook Gamer", "categoria": "Eletrônicos", "preco": 4500.00, "em_estoque": True},
    {"nome": "Teclado Mecânico", "categoria": "Periféricos", "preco": 350.00, "em_estoque": True},
    {"nome": "Cadeira Gamer", "categoria": "Móveis", "preco": 900.00, "em_estoque": False},
]

for i, doc in enumerate(produtos):
    es.index(index=index_name, id=i+1, body=doc)

print("📦 Produtos inseridos!")

# Consulta: buscar produtos da categoria 'Eletrônicos'
query = {
    "query": {
        "term": {
            "categoria": {
                "value": "Eletrônicos"
            }
        }
    }
}


res = es.search(index=index_name, body=query)

print("\n🔍 Resultado da busca por categoria 'Eletrônicos':")
for hit in res['hits']['hits']:
    print(f"- {hit['_source']['nome']} (R${hit['_source']['preco']})")
