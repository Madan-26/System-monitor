import psutil
from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    while True:
        cpu_percent = psutil.cpu_percent()
        mem_percent = psutil.virtual_memory().percent
        message = None
        if cpu_percent > 80 or mem_percent > 87:
            message = "WARNING: HIGH CPU/MEMORY utilization"
        return {
            'cpu_percent': cpu_percent,
            'mem_percent': mem_percent,
            'message': message
        }
        time.sleep(1)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
