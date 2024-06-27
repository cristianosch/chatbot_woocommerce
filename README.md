# WooCommerce Chatbot

Este é um chatbot simples em Python usando Flask para interagir com a API do WooCommerce.

## Configuração

1. Clone o repositório:
    ```bash
    git clone https://github.com/cristianosch/chatbot_woocommerce.git
    cd chatbot_woocommerce
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    .\venv\Scripts\activate  # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Crie e configure as credenciais da API no arquivo `config.py`.

Exemplo:
config.py 

    WC_URL = 'https://seu-site/wp-json/wc/v3'
    CONSUMER_KEY = 'ck_key'
    CONSUMER_SECRET = 'cs_secret'


1. Execute o aplicativo:
    ```bash
    python app.py
    ```

2. O chatbot estará acessível em `http://localhost:5000/chatbot`.

## Uso

Envie uma requisição POST para `http://localhost:5000/chatbot` com o seguinte payload:
```json
{
    "message": "Quais produtos vocês têm?"
}

## Teste No terminal de comando

curl -X POST http://localhost:5000/chatbot -H "Content-Type: application/json" -d '{"message": "Quais produtos vocês têm?"}'
curl -X POST http://localhost:5000/chatbot -H "Content-Type: application/json" -d '{"message": "Quais pizzas vocês têm?"}'
curl -X POST http://localhost:5000/chatbot -H "Content-Type: application/json" -d '{"message": "Quais saladas vocês têm?"}'
curl -X POST http://localhost:5000/chatbot -H "Content-Type: application/json" -d '{"message": "Qual comida vegana vocês tem?"}'
curl -X POST http://localhost:5000/chatbot -H "Content-Type: application/json" -d '{"message": "Quais sobremesas vocês têm?"}'
curl -X POST http://localhost:5000/chatbot -H "Content-Type: application/json" -d '{"message": "Quais pastas vocês têm?"}'
curl -X POST http://localhost:5000/chatbot -H "Content-Type: application/json" -d '{"message": "Quais hamburgueres vocês têm?"}'
curl -X POST http://localhost:5000/chatbot -H "Content-Type: application/json" -d '{"message": "Como é feita a entrega?"}'
curl -X POST http://localhost:5000/chatbot -H "Content-Type: application/json" -d '{"message": "Qual é o horário de funcionamento?"}'
curl -X POST http://localhost:5000/chatbot -H "Content-Type: application/json" -d '{"message": "Qual é a região de entrega?"}'


