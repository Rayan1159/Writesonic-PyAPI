import json

from ..http import request
import requests


class ChatSonic:
    token = ""
    enable_memory = False
    input_text = None
    enable_google_results = False

    def __init__(self, token, input_text, enable_memory, enable_google_results):
        """
        :param token:
        :param input_text:
        :param enable_memory:
        :param enable_google_results:
        """

        self.token = token
        self.input_text = input_text
        self.enable_memory = enable_memory
        self.enable_google_results = enable_google_results
        pass

    def get_response_as_string(self) -> str:
        """
        Gets the response from get_response and turns message into a string

        :return: str
        :exception requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError
        """

        response = self.get_response()
        string = json.dumps(response)

        return string

    def get_response_as_array(self) -> []:
        """
        Gets the response from get_response and turns message into an array

        :return: []
        :exception requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError
        """

        response = self.get_response()

        word_array = []

        message = response["message"]
        for word in message.split(" "):
            word_array.append(word)
        pass

        return word_array

    def get_response(self):
        """
        Get a response from the chatsonic endpoint

        :return:

        :exception requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError
        """
        is_token_string = type(self.token) is str
        is_enable_mem = type(self.enable_memory) is bool
        is_input_string = type(self.input_text) is str
        is_google_results = type(self.enable_google_results) is bool

        if is_token_string and is_enable_mem and is_input_string and is_google_results:
            req = request.Request()
            try:
                json_object = req.post("https://api.writesonic.com/v2/business/content/chatsonic?engine=premium", data={
                    "enable_google_results": self.enable_google_results,
                    "enable_memory": self.enable_memory,
                    "input_text": self.input_text
                }, headers={
                    "accept": "application/json",
                    "content-type": "application/json",
                    "X-API-KEY": self.token,
                })
                return json_object
            except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError) as e:
                print(e)
        else:
            raise TypeError("token, enable_memory, input_text, and enable_google_results must be a string or bool")
