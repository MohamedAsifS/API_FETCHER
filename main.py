from flask import Flask,jsonify,request


app = Flask(__name__)

api_key={
    "pixabay":"abcd",
    "pexels":"bcda"
}

@app.route('/get-user/<key>')
def get_user(key):
   
    
    
    
    if key in api_key:
        return jsonify(api_key[key]),200
    else:
        return jsonify({"error":"Invalid API key"}),401
    
   

    
    
    







if __name__ == '__main__':
    app.run(debug=True)