"""Time service"""

from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    response = {
        "currentTime": datetime.now(timezone.utc).isoformat()
    }
    return jsonify(response)

app.run()
