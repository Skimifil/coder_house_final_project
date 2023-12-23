# Pipeline de dados com Python

Esse projeto tem por objetivo criar uma pipeline de dados que pega informações de uma API e armazena em uma banco de dados não-relacional e em relacional.

Irei usar as tecnologias como:
Banco de dados:
1. MongoDB
2. ScyllaDB
3. MySQL

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

MYSQL_CONFIG = {
    'MYSQLDBUSER': 'user',
    'MYSQLDBPASSWORD': 'senha',
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

## Documentação dos códigos

### main.py

Função main:
    
    É a chamada da pipeline, por ela que começa todo o fluxo, nela é chamada algumas funções do código "database_manipulation.py" (mains informações abaixo).

Função import_data:

    Por ela é feita a chamada da API, mas deve ser alterado para um arquivo externo, ali foi para deixar mais prático os testes.


### database_connect.py

Função connect_mongo:

    Função para conexão no Atlas MongoDB, ele pega as informações de conexão, monta a uri de acesso e retorna o "client" para ser usado na requisições durante o pipeline.

### database_manipulation.py

Função conecta_collection:

    Utilizando a função de conexão no MongoDB, ele faz a conexão na 'collection' (base de dados) para iniciar a manipulação dos dados na base.

Função desconect_collection:

    Para fins de boas praticas, foi criado a função para fazer o 'logout' no MongoDB.

Função create_mongo:

    Durante a manipulação, caso a 'collection' não exista, você pode cria-la com este função. Lembrando que essa função precisa ser alterada conforme os dados que tiver sendo usado.

Função insert_mongo:

    Função que faz a inserção dos dados na 'collection', ele precisa ser alterado para se encaixar com o dataframe usado.

Função list_mongo_db_info:

    Função para mostrar as informações do MongoDB.

Função list_mongo_db_collection_info:

    Função para mostrar as informações da Collection.

Função remove_doc_mongo:

    Função que remove um documento da 'collection'.

Função alter_collunm:

    Função para alterar o nome de alguma coluna da 'collection'.


### data_manipulation.ipynb

Criei esse Jupyter notebook para manipular o dados da 'collection', ele é pra testar e avaliar os dados armazenados.

## Referências
[Alura](https://www.alura.com.br/curso-online-pipeline-dados-integrando-python-mongodb-mysql)

[Millena Gená Pereira](https://github.com/millenagena)

[MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register)

[TopTal](https://www.toptal.com/developers/gitignore)

[Spotify for Developers](https://developer.spotify.com/documentation/web-api/reference/get-an-artist)