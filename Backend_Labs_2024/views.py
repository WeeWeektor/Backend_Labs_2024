from flask import Flask, jsonify
import datetime

app = Flask(__name__)


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return jsonify({
        "Current date and time:": date,
        "Service status": 200
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
