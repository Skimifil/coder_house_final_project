from mongodb_database_manipulation import *
from api_spotify import import_data

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    artist_id = '0TnOYISbd1XYRBk9myaseg'
    artistas = import_data(f'https://api.spotify.com/v1/artists/{artist_id}')
    insert_mongo("spotify", "artists", [artistas])

    artistas_albums = import_data(f'https://api.spotify.com/v1/artists/{artist_id}/albums')
    insert_mongo("spotify", "artists_albums", [artistas_albums])

    artistas_top_tracks = import_data(f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=BR')
    insert_mongo("spotify", "artists_top_tracks", [artistas_top_tracks])

