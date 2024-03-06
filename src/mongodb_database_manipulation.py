from src.connections.database_connect import connect_mongo
from bson import ObjectId
from logger import configurar_logger

logger_mongodb_data_manipulation = configurar_logger("mongodb_database_manipulation",
                                                     "mongodb_database_manipulation.log")


def conecta_collection(database, coll):
    logger_mongodb_data_manipulation.info(
        f"[conecta_collection] Conectando na base de dados {database} e collection {coll}.")

    client = connect_mongo()
    db = client[database]
    collection = db[coll]

    logger_mongodb_data_manipulation.info(
        f"[conecta_collection] Conectado na base de dados {database} e collection {coll}.")
    return collection, client


def disconnect_connection(client):
    logger_mongodb_data_manipulation.info(f"[disconnect_connection] Desconectado da base de dados.")
    client.close()


# Caso seu cluster ainda não tenha o banco de dados, você pode usar este script para criar e começar a popular
def create_mongo(cr_database, cr_collection):
    logger_mongodb_data_manipulation.info(
        f"[create_mongo] Criando a base de dados {cr_database} e collection {cr_collection}.")
    collection, client = conecta_collection(cr_database, cr_collection)

    try:
        # Colocado uma informação genérica para validarmos se o banco foi criado mesmo.
        product = {"produto": "computador", "quantidade": 77}
        collection.insert_one(product)

        databases = client.list_database_names()
        print(databases)
        if databases:
            logger_mongodb_data_manipulation.info(
                f"[create_mongo] Base de dados {cr_database} e collection {cr_collection} criados.")

        produtos_inseridos = collection.find_one()
        print(produtos_inseridos)

    except Exception as e:
        logger_mongodb_data_manipulation.error(
            f"[create_mongo] Erro ao criar a base de dados {cr_database} e collection {cr_collection} devido ao erro {e}.")
        print(e)
    finally:
        disconnect_connection(client)


def insert_mongo(ins_database, ins_collection, dados):
    logger_mongodb_data_manipulation.info(
        f"[insert_mongo] Inserindo dados na base de dados {ins_database} e collection {ins_collection}.")
    collection, client = conecta_collection(ins_database, ins_collection)

    try:
        para_inserir = collection.insert_many(dados)
        numero_de_docs_inseridos = len(para_inserir.inserted_ids)
        numero_de_docs_na_base = collection.count_documents({})
        logger_mongodb_data_manipulation.info(
            f"[insert_mongo] Foram inseridos {numero_de_docs_inseridos} documentos no banco de dados {ins_database} e collection {ins_collection}, passando a existir {numero_de_docs_na_base} documentos.")
        print(
            f"Foram inseridos {numero_de_docs_inseridos} documentos no banco de dados, passando a existir {numero_de_docs_na_base} documentos.")
    except Exception as e:
        logger_mongodb_data_manipulation.error(f"[insert_mongo] Erro ao inserir documentos no banco de dados {ins_database} e collection {ins_collection} devido ao erro {e}.")
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
    logger_mongodb_data_manipulation.info(
        f"[remove_doc_mongo] Removendo dados na base de dados {rem_database} e collection {rem_collection}.")
    collection, client = conecta_collection(rem_database, rem_collection)

    try:
        id_obj = ObjectId(id_doc)
        id_remover = collection.delete_one({"_id": id_obj})

        if id_remover.deleted_count == 1:
            logger_mongodb_data_manipulation.info(
                f"[remove_doc_mongo] Foi feito a remoção do documento de id {id_doc}, segue log da remoção: {id_remover}.")
            print(f"Foi feito a remoção do documento de id {id_doc}, segue log da remoção: {id_remover}.")
        else:
            logger_mongodb_data_manipulation.info(
                f"[remove_doc_mongo] Nenhum documento foi removido para o id {id_doc}.")
            print(f"Nenhum documento foi removido para o id {id_doc}.")
    except Exception as e:
        logger_mongodb_data_manipulation.error(f"[remove_doc_mongo] Erro ao remover documentos no banco de dados {rem_database} e collection {rem_collection} devido ao erro {e}.")
        print(e)
    finally:
        disconnect_connection(client)


def alter_collunm(alt_database, alt_collection, nome_antigo, nome_novo):
    logger_mongodb_data_manipulation.info(
        f"[alter_collunm] Alterando um coluna da base de dados {alt_database} e collection {alt_collection}.")
    collection, client = conecta_collection(alt_database, alt_collection)
    try:
        collection.update_many({}, {"$rename": {nome_antigo: nome_novo}})
        valida_alterado = collection.find_one()
        logger_mongodb_data_manipulation.info(
            f"[alter_collunm] Foi feito a alteração, segue um documento de exemplo: {valida_alterado}.")
        print(f"Foi feito a alteração, segue um documento de exemplo: {valida_alterado}.")
    except Exception as e:
        logger_mongodb_data_manipulation.error(f"[alter_collunm] Erro ao alterar a coluna no banco de dados {alt_database} e collection {alt_collection} devido ao erro {e}.")
        print(e)
    finally:
        disconnect_connection(client)
