from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Flask App!"


@app.route('/json')
def json_route():
    return jsonify(message = "Hello, WebTest!")


@app.route('/echo', methods = ['POST'])
def echo():
    data = request.json
    return jsonify(data)
