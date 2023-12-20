from mongodb_database_manipulation import *
from api_spotify import import_data



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    connect_mongo()
    artistas = import_data('https://api.spotify.com/v1/artists/0TnOYISbd1XYRBk9myaseg')
    insert_mongo("db_produtos", "produtos", artistas)
    #list_mongo_db_info()
    list_mongo_db_collection_info()
