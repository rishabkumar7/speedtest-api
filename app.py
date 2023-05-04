from flask import Flask, jsonify, render_template
import speedtest
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

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