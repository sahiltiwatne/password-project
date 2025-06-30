from flask import Flask, render_template, request, jsonify
import random
import string
import re

app = Flask(__name__, static_folder='static')

# Function to check password strength
def check_password_strength(password):
    strength = 0
    tips = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "number": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    strength = sum(tips.values())  # Count how many conditions are met
    return strength, tips

# Function to generate a strong password
def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choices(characters, k=12))
    return password

# Route to serve the HTML page
@app.route('/')
def home():
    return render_template('final.html')

# Route to analyze password strength
@app.route('/check-password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get("password", "")

    strength, tips = check_password_strength(password)
    return jsonify({"strength": strength, "tips": tips})

# Route to generate a strong password
@app.route('/generate-password', methods=['GET'])
def suggest_password():
    password = generate_password()
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)
