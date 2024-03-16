# add - new product 
# product_id_func = "8726062301529"
import requests

product_title_func = "AAA 7 - Test product"
product_price_func = 100.00
product_sku_func = 23
product_barcode_func = 97654321
product_stock_func = 991
product_option1_func = "Height: 14.0 cm x Width: 16.0 cm x Length: 70.0 cm"
brand = 'OK'
product_description_func = 'This is the description of the project'


PrivateApp_api_token = "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5"
api_key = "19b3480df3e1a14099e5e9399471245"
api_secret_key = "aab63c72eb904fbd1ac4278c6ac1452"
shop_name = "2ahyjt-gt"
collection_id = '2584340299988'


image_urls =  ["https://storage.googleapis.com/floralogistics-image-service-prod/public-images/92169df1fca04beb9ca5ffb627fe3fa245233174ec7c4b9fbf3334c06ce183a6/thumbnail_600.jpg",
               "https://storage.googleapis.com/floralogistics-image-service-prod/public-images/d0f0f53cdc774af1a8169ef95a2c80ac63f82a7ca1134e7d8f9c6a5530930f03/thumbnail_600.jpg"]


# Function to format image URLs
def format_image_urls(image_urls):
    formatted_urls = [{"position": i + 1, "src": url} for i, url in enumerate(image_urls)]
    return formatted_urls

# Update headers with your access token
headers = {
    'X-Shopify-Access-Token': PrivateApp_api_token,
    'Content-Type': 'application/json',
}

# Format image URLs
formatted_urls = format_image_urls(image_urls)

# Initialize json_data with your product data
json_data = {
    "product": {
        "handle": product_title_func.replace(' ','-').replace('Ø','-').replace('↕', '-').replace('+','-') + '-'+ str(product_sku_func),
        "title": product_title_func,
        "body_html": product_description_func,
        "images": formatted_urls,        
        "variants": [
            {
                "price": product_price_func,
                "sku": str(product_sku_func),
                "barcode": str(product_barcode_func),
                "option1": product_option1_func,
                "weight": 20,
                "weight_unit": 'g',
                "inventory_tracker": "shopify",
                "inventory_management": "shopify",
                "fulfillment_service": "manual",
                "inventory_policy": "deny",
            }
        ],
        "options": [
            {
                "name": "Dimention",
                "position": 1,
                "values": [product_option1_func]
            }
        ],
        "status": "draft",
        "collection_ids": [collection_id],
        "published_scope": "global",
        "published": True,
        "vendor": "Ever",
        "Location": "Pakistan",
    }
}

# Make POST request to Shopify API
response = requests.post(
    f'https://{shop_name}.myshopify.com/admin/api/2024-01/products.json',
    headers=headers,
    json=json_data,
)

# Print response
print(response.json())
print(response.status_code)

if response.status_code == 201: # if response is 200, we will extract the inventory item id , and put in data2
    response1_json = response.json()
    product_inventory_item_id = int(response1_json.get('product').get('variants')[0].get('inventory_item_id'))

    data2 = {
        'location_id': 74698260692,
        'inventory_item_id': product_inventory_item_id,
        'available': product_stock_func,
        }

    response2 = requests.post(f'https://{shop_name}.myshopify.com/admin/api/2024-01/inventory_levels/set.json',headers=headers,json=data2)
    print(response2.status_code)
    print(response2.json())
