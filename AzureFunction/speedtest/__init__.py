import json
import speedtest
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    speedtester = speedtest.Speedtest()
    download_speed = speedtester.download() / 10**6
    upload_speed = speedtester.upload() / 10**6

    result = {"download_speed": download_speed, "upload_speed": upload_speed}
    return func.HttpResponse(json.dumps(result))
