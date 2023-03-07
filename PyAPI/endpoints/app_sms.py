import requests
from ..http import request
from ..globals import globals
from ..exceptions import language_exception as LanguageException;
from ..exceptions import engine_exception as EngineException;

class AppSms: 
    token = ""
    engine = ""
    language = ""
    num_copies = 1
    description = "";

    def __init__(self, token, engine, language, description, num_copies=1) -> None:
        self.token = token
        self.engine = engine
        self.language = language
        self.description = description
        self.num_copies = num_copies
        pass    

    def get_response_as_string(self, ) -> str:
        """
        This function parses the response from "get_response_as_dict" to a string,
        When it's done the function returns the parsed dict as a string.
        """

        response = self.get_response_as_dict()
        word_array = []
        message = response["text"]

        for word in message.split(" "):
            word_array.append(word)
        pass
        
        string = ""
        for word in word_array:
            string += word + " "
        pass

        return string

    def get_response_as_dict(self) -> dict:
        """ 
        This function makes a request to the v2/business/content/app-sms endpoint.
        And returns the response as a dictionary.
        """

        is_token_set = type(self.token) is str and not None
        is_engine_set = type(self.engine) is str and not None
        is_language_set = type(self.language) is str and not None
        is_description_set = type(self.description) is str and not None
        is_num_copies_set = type(self.num_copies) is int and not None

        if is_token_set and self.token and is_engine_set and is_language_set and is_description_set and is_num_copies_set:
            req = request.Request()
            is_language_supported = self.language in globals.supported_lang
            is_engine_supported = self.engine in globals.engines

            if is_language_supported:
                if is_engine_supported:
                    try:
                        json_object = req.post(
                            "https://api.writesonic.com/v2/business/content/app-notifications", query={
                                "engine": self.engine,
                                "language": self.language,
                                "num_copies": self.num_copies,
                            }, data={
                                "description": self.description,
                            }, headers={
                                "accept": "application/json",
                                "content-type": "application/json",
                                "X-API-KEY": self.token,
                            })
                        return json_object
                    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError) as e:
                        print(e)
                    pass   
                else:
                    raise EngineException.EngineException("Engine not supported")
                pass
            else:
                raise LanguageException.LanguageException("Language not supported")
            pass
        else:
            raise TypeError("One or more arguments are not set")
        pass
    pass