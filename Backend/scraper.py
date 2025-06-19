import requests # Importing the requests library to make HTTP requests
from flask import Blueprint, jsonify # Helps make a group of web paths and send data back

scraper_blueprint = Blueprint('scraper', __name__)
SCRAPE_URL = "https://fakestoreapi.com/products" # # The website link to get product data


@scraper_blueprint.route('/scrape', methods=['GET']) # This makes '/scrape' run this function when someone visits it
def scrape():
    try:
        res = requests.get(SCRAPE_URL) # Go to the website and get the data
        products = res.json() # the data into Python objects
        return jsonify(products)  # Send the products back to the user
    except Exception as e:
        return jsonify({"error": str(e)}), 500 # If something goes wrong, send an error message back


