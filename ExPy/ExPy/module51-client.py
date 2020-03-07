"""Time client"""

import urllib.request
import json
from datetime import datetime

# make sure that module51-server.py service is running
TIME_URL = "http://localhost:5000/"

def ex51():
    with urllib.request.urlopen(TIME_URL) as response:
        body = response.read()
    parsed = json.loads(body)
    date = datetime.fromisoformat(parsed["currentTime"])
    stamp = date.strftime("%H:%M:%S %Z %B %m %d")
    print("The current time is %s" % stamp)

if __name__ == "__main__":
    ex51()