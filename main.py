from database_connect import connect_mongo
from database_manipulation import *
import requests


def import_data(url):
    response = requests.get(url)
    return response.json()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    connect_mongo()
    docs = import_data("https://labdados.com/produtos")
    insert_mongo(docs)
    list_mongo_db_info()
    remove_doc_mongo("6552d722b1b727b297c1ad49")
    #list_mongo_db_info()
    #list_mongo_db_collection_info()
    alter_collunm("lon", "Longitude")
