from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from src.connections.configs import MONGODB_CONFIG
from src.logger import configurar_logger

logger_database_connection = configurar_logger("database_connection",
                                               "database_connection.log")


def connect_mongo():
    """
        Estabelece uma conexão com o banco de dados MongoDB.

        Retorna:
        - pymongo.database.Database ou None: Retorna o objeto de banco de dados pymongo.database.Database
          se a conexão for bem-sucedida. Retorna None se houver falha na conexão.

        Exceções:
        - Exception: Se ocorrer algum erro durante a conexão com o MongoDB, uma exceção será levantada.

        Exemplo:
        >>> db = connect_mongo()
    """
    mongo_user = MONGODB_CONFIG['MONGODBUSER']
    mongo_pass = MONGODB_CONFIG['MONGODBPASSWORD']
    mongo_server = MONGODB_CONFIG['MONGODBSERVER']
    uri = f"mongodb+srv://{mongo_user}:{mongo_pass}@{mongo_server}/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        logger_database_connection.info(f"[connect_mongo] Pinged your deployment. You successfully connected to MongoDB!")
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        logger_database_connection.error(
            f"[connect_mongo] Erro ao conectar no MongoDB, erro: {e}")
        print(f"Erro ao conectar no MongoDB, erro: {e}")
