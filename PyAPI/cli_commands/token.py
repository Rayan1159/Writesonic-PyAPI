import json

def set_token(token=None) -> None:
    """
    This function is executed from the command line.
    It sets the token in the PyAPI package.

    The token is used to authenticate requests to the API.
    """

    #open json file
    with open("PyAPI/environment/environment.json", "w") as f:
        data = json.load(f)

        #check if token is set in data
        if not "token" in data:
            data["token"] = token
        else:
            print("The token is already present in the environment file.")    
        pass
    pass
pass

def clear_token(token=None) -> None:
    """
    This function is executed from the command line.
    It clears the token in the PyAPI package.
    
    The request can no longer complete when this is executed since each request requires a token present.
    """

    with open("PyAPI/environment/environment.json", "w") as f:
        data = json.load(f)

        if "token" in data:
            del data["token"]
        else: 
            print("The token could not be found in the environment file.")
        pass
    pass
pass