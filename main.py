from setup_indices import criar_indices
from insert_data import inserir_dados
from queries import (
    buscar_produtos_por_tag,
    buscar_por_descricao,
    buscar_fuzzy_por_nome,
    buscar_por_tag_exata,
    buscar_produtos_ativos_com_preco_maximo,
    buscar_por_data_ultimos_dias,
    buscar_multiplos_indices,
    buscar_usuarios_por_cidade
)

def mostrar_resultados(resultados, titulo):
    print(f"\n🔎 {titulo}")
    for hit in resultados["hits"]["hits"]:
        print("-", hit["_source"])

def main():
    criar_indices()
    inserir_dados()

    # 1. Term exato (campo keyword)
    resultado1 = buscar_por_tag_exata("gamer")
    mostrar_resultados(resultado1, "Produtos com tag exata 'gamer'")

    # 2. Fuzzy match no nome
    resultado2 = buscar_fuzzy_por_nome("notbok")
    mostrar_resultados(resultado2, "Busca fuzzy por nome: 'notbok'")

    # 3. Match no campo descricao
    resultado3 = buscar_por_descricao("amortecimento reforçado")
    mostrar_resultados(resultado3, "Produtos com descrição contendo 'amortecimento reforçado'")

    # 4. Bool com filtro de preço
    resultado4 = buscar_produtos_ativos_com_preco_maximo("camiseta", 100)
    mostrar_resultados(resultado4, "Camisetas com preço até R$ 100")

    # 5. Range por data de cadastro (últimos 7 dias)
    resultado5 = buscar_por_data_ultimos_dias(7)
    mostrar_resultados(resultado5, "Produtos cadastrados nos últimos 7 dias")

    # 6. Multi índice
    resultado6 = buscar_multiplos_indices("gamer")
    mostrar_resultados(resultado6, "Busca por 'gamer' em múltiplos índices")

if __name__ == "__main__":
    main()
