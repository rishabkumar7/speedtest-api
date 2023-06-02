import ping3
from flask import Flask, jsonify, render_template, request
import speedtest
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/myip')
def get_my_ip():
    user_ip = request.remote_addr
    ping_result = measure_ping(user_ip)
    result = {"user_ip": user_ip, "ping_result": ping_result}
    return jsonify(result)
#f"Your public IP address is: {user_ip}\nPing Result: {ping_result}"

def measure_ping(ip_address):
    try:
        response_time = ping3.ping(ip_address, timeout=2, unit="ms")
        if response_time is not None:
            result = f"Response Time: {response_time} ms"
        else:
            result = "No response"
    except Exception as e:
        result = str(e)
    return result 

@app.route('/speedtest')
def measure_speed():
    speedtester = speedtest.Speedtest()
    message = "Please wait while the speed test is in progress..."
    print(message)
    time.sleep(5)  # Simulate calculation time
    download_speed = speedtester.download() / 10**6
    upload_speed = speedtester.upload() / 10**6
    result = {"download_speed": download_speed, "upload_speed": upload_speed}
    return jsonify(result)

if __name__ == '__main__':
    app.run()