from flask import Blueprint, jsonify, session
import requests, random

bp = Blueprint("products", __name__) # a group of web paths called 'products'

@bp.route("/api/scrape") # This is the path to scrape products
def scrape():
    if "user" not in session: # If the user is not logged in
        return jsonify({"error": "unauthorized"}), 401 # Return an error message

    res = requests.get("https://fakestoreapi.com/products") ## Get product data from the website
    products = res.json()

   # # Add more products until there are at least 30
    idx = 200
    categories = ["shirts", "pants", "shoes", "watches", "perfumes"]
    while len(products) < 30:
        cat = random.choice(categories)
        products.append({
            "id": idx,
            "title": f"Sample {cat.title()} {idx}",
            "price": round(random.uniform(100, 3000), 2),
            "category": cat,
            "image": "https://via.placeholder.com/150"
        })
        idx += 1

    
    products = products[:30]
    return jsonify(products)
