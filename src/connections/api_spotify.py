import requests
import base64
from src.connections.configs import SPOTIFY_CONFIG
from src.logger import configurar_logger

logger_api_connection = configurar_logger("api_connection",
                                          "api_connection.log")


def connect_api():
    try:
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

        if access_token:
            logger_api_connection.info(f"[connect_api] Conectado na API do Spotify.")

        return access_token
    except Exception as e:
        logger_api_connection.error(
            f"[connect_api] Erro ao conectar na API, erro: {e}.")
        print(f"Erro ao conectar na API, erro: {e}.")


def import_data(endpoint):
    try:
        token = connect_api()
        headers = {'Authorization': f'Bearer {token}'}

        response = requests.request('GET', url=endpoint, headers=headers)
        if response.status_code == 200:
            logger_api_connection.info(f"[import_data] Importação feita com sucesso.")

        return response.json()

    except Exception as e:
        logger_api_connection.error(f"[import_data] Erro ao importar, devido ao erro {e}.")
