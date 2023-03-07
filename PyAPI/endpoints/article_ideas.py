import requests
from ..http import request
from ..exceptions import language_exception as LanguageException
from ..exceptions import engine_exception as EngineException
from ..exceptions import no_file_exception as NoFileException
from ..globals import globals


class ArticleIdeas:
    token = ""
    language = ""
    topic = ""
    input_text = ""
    enable_memory = False
    enable_google_results = False
    engine = ""
    input_file = None
    num_copies = 1

    def __init__(self, token, language, topic, input_text, enable_memory, enable_google_results, engine, input_file, num_copies=1) -> None:
        self.token = token
        self.language = language
        self.topic = topic
        self.input_text = input_text
        self.enable_memory = enable_memory
        self.enable_google_results = enable_google_results
        self.engine = engine
        self.input_file = input_file
        self.num_copies = num_copies
        pass

    def get_response_as_string(self):
        """
        This function parses the response from "get_response_as_dict" to a string,
        When it's done the function returns the parsed dict as a string.

        :param self: The object itself
        :type self: object
        :return: The parsed dict as a string
        :rtype: str
        """

        file_topic = ""
        file_content = ""

        if self.input_file is not None and self.input_file.endswith(".txt"):
            file_topic = self.input_file.split(".")[0]
            file_content = open(self.input_file, "r").read()
            return [file_topic, file_content]
        elif not self.input_file.endwiths(".txt"):
            raise TypeError("File must be a .txt file") 
        elif self.input_file is None:
            raise NoFileException.NoFileException("No file was provided")    
        pass

    def get_response_as_dict(self):
        """
        This function makes a request to the v2/business/content/article-ideas endpoint.
        And returns the response as a dictionary.

        :param self: The object itself
        :type self: object
        :return: The response as a dictionary
        :rtype: dict
        """

        is_token_set = self.token is str and not None
        is_language_set = self.language is str and not None
        is_input_text_set = self.input_text is str and not None
        is_enable_memory_set = self.enable_memory is bool and not None
        is_enable_google_results_set = self.enable_google_results is bool and not None
        is_engine_set = self.engine is str and not None

        if is_token_set and is_language_set and is_input_text_set or self.input_file is not None and is_enable_memory_set and is_enable_google_results_set and is_engine_set:
            req = request.Request()
            is_language_supported = self.language in globals.supported_lang
            is_engine_supported = self.engine in globals.engines

            if is_language_supported:
                if is_engine_supported:
                    try:
                        json_object = req.post(
                            "https://api.writesonic.com/v2/business/content/blog-ideas", query={
                                "engine": self.engine,
                                "language": self.language,
                                "num_copies": self.num_copies,
                            }, data={
                                "enable_google_results": self.enable_google_results,
                                "enable_memory": self.enable_memory,
                                "topic": self.topic if self.input_file is not None else get_file_topic(),
                                "input_text": self.input_text if self.input_file is not None else self.read_file(),
                            }, headers={
                                "accept": "application/json",
                                "content-type": "application/json",
                                "X-API-KEY": self.token,
                            })
                        return json_object
                    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError) as e:
                        raise e
                else:
                    raise EngineException.InvalidEngineException("Engine not supported")
                    pass
            else:
                raise LanguageException.LanguageNotSupported("Language not supported")
                pass
