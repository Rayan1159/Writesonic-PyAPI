from PyAPI.endpoints import chat_sonic as ChatSonic
import requests

if __name__ == "__main__":
    """ 
    
    This code does not interfere with the PyAPI package. 
    And is only meant to be used for command line testing.  
    
    """
    chat_sonic = ChatSonic.ChatSonic(token="1a39b2fb-bd07-4508-b0b1-142c32e5daec", enable_memory=True, input_text="Hello", enable_google_results=True)

    try:
        print(chat_sonic.get_response_as_array())
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError) as e:
        print(e)
pass
