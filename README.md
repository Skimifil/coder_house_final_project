# Pipeline de dados com Python

Esse projeto tem por objetivo criar uma pipeline de dados que pega informações de uma API e armazena em uma banco de dados não-relacional (MongoDB) e em relacional (MySQL).

## Pré-requisitos

### Arquivo de informações sensíveis
Crie um arquivo de informações sensiveis, como usuários e senhas, para serem acessados pela aplicação. Ele será importado pelo "from configs import MONGODB_CONFIG"

### MongoDB
Crie uma conta no MongoDB Atlas, crie um cluster, um usuário de acesso e configure as permissões de conexão.

Caso você não tenha o seu banco de dados criado no MongoDB Atlas, use o "database_create.py" para fazer isso.


## Referências
[Alura](https://www.alura.com.br/curso-online-pipeline-dados-integrando-python-mongodb-mysql)

[Millena Gená Pereira](https://github.com/millenagena)