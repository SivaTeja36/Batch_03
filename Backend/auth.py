from flask import Blueprint, request, session, jsonify #Blueprint: Helps group related web paths together, request: Gets data sent by the user, session: Saves info about the user while they use the app, jsonify: Sends data back to the user in JSON format. 

auth = Blueprint("auth", __name__) # Make a group of paths called 'auth'
USER = {"username": "admin", "password": "admin123"} # Set up a user with a name and password

@auth.route("/api/login", methods=["POST"]) # This is the login path
def login():
    data = request.json # Get user data which was sent
    if data["username"] == USER["username"] and data["password"] == USER["password"]: # verifies if the username and password are correct
        session["user"] = data["username"] #if it was correct
        return jsonify({"message": "ok"}), 200 # logged in successfully
    return jsonify({"message": "invalid"}), 401 # if it was not correct, return an error message

@auth.route("/api/logout") # This is the logout path
def logout():
    session.pop("user", None) # Log out the user
    return jsonify({"message": "ok"}) # Return a message saying the user has logged out

@auth.route("/api/check-auth") # This checks if the user is signed in.
def check_auth():
    return jsonify({"auth": "user" in session})# Say if the user is logged in or not
