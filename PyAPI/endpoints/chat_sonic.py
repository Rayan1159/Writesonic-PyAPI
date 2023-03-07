import json

from ..http import request
from ..globals import globals
from ..exceptions import language_exception as LanguageException
from ..exceptions import engine_exception as EngineException
import requests

class ChatSonic:
    token = ""
    language = ""
    enable_memory = False
    input_text = None
    enable_google_results = False
    engine = ""

    def __init__(self,
                 token, 
                 language, 
                 input_text,
                 enable_memory, 
                 enable_google_results,
                 engine):
        """
        :param token:
        :param input_text:
        :param enable_memory:
        :param enable_google_results:
        """

        self.token = token
        self.language = language
        self.input_text = input_text
        self.enable_memory = enable_memory
        self.enable_google_results = enable_google_results
        self.engine = engine
        pass

    def get_response_as_string(self) -> str:
        """
        Gets the response from get_response and turns message into a string

        :return: str
        :exception requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError
        """

        response = self.get_response()

        word_array = []
        message = response["message"]

        for word in message.split(" "):
            word_array.append(word)
        pass

        string = ""
        for word in word_array:
            string += word + " "
        pass

        return string

    def get_response_as_array(self) -> []:
        """
        Gets the response from get_response and turns message into an array

        :return: []
        :exception requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError
        """

        response = self.get_response_as_dict()

        word_array = []

        message = response["message"]
        for word in message.split(" "):
            word_array.append(word)
        pass

        return word_array

    def get_response_as_dict(self) -> dict:
        """
        Get a response from the chatsonic endpoint

        :return:

        :exception requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError, ValueError
        """
        is_token_string = type(self.token) is str and not None
        is_enable_mem = type(self.enable_memory) is bool and not None
        is_input_string = type(self.input_text) is str and not None
        is_google_results = type(self.enable_google_results) is bool and not None
        language_supported = self.language in globals.supported_lang
        engine_supported = self.engine in globals.engines

        if is_token_string and is_enable_mem and is_input_string and is_google_results:
            req = request.Request()
            if language_supported:
                if engine_supported:
                    try:
                        json_object = req.post(
                            "https://api.writesonic.com/v2/business/content/chatsonic", query={
                            "engine": self.engine,
                            "language": self.language
                        }, data={
                            "enable_google_results": self.enable_google_results,
                            "enable_memory": self.enable_memory,
                            "input_text": self.input_text,
                        }, headers={
                            "accept": "application/json",
                            "content-type": "application/json",
                            "X-API-KEY": self.token,
                        })
                        return json_object
                    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError) as e:
                        print(e)
                else:
                    raise EngineException.InvalidEngineException
            else:
                raise LanguageException.LanguageNotSupported("Language not supported")
        else:
            raise TypeError("token, enable_memory, input_text, and enable_google_results must be a string or bool")
