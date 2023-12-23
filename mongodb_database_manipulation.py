from database_connect import connect_mongo
from bson import ObjectId


def conecta_collection(database, coll):
    client = connect_mongo()

    db = client[database]
    collection = db[coll]
    return collection, client


def disconnect_connection(client):
    client.close()


# Caso seu cluster ainda não tenha o banco de dados, você pode usar este script para criar e começar a popular
def create_mongo(cr_database, cr_collection):
    collection, client = conecta_collection(cr_database, cr_collection)

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
        disconnect_connection(client)


def insert_mongo(ins_database, ins_collection, dados):
    collection, client = conecta_collection(ins_database, ins_collection)

    try:
        para_inserir = collection.insert_many(dados)
        numero_de_docs_inseridos = len(para_inserir.inserted_ids)
        numero_de_docs_na_base = collection.count_documents({})
        print(
            f"Foram inseridos {numero_de_docs_inseridos} documentos no banco de dados, passando a existir {numero_de_docs_na_base} documentos.")
    except Exception as e:
        print(e)
    finally:
        disconnect_connection(client)


def list_mongo_db_info(dbinfo_database, dbinfo_collection):
    collection, client = conecta_collection(dbinfo_database, dbinfo_collection)

    try:
        numero_de_docs_na_base = collection.count_documents({})
        print(f"Atualmente, a base possui {numero_de_docs_na_base} documentos.")
    except Exception as e:
        print(e)
    finally:
        disconnect_connection(client)


def list_mongo_db_collection_info(collinfo_database, collinfo_collection):
    collection, client = conecta_collection(collinfo_database, collinfo_collection)

    try:
        for doc in collection.find():
            print(doc)
    except Exception as e:
        print(e)
    finally:
        disconnect_connection(client)


def remove_doc_mongo(rem_database, rem_collection, id_doc):
    collection, client = conecta_collection(rem_database, rem_collection)

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
        disconnect_connection(client)


def alter_collunm(alt_database, alt_collection, nome_antigo, nome_novo):
    collection, client = conecta_collection(alt_database, alt_collection)
    try:
        collection.update_many({}, {"$rename": {nome_antigo: nome_novo}})
        valida_alterado = collection.find_one()
        print(f"Foi feito a alteração, segue um documento de exemplo: {valida_alterado}")
    except Exception as e:
        print(e)
    finally:
        disconnect_connection(client)
