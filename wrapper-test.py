from PyAPI.endpoints import chat_sonic as ChatSonic
import requests

if __name__ == "__main__":
    """ 
    
    This code does not interfere with the PyAPI package. 
    And is only meant to be used for command line testing.  
    
    """
    chat_sonic = ChatSonic.ChatSonic(
        token="",
        enable_memory=True,
        input_text="Hello",
        enable_google_results=True,
        language="ens",
        engine="premium"
    )

    try:
        print(chat_sonic.get_response_as_dict())
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError) as e:
        print(e)
pass
