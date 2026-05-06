from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "API is Working! Use /api/bgmi/UID"

@app.route('/api/bgmi/<uid>')
def get_user(uid):
    url = f"https://id-game-checker.p.rapidapi.com/bgmi/{uid}"
    headers = {
        "x-rapidapi-host": "id-game-checker.p.rapidapi.com",
        "x-rapidapi-key": "4031d8fca9mshd856dbf4ba5f5e5p1ad3bejsnd6dbde6aa518"
    }
    try:
        response = requests.get(url, headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel handle karega, lekin ye line safety ke liye
if __name__ == "__main__":
    app.run()
