from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return {"status": "Server is running", "usage": "/api/bgmi/<id>"}

@app.route('/api/bgmi/<uid>')
def get_user(uid):
    url = f"https://id-game-checker.p.rapidapi.com/bgmi/{uid}"
    headers = {
        "x-rapidapi-host": "id-game-checker.p.rapidapi.com",
        "x-rapidapi-key": "4031d8fca9mshd856dbf4ba5f5e5p1ad3bejsnd6dbde6aa518"
    }
    try:
        r = requests.get(url, headers=headers)
        return jsonify(r.json())
    except:
        return jsonify({"error": "API Error"}), 500

# Ye line mat bhoolna
if __name__ == "__main__":
    app.run(debug=True)
