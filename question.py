from flask import Flask, request, jsonify, make_response
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your_default_secret_key')

# Predefined user credentials (for demo purposes only)
USER_DATA = {
    "username": "testuser",
    "password": "testpassword"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json

    # Check if username and password are provided
    if not data or not data.get('username') or not data.get('password'):
        return make_response(jsonify({"error": "Missing username or password"}), 400)

    # Validate user credentials
    if data['username'] == USER_DATA['username'] and data['password'] == USER_DATA['password']:
        return jsonify({"message": "Login successful!"})
    else:
        return make_response(jsonify({"error": "Invalid credentials"}), 401)

@app.route('/')
def index():
    return "Welcome to the Google App Engine user validation app!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
