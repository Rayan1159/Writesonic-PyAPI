class InvalidEngineException(Exception):
    def __init__(self, message):
        self.message = message
    pass
