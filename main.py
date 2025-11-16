from fastapi import FastAPI
from models import Product
app=FastAPI()

@app.get("/")
def greet():
    return "Welcome"

products = [
    Product(id=1, name="Phone", description="Budget smartphone", price=100, quantity=10),
    Product(id=2, name="Laptop", description="Lightweight performance laptop", price=800, quantity=5),
    Product(id=3, name="Headphones", description="Wireless noise-cancelling headphones", price=150, quantity=15),
    Product(id=6, name="Smartwatch", description="Fitness tracking smartwatch", price=120, quantity=8),
    Product(id=7, name="Tablet", description="10-inch display Android tablet", price=250, quantity=7)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return "Product not found"


@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product
