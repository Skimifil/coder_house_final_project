# Pipeline de dados com Python

Esse projeto tem por objetivo criar uma pipeline de dados que pega informações de uma API e armazena em uma banco de dados não-relacional.

Irei usar as tecnologias como:
Banco de dados:
1. MongoDB

Linguagem:
1. Python

Frameworks:
1. Request
2. Jupyter
3. Spark


## Pré-requisitos

### Arquivo de requirements

Dentro da estrutura do código, existe o arquivo "requirements.txt", nele vai constar todas as dependências do pipeline.

### Arquivo de GitIgnore

Ja estruturado o arquivo de ".gitignore" com ajuda do site [TopTal](https://www.toptal.com/developers/gitignore).

### Arquivo de informações sensíveis
Crie um arquivo de informações sensiveis, como usuários, senhas e 'secret's para serem acessados pela aplicação. Ele será importado pelo "from configs import MONGODB_CONFIG"

O arquivo deve se chamar 'configs.py' e deve ter o seguinte conteúdo:
```python
MONGODB_CONFIG = {
    'MONGODBUSER': 'user',
    'MONGODBPASSWORD': 'senha',
    'MONGODBSERVER': 'server_dns',
}

SPOTIFY_CONFIG = {
    'CLIENTID': 'client_id',
    'CLIENTSECRET': 'client_secret',
}
```

### MongoDB
Crie uma conta no MongoDB Atlas, crie um cluster, um usuário de acesso e configure as permissões de conexão.

[MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register)

Ao criar seu banco de dados crie seguindo a seguinte estrutura:

Banco de dados: spotify

Collections:
1. artists
2. artists_albums
3. artists_top_tracks

### Spotify API

Será usado os dados da API do Spotify para o Pipeline no projeto final, então ja preparei algumas coisas pra isso. É preciso se cadastrar no 'Spotify for Developers' e seguir os passos de criação de 'app'.

## Estrutura do projeto

````shell
-> .gitignore
-> README.md
-> requirements.txt
-> logs\
  |
    -- arquivos_logs.log
-> notebooks\
  |
    -- data_manipulation.ipynb
-> src\
  |
    -- logger.py
    -> main.py
    -- mongodb_database_manipulation.py
    -- utils.py
    connections\
      |
        -- database_connect.py
        -- api_spotify.py
        -- config.py
````

Pasta principal
````shell
README.md (O arquivo README)
requirements.txt (Lista de dependências do projeto)
.gitignore (Lista de arquivos a serem ignorados pelo Git)
````

Subpastas
````shell
logs:
     São gerados os logs das funções de cada funcionalidade:
        database_connection.log (Arquivo de log de conexão ao banco de dados)
        mongodb_database_manipulation.log (Arquivo de log de manipulação do banco de dados MongoDB)
        api_connection.log (Arquivo de log da API)
notebooks:
    data_manipulation.ipynb (Notebook Jupyter para modelagem de dados)
src:
    connections:
        configs.py (Arquivo de configuração do projeto, contendo as informações de acesso ao MongoDB e quais são os endpoints da API)
        database_connect.py (Arquivo para conexão ao banco de dados MongoDB)
        api_spotify.py (Arquivo para conexão na API)
    main.py (Arquivo principal do projeto)
    logger.py (Arquivo de configuração do logger e geração de logs)
    mongodb_database_manipulation.py (Arquivo para manipulação do banco de dados MongoDB)
    utils.py (Arquivo de utilidades)
````

## Referências
[Coder House](https://www.coderhouse.com/br/)

[Alura](https://www.alura.com.br/curso-online-pipeline-dados-integrando-python-mongodb-mysql)

[Millena Gená Pereira](https://github.com/millenagena)

[MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register)

[TopTal](https://www.toptal.com/developers/gitignore)

[Spotify for Developers](https://developer.spotify.com/documentation/web-api/reference/get-an-artist)