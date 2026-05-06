from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/bgmi/<uid>')
def get_username(uid):
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

# Ye line local testing ke liye hai, Vercel ise ignore kar dega
if __name__ == "__main__":
    app.run()
