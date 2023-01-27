import requests
from ..http import request
from ..exceptions import language_exception as LanguageException
from ..exceptions import engine_exception as EngineException
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

    def get_response(
        self,
        token,
        language,
        topic,
        input_text,
        enable_memory,
        enable_google_results,
        engine,
        input_file=None,
        num_copies=1
    ) -> {}:
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

    def read_file(self):
        # TODO Add support for JSON, XML and Excel files

        topic_content = ""
        input_text = ""

        if self.input_file is not None:
            if self.input_file.endswith(".txt"):
                with open(self.input_file, "r") as file:
                    input_text = file.read()
                    topic = input_text.split("\n")[0].split(":")
                pass
            pass
        pass
        return [topic_content, input_text]
    pass

    def get_response_as_dict(self):
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

            def get_file_topic():
                topic = ""
                is_set = self.input_file if self.input_file is not None else False
                if is_set:
                    topic = self.read_file()[0]
                pass
                return topic
            pass

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
