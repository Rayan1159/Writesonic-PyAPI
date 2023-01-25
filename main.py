from PyAPI.http import request
import requests

if __name__ == "__main__":
    req = request.Request()
    try:
        response = req.post("https://api.writesonic.com/v2/business/content/chatsonic?engine=premium", data={
            "enable_google_results": "true",
            "enable_memory": True,
            "input_text": "Is PHP good"
        }, headers={
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": "",
        })
        print(response)
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError) as e:
        print(e)
    pass

