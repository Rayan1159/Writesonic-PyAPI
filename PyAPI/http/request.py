import requests
import json
from ..abstract_classes import abstract_request as AbstractRequest


class Request(AbstractRequest.AbstractRequest):

    def post(self, url, data=None, query=None, headers=None) -> dict | None:
        """
        Makes a POST Request to one of writesonic's API endpoints

        :param url:
        :param data:
        :param query:
        :param headers:
        :return: dict | None

        :exception requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError
        """

        is_data_dict = type(data) is dict
        is_headers_dict = type(headers) is dict
        is_query_dict = type(query) is dict

        if is_data_dict and is_headers_dict and is_query_dict:
            response = requests.post(url, params=query, data=json.dumps(data), headers=headers)

            if response is not None:
                if response.status_code == 200:
                    return response.json()
                else:
                    raise requests.exceptions.HTTPError("HTTP Error: " + str(response.status_code))
                pass
            else:
                raise requests.exceptions.ConnectionError("No response from server")
        else:
            raise TypeError("query, data and headers must be a dict")
        pass
