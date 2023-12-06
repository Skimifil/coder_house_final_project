from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from configs import MONGODB_CONFIG


def connect_mongo():

    mongo_user = MONGODB_CONFIG['MONGODBUSER']
    mongo_pass = MONGODB_CONFIG['MONGODBPASSWORD']
    mongo_server = MONGODB_CONFIG['MONGODBSERVER']
    uri = f"mongodb+srv://{mongo_user}:{mongo_pass}@{mongo_server}/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)
