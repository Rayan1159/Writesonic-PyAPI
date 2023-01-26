from PyAPI.http import request
import requests


class ChatSonic:
    token = ""

    def  __init__(self, token):
        """
        :param token:
        :return: None
        """

        self.token = token
        pass

    def get_response_as_string(self, enable_memory=False, input_text=None, enable_google_results=None):
        """
        Gets the response from get_response and turns message into a string

        :param enable_memory:
        :param input_text:
        :param enable_google_results:
        :return: None

        :exception requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError
        """

    def get_response_as_array(self, enable_memory=False, input_text=None, enable_google_results=None):
        """
        Gets the response from get_response and turns message into an array

        :param enable_memory:
        :param input_text:
        :param enable_google_results:
        :return: []

        :exception requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError
        """

        response = self.get_response(enable_memory=enable_memory, input_text=input_text,
                                     enable_google_results=enable_google_results)

        word_array = []

        message = response["message"]
        for word in message.split():
            word_array.append(word)
        pass

        return word_array

    def get_response(self, enable_memory, input_text, enable_google_results):
        """
        Get a response from the chatsonic endpoint

        :param enable_memory:
        :param input_text:
        :param enable_google_results:
        :return:

        :exception requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError
        """
        is_token_string = type(self.token) is str
        is_enable_mem = type(enable_memory) is bool
        is_input_string = type(input_text) is str
        is_google_results = type(enable_google_results) is bool

        if is_token_string and is_enable_mem and is_input_string and is_google_results:
            req = request.Request()
            try:
                json_object = req.post("https://api.writesonic.com/v2/business/content/chatsonic?engine=premium", data={
                    "enable_google_results": enable_google_results,
                    "enable_memory": enable_memory,
                    "input_text": input_text
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
