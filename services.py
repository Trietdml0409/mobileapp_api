from models import Product


default_products = [
    {
        "id": 10,
        "name": "PC RTX 3050 2023",
        "price": 11000000,
        "image": "https://file.hstatic.net/200000722513/file/7-gearvn-pc-gvn-intel-i3-3050-t8.png",
        "createdAt": "2026-3-1",
        "isBestSeller": True,
        "brandName": "NVIDIA",
        "liked": False,
    },
    {
        "id": 20,
        "name": "PC GTX 1050 2023",
        "price": 10000000,
        "image": "https://cdn.hstatic.net/products/200000420363/5888-5050_866c83a581f44117a7dcb6264f71490f_large.jpg",
        "createdAt": "2026-3-1",
        "isBestSeller": True,
        "brandName": "NVIDIA",
    },
    {
        "id": 30,
        "name": "PC Ryzen 5 5600G 2023",
        "price": 50000000,
        "image": "https://cdn.hstatic.net/products/200000420363/screenshot_2_e5ef09c2fb354e1b86a804bbb10e02a0_large.png",
        "createdAt": "2026-3-1",
        "isBestSeller": False,
        "brandName": "AMD",
    },
    {
        "id": 40,
        "name": "PC Ryzen 7 5800H Gen 1",
        "price": 45000000,
        "image": "https://cdn.hstatic.net/products/200000420363/_new_-_nh-sp-web_60fb8f06edf64bb5968c786a5aa36734_large.png",
        "createdAt": "2026-3-1",
        "isBestSeller": False,
        "brandName": "AMD",
    },
    {
        "id": 50,
        "name": "PC Ryzen 9 5900HX Gen 2",
        "price": 30000000,
        "image": "https://product.hstatic.net/200000420363/product/ls27dg502eexxv-2_a4e1e2792a654f66923442db7a43084b_large.png",
        "createdAt": "2026-3-1",
        "isBestSeller": False,
        "brandName": "AMD",
    },
]

def get_products_service():
    return default_products


def update_product_service(product_id: int, product: Product):
    has_product = False
    product_index = -1
    for i, p in enumerate(default_products):
        if p["id"] == product_id:
            has_product = True
            product_index = i
            break

    if not has_product:
        return None

    updated_product = {
        "id": product_id,
        "name": product.name,
        "price": product.price,
        "image": product.image,
        "createdAt": product.createdAt,
        "isBestSeller": product.isBestSeller,
        "brandName": product.brandName,
        "liked": product.liked,
    }

    # Update the product in the list by index
    default_products[product_index] = updated_product
    # Save: file/database
    # call model to save the product

    return updated_product
