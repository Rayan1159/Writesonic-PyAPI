from abc import ABC, abstractmethod


class AbstractRequest(ABC):

    @abstractmethod
    def post(self, url, data=None, headers=None):
        raise NotImplementedError
        pass
