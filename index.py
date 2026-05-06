from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "BGMI API Server is Active!"

@app.route('/api/bgmi/<uid>')
def get_bgmi_user(uid):
    # RapidAPI URL with dynamic UID
    url = f"https://id-game-checker.p.rapidapi.com/bgmi/{uid}"
    
    headers = {
        "x-rapidapi-host": "id-game-checker.p.rapidapi.com",
        "x-rapidapi-key": "4031d8fca9mshd856dbf4ba5f5e5p1ad3bejsnd6dbde6aa518"
    }

    try:
        response = requests.get(url, headers=headers)
        # Seedha JSON return karega jo RapidAPI se aayega
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel ko iski zaroorat hoti hai
app.run()
