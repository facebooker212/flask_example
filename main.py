from flask import Flask, request, jsonify, send_file, make_response
from flask_cors import CORS
import os
import sys

app = Flask(__name__) # Initialize flask App
CORS(app) # Enable CORS on server side

# Index route and most basic example
@app.route('/', methods=['GET'])
def index():
    return jsonify({"Status": "Online!"})

# Custom route with return values in JSON
@app.route('/ninjas', methods=['GET'])
def values():
    
    names = ["Naruto", "Sasuke", "Sakura", "Kakashi"]
    
    return jsonify({"Shinobis": names})

# Post request example
@app.route('/name', methods=['POST'])
def name():
    req = request.get_json()
    
    name = req['Name']
    
    return jsonify({"Hello": name})

# Upload files
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['no_watermark']
    
    file.save('files/watermark.pdf')
    
    return 'PDF saved'
# Download the files
@app.route('/download')
def download():
    path = 'files/watermark.pdf'
    
    response = make_response(send_file(path))
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=watermark.pdf'
    
    return response

if __name__ == '__main__':
    from waitress import serve
    # This line is to debug requests made to the server on development
    #app.run(use_reloader=True, port=3000, threaded=True)
    # This is to run the server on deployment and get full performance
    serve(app, host="0.0.0.0", port=3000, url_scheme='https')
