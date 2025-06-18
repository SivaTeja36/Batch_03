from flask import Flask
from flask_cors import CORS
from auth import auth
from products import bp as products_bp

app = Flask(__name__)
app.secret_key = "supersecretkey"
CORS(app, supports_credentials=True)

app.register_blueprint(auth)
app.register_blueprint(products_bp)

if __name__ == "__main__":
    app.run(debug=True)
