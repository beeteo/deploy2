from flask import Flask, render_template, jsonify
from Core.randomize import randomize

app = Flask(__name__, template_folder='Template')

@app.route('/')
def main():
    return jsonify(
        {
            "categorys": [
                'kiss',
                'hug'
            ],
            "base_url": "https://beete.xyz/api/v1/{category}"
        }
    )

@app.route('/api/v1/kiss')
def kiss():
    return jsonify(
        {
            "url": randomize().get_kiss_gif()
        }
    )

if __name__ == '__main__':
    app.run(debug=True)