import socket
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    subprocess.Popen(["python3", "stress_cpu.py"])
    return '', 200

@app.route('/', methods=['GET'])
def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return {'IP': ip_address}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
