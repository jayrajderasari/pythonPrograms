from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'About':'Hello, World!'})

def sum(a,b):
    return a*b

if __name__ == '__main__':
    app.run(debug=True)