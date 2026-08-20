from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Flask API running in Docker!"
    })

@app.route('/api')
def api():
    return jsonify({
        "status": "success",
        "message": "Flask API is working"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)