from flask import Flask, jsonify
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


data = {
    'username':'Frank Oliver',
    'password':3235128,
    'email':'frankol12@gmail.com'
}

@app.route('/')
def hello():
    return jsonify({'data':data}),201


if __name__ == '__main__':
    app.run(debug=True)