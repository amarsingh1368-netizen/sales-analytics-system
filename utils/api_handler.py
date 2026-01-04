import requests

def fetch_all_products():
    """
    Fetches all products from DummyJSON API

    Returns: list of product dictionaries
    """
    url = "https://dummyjson.com/products?limit=100"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raises error for 4xx/5xx

        data = response.json()
        products = []

        for p in data.get('products', []):
            products.append({
                'id': p.get('id'),
                'title': p.get('title'),
                'category': p.get('category'),
                'brand': p.get('brand'),
                'price': p.get('price'),
                'rating': p.get('rating')
            })

        print(f"Successfully fetched {len(products)} products from API")
        return products

    except requests.exceptions.RequestException as e:
        print("Failed to fetch products from API:", e)
        return []

def create_product_mapping(api_products):
    """
    Creates a mapping of product IDs to product info
    """
    product_mapping = {}

    for product in api_products:
        product_id = product.get('id')

        if product_id is None:
            continue

        product_mapping[product_id] = {
            'title': product.get('title'),
            'category': product.get('category'),
            'brand': product.get('brand'),
            'rating': product.get('rating')
        }

    return product_mapping
