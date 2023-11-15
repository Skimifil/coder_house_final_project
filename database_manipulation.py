from database_connect import connect_mongo
from bson import ObjectId


def conecta_collection(database,coll):
    client = connect_mongo()

    db = client[database]
    collection = db[coll]
    return collection, client


# Caso seu cluster ainda não tenha o banco de dados, você pode usar este script para criar e começar a popular
def create_mongo():

    collection, client = conecta_collection("db_produtos","produtos")

    try:
        # Colocado uma informação genérica para validarmos se o banco foi criado mesmo.
        product = {"produto": "computador", "quantidade": 77}
        collection.insert_one(product)

        databases = client.list_database_names()
        print(databases)

        produtos_inseridos = collection.find_one()
        print(produtos_inseridos)
    except Exception as e:
        print(e)
    finally:
        client.close()


def insert_mongo(dados):

    collection, client = conecta_collection("db_produtos","produtos")

    try:
        collection.insert_many(dados)
        numero_de_docs_inseridos = len(dados.inser_ids)
        numero_de_docs_na_base = collection.count_documents({})
        print(f"Foram inseridos {numero_de_docs_inseridos} documentos no banco de dados, passando a existir {numero_de_docs_na_base} documentos.")
    except Exception as e:
        print(e)
    finally:
        client.close()


def list_mongo_db_info():

    collection, client = conecta_collection("db_produtos","produtos")

    try:
        numero_de_docs_na_base = collection.count_documents({})
        print(f"Atualmente, a base possui {numero_de_docs_na_base} documentos.")
    except Exception as e:
        print(e)
    finally:
        client.close()


def remove_doc_mongo(id_doc):

    collection, client = conecta_collection("db_produtos", "produtos")

    try:
        id_obj = ObjectId(id_doc)
        id_remover = collection.delete_one({"_id": id_obj})

        if id_remover.deleted_count == 1:
            print(f"Foi feito a remoção do documento de id {id_doc}, segue log da remoção: {id_remover}")
        else:
            print(f"Nenhum documento foi removido para o id {id_doc}")
    except Exception as e:
        print(e)
    finally:
        client.close()
