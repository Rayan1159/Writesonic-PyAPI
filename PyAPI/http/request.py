import requests
import json


class Request(AbstractRequest.AbstractRequest):
    token = ""
    enable_memory = False

    def __init__(self, token=None, enable_memory=False):
        self.token = token
        self.enable_memory = enable_memory

    pass

    def post(self, url, data=None, headers=None) -> dict | None:
        """
        Makes a POST Request to one of writesonic's API endpoints

        :param url:
        :param data:
        :param headers:
        :return: dict | None
        """

        is_data_dict = type(data) is dict
        is_headers_dict = type(headers) is dict

        if is_data_dict and is_headers_dict:
            response = requests.post(url, data=json.dumps(data), headers=headers)

            if response is not None:
                if response.status_code == 200:
                    return response.json()
                else:
                    raise requests.exceptions.HTTPError("HTTP Error: " + str(response.status_code))
                pass
            else:
                raise requests.exceptions.ConnectionError("No response from server")
        else:
            raise TypeError("data and headers must be a dict")
        pass
