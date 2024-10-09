from flask import Flask, jsonify, request

app = Flask(__name__)

# API keys dictionary
api_key = {
    "pixabay": "46218998-2ceeb9224ed3548d2618c757f",
    "secunsplash": "vbVL2Y7Uqq6_dlech1Uuo8DlzjwUZ_dFUAE_ORNRhHY",
    "unsplash": "6ieqbTayrqHcy9TnGDjG9FIaN3DKid-vT60oj1_klOk"
   
}

@app.route('/api', methods=['GET'])
def get_user():
    # Extract 'key' from query parameters
    key = request.args.get('key')

    if key in api_key:
        return jsonify({"api_key": api_key[key]}), 200
    else:
        return jsonify({"error": "Invalid API key"}), 401

if __name__ == '__main__':
    app.run(debug=True)
