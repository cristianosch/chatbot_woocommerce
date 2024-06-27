import requests
import base64
from config import WC_URL, CONSUMER_KEY, CONSUMER_SECRET

# Função para obter produtos do WooCommerce
def get_products(category=None):
    endpoint = f"{WC_URL}/products"
    auth = base64.b64encode(f"{CONSUMER_KEY}:{CONSUMER_SECRET}".encode()).decode()
    headers = {
        'Authorization': f'Basic {auth}'
    }
    params = {}
    if category:
        params['category'] = category

    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        products = response.json()
        if isinstance(products, list):
            return products
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API do WooCommerce: {e}")
        return None
    
def get_categories():
    endpoint = f"{WC_URL}/products/categories"
    auth = base64.b64encode(f"{CONSUMER_KEY}:{CONSUMER_SECRET}".encode()).decode()
    headers = {
        'Authorization': f'Basic {auth}'
    }

    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        categories = response.json()
        return categories
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API do WooCommerce: {e}")
        return None

# Obter e imprimir as categorias
categories = get_categories()
if categories:
    for category in categories:
        print(f"ID: {category['id']}, Nome: {category['name']}")


category_map = {
    # Use o ID correto obtido do WooCommerce
    'pizza': 18,
    'hamburguer': 19,  
    'pasta': 20,
    'saladas': 24,
    'sobremesas': 21,
    'vegano': 25,
    'bebidas': 22
}



def get_response(user_message):
    category_map = {
        'pizza': 18,
        'hamburguer': 19,
        'pasta': 20,
        'saladas': 24,
        'sobremesas': 21,
        'vegano': 25,
        'bebidas': 22
    }

    if 'produtos' in user_message:
        products = get_products()
        if not products:
            return "Desculpe, não consegui obter os produtos no momento."
        else:
            product_details = [f"{product['name']} - {product['permalink']}" for product in products]
            return f"Temos os seguintes produtos:\n" + "\n".join(product_details)

#PIZZA
    if 'pizzas' in user_message or 'pizza' in user_message:
        products = get_products(category=category_map['pizza'])
        if not products:
            return "Desculpe, não temos pizzas no momento."
        else:
            product_details = [f"{product['name']} - {product['permalink']}" for product in products]
            return f"Temos as seguintes pizzas:\n" + "\n".join(product_details)

#HAMBURGUER
    if 'hamburgueres' in user_message or 'hambúrgueres' in user_message:
        products = get_products(category=category_map['hamburguer'])
        if not products:
            return "Desculpe, não temos hambúrgueres no momento."
        else:
            product_details = [f"{product['name']} - {product['permalink']}" for product in products]
            return f"Temos os seguintes hambúrgueres:\n" + "\n".join(product_details)

#PASTA        
    if 'pasta' in user_message or 'pastas' in user_message or 'massas' in user_message:
        products = get_products(category=category_map['pasta'])
        if not products:
            return "Desculpe, não temos pasta no momento."
        else:
            product_details = [f"{product['name']} - {product['permalink']}" for product in products]
            return f"Temos as seguintes pastas:\n" + "\n".join(product_details)
        
#SALADA
    if 'salada' in user_message or 'saladas' in user_message:
        products = get_products(category=category_map['saladas'])
        if not products:
            return "Desculpe, não temos salada no momento."
        else:
            product_details = [f"{product['name']} - {product['permalink']}" for product in products]
            return f"Temos as seguintes saladas:\n" + "\n".join(product_details)

#SOBREMESA
    if 'sobremesa' in user_message or 'sobremesas' in user_message:
        products = get_products(category=category_map['sobremesas'])
        if not products:
            return "Desculpe, não temos sobremesa no momento."
        else:
            product_details = [f"{product['name']} - {product['permalink']}" for product in products]
            return f"Temos as seguintes sobremesas:\n" + "\n".join(product_details)

#VEGANO
    if 'vegano' in user_message or 'vegana' in user_message:
        products = get_products(category=category_map['vegano'])
        if not products:
            return "Desculpe, não temos comida vegana no momento."
        else:
            product_details = [f"{product['name']} - {product['permalink']}" for product in products]
            return f"Temos as seguintes comidas veganas:\n" + "\n".join(product_details)
        
#BEBIDAS
    if 'bebida' in user_message or 'bebidas' in user_message:
        products = get_products(category=category_map['bebidas'])
        if not products:
            return "Desculpe, nenhuma bebida no momento."
        else:
            product_details = [f"{product['name']} - {product['permalink']}" for product in products]
            return f"Temos as seguintes bebidas:\n" + "\n".join(product_details)


    if 'entrega' in user_message:
        return "A entrega é feita diretamente pelo site, Glovo ou Uber Eats."

    if 'horário de funcionamento' in user_message or 'horário' in user_message:
        return "Nosso horário de funcionamento é das 9 às 18 horas."

    if 'região' in user_message:
        return "Fazemos entregas apenas para a região central de Lisboa."

    return "Desculpe, não entendi sua pergunta. Você pode perguntar sobre nossos produtos, entrega, horário de funcionamento ou região de entrega."


