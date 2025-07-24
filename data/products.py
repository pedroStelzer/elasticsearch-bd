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
    }
]
