from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    if email == user_profile["email"]:
        return jsonify({"message": f"Login successful for {email}"})
    else:
        return jsonify({"message": "Login failed. Email not found."}), 401

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return jsonify(user_profile)

if __name__ == '__main__':
    app.run()
