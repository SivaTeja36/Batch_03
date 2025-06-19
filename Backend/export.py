import csv
from flask import send_file #send files to the user

def export_to_csv():
    import json
    with open("data.json") as f: # Open the data.json file
        data = json.load(f) # Reads  data from the file


    with open("products.csv", "w", newline="", encoding='utf-8') as file: # Make a new CSV file
        writer = csv.DictWriter(file, fieldnames=["name", "price", "rating", "image", "url"])  # Set up the columns
        writer.writeheader() # Write the column names
        writer.writerows(data) # Write all the data to the file

    return send_file("products.csv", as_attachment=True) # user can download the CSV file
