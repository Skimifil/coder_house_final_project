from database_connect import connect_mongo


# Caso seu cluster ainda não tenha o banco de dados, você pode usar este script para criar e começar a popular
if __name__ == '__main__':
    # Chamando a conexão com o MongoDB
    client = connect_mongo()

    db = client["db_produtos"]
    collection = db["produtos"]
    #product = {"produto": "computador", "quantidade": 77}
    #collection.insert_one(product)

    databases = client.list_database_names()
    print(databases)

    produtos_inseridos = collection.find_one()
    print(produtos_inseridos)
