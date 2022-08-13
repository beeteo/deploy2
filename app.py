from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return jsonify({'hola': "omg"})

if __name__ == '__main__':
    app.run()