from datetime import datetime

produtos = [
    {
        "id": "p1",
        "nome": "Notebook Gamer X",
        "descricao": "Notebook com placa de vídeo dedicada e 16GB RAM.",
        "preco": 4500.00,
        "categoria": "Informática",
        "estoque": 20,
        "disponivel": True,
        "tags": ["gamer", "notebook", "informática"],
        "data_cadastro": datetime.now()
    },
    {
        "id": "p2",
        "nome": "Fone Bluetooth X100",
        "descricao": "Fone com cancelamento de ruído e longa duração de bateria.",
        "preco": 299.90,
        "categoria": "Áudio",
        "estoque": 50,
        "disponivel": True,
        "tags": ["fone", "bluetooth", "áudio"],
        "data_cadastro": datetime.now()
    },
    {
        "id": "p3",
        "nome": "Cafeteira Elétrica Inox",
        "descricao": "Design moderno com timer programável e filtro permanente.",
        "preco": 219.90,
        "tags": ["cozinha", "cafeteira", "eletrodoméstico"],
        "data_cadastro": datetime.now()
    },
    {
        "id": "p4",
        "nome": "Liquidificador Turbo",
        "descricao": "Alta potência com 6 lâminas inoxidáveis para receitas diversas.",
        "preco": 189.00,
        "tags": ["cozinha", "liquidificador", "eletrodoméstico"],
        "data_cadastro": datetime.now()
    },
    {
        "id": "p5",
        "nome": "Camisa Dry Fit Preta",
        "descricao": "Ideal para atividades físicas com tecido respirável.",
        "preco": 89.90,
        "tags": ["camisa", "esporte", "preta"],
        "data_cadastro": datetime.now()
    },
    {
        "id": "p6",
        "nome": "Tênis Corrida Pro",
        "descricao": "Amortecimento avançado para melhor performance.",
        "preco": 349.90,
        "tags": ["tênis", "corrida", "esporte"],
        "data_cadastro": datetime.now()
    },
    {
        "id": "p7",
        "nome": "Fone Bluetooth Noise Cancelling",
        "descricao": "Áudio limpo com cancelamento ativo de ruído.",
        "preco": 599.90,
        "tags": ["fone", "bluetooth", "áudio"],
        "data_cadastro": datetime.now()
    },
    {
        "id": "p8",
        "nome": "Mouse Gamer RGB",
        "descricao": "Sensor de alta precisão e iluminação personalizável.",
        "preco": 199.90,
        "tags": ["gamer", "mouse", "periféricos"],
        "data_cadastro": datetime.now()
    },
    {
        "id": "p9",
        "nome": "Smartphone Z12",
        "descricao": "Câmera tripla com IA, 128GB de memória e bateria de longa duração.",
        "preco": 2299.00,
        "tags": ["smartphone", "celular", "tecnologia"],
        "data_cadastro": datetime.now()
    },
    {
        "id": "p10",
        "nome": "Teclado Mecânico ABNT2",
        "descricao": "Teclado com switches silenciosos e iluminação RGB.",
        "preco": 289.90,
        "tags": ["gamer", "teclado", "periféricos"],
        "data_cadastro": datetime.now()
    }
]
