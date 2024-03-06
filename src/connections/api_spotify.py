import requests
import base64
from configs import SPOTIFY_CONFIG


def connect_api():
    client_id = SPOTIFY_CONFIG['CLIENTID']
    client_secret = SPOTIFY_CONFIG['CLIENTSECRET']

    # Encoded da autenticação em base64
    string = client_id + ':' + client_secret
    string_bytes = string.encode('ascii')

    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode('ascii')

    # Requisição
    url = 'https://accounts.spotify.com/api/token'
    headers = {'Authorization': f'Basic {base64_string}',
               'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'grant_type': 'client_credentials'}
    response = requests.request('POST', url=url, headers=headers, data=payload)
    access_token = response.json()['access_token']

    return access_token


def import_data(endpoint):
    token = connect_api()
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.request('GET', url=endpoint, headers=headers)
    return response.json()

