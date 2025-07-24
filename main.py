from setup_indices import criar_indices
from insert_data import inserir_dados
from queries import buscar_produtos_por_tag

def main():
    criar_indices()
    inserir_dados()

    resultado = buscar_produtos_por_tag("gamer")
    print("Resultados da busca:")
    for hit in resultado["hits"]["hits"]:
        print(hit["_source"])

if __name__ == "__main__":
    main()