from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/login', methods=["POST"])
def login():
    userName = (request.form['userName'])
    password = (request.form['password'])

    if userName == 'Jayraj' and password == 'Jerry@123':
        return "Login Sucessful"
    else:
        return "Incorrect User ID or Password"  

if __name__ == '__main__':
    app.run(debug=True)