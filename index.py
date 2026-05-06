from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "BGMI API is Live! Use /api/bgmi/YOUR_ID"

# Yeh hai main endpoint jo tum mang rahe ho
@app.route('/api/bgmi/<uid>')
def get_bgmi_user(uid):
    url = f"https://id-game-checker.p.rapidapi.com/bgmi/{uid}"
    
    headers = {
        "x-rapidapi-host": "id-game-checker.p.rapidapi.com",
        "x-rapidapi-key": "4031d8fca9mshd856dbf4ba5f5e5p1ad3bejsnd6dbde6aa518",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        # Yeh browser ko JSON data bhejega, download nahi karega
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
