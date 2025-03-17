from flask import Flask, jsonify, request
from src.systems.monitoring import get_cpu_usage, get_memory_usage
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>ESNSeY Live Metrics</h1>
    <div id="metrics">Loading...</div>
    <script>
    setInterval(() => fetch('/data')
      .then(r => r.json())
      .then(data => document.getElementById('metrics').innerHTML = 
        `CPU: ${data.cpu.toFixed(1)}% | MEM: ${data.mem.toFixed(2)}GB`), 1000)
    </script>
    '''

@app.route('/data')
def data():
    app.logger.info(f"Request from IP: {request.remote_addr}")
    return jsonify({
        "cpu": get_cpu_usage(),
        "mem": get_memory_usage()
    })

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
