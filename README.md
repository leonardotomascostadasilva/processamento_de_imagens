# Image Service API
Este projeto é uma aplicação web desenvolvida em Python usando Flask, organizada segundo os princípios da Clean Architecture. O serviço permite o upload, listagem e consulta de imagens armazenadas em um banco de dados PostgreSQL.

# Rotas Disponíveis
## Upload de Imagens
- **Descrição**: Permite o upload de arquivos de imagem no formato .tif para o banco de dados.
- **Método HTTP**: POST
- **URL**: /upload
- **Parâmetros**:
    - files (form-data): Arquivo TIFF a ser enviado.
    - context (form-data, opcional): Contexto adicional para categorizar a imagem.
- **Respostas**:
    - 200 OK: Imagem armazenada com sucesso.
    - 400 Bad Request: Erro na validação do arquivo.
    - 500 Internal Server Error: Erro interno no processamento.
**Exemplo com curl**:
```bash
curl -X POST http://127.0.0.1:5000/upload \
     -F "files=@path/to/image.tif" \
     -F "context=exemplo-contexto"

```
## Listar Imagens
- **Descrição**: Retorna uma lista de imagens com base no campo context.
- **Método HTTP**: GET
- **URL**: /images
- **Parâmetros (query string)**:
    - context (opcional): Contexto usado para filtrar imagens.
- **Respostas**:
    - 200 OK: Lista de imagens no formato JSON.
    - 500 Internal Server Error: Erro interno no processamento.
**Exemplo com curl**:
```bash
curl -X GET http://127.0.0.1:5000/images

curl -X GET "http://127.0.0.1:5000/images?context=exemplo-contexto"

```

**Exemplo de resposta**:
```json
[
    {
        "id": 1,
        "name": "example.tif",
        "context": "exemplo-contexto",
        "created_at": "2025-01-18T12:34:56"
    },
    {
        "id": 2,
        "name": "another_example.tif",
        "context": "outro-contexto",
        "created_at": "2025-01-18T14:22:33"
    }
]
```
## Buscar Dados da Imagem
- **Descrição**: Retorna os dados binários de uma imagem específica, permitindo que o cliente visualize ou baixe o arquivo.
- **Método HTTP**: GET
- **URL**: /images/<image_id>/data
- **Parâmetros**:
    - image_id: ID da imagem no banco de dados.
**Respostas**:
    - 200 OK: Retorna os dados binários da imagem.
    - 404 Not Found: Imagem não encontrada.
    - 500 Internal Server Error: Erro interno no processamento.
**Exemplo com curl**:
```bash
curl -X GET http://127.0.0.1:5000/images/1/data --output image.tif
```

# Configuração do Banco de Dados
A aplicação utiliza PostgreSQL como banco de dados. Certifique-se de configurar a string de conexão no arquivo de configuração (infrastructure/database.py):

```python
DATABASE_URL = "postgresql://postgresql:password@localhost/mydatabase"
```

## Estrutura da Tabela
```sql
CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    image_data BYTEA,
    context TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

# Organização do Código
O projeto segue o padrão Clean Architecture, com os seguintes módulos:

- domain: Contém as entidades principais do sistema, como ImageModel.
- application: Lida com os casos de uso, como upload, listagem e consulta de imagens.
- infrastructure: Contém a lógica de acesso ao banco de dados e configurações.
- webapi: Define as rotas HTTP e a interface com o cliente.

