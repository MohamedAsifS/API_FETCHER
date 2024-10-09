from flask import Flask,jsonify,request


app = Flask(__name__)

api_key={
    "pixabay":"46218998-2ceeb9224ed3548d2618c757f",
    "pexels":"3CAbImegKz2Rb9YhSfOpJ9fLNHRG3x25C5idvisk2otyUbURHiSX1KVQ",
    "unsplash":"6ieqbTayrqHcy9TnGDjG9FIaN3DKid-vT60oj1_klOk"
}

@app.route('/get-user/<key>')
def get_user(key):
   
    
    
    
    if key in api_key:
        return jsonify(api_key[key]),200
    else:
        return jsonify({"error":"Invalid API key"}),401
    
   

    
    
    







if __name__ == '__main__':
    app.run(debug=True)