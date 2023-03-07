from PyAPI.endpoints import app_sms as SMS
import requests

if __name__ == "__main__":
    """ 
    This code does not interfere with the PyAPI package. 
    And is only meant to be used for command line testing.  
    """

    try:
        sms = SMS.AppSms(
            token='4d5a8f4a-e51b-4c58-bb35-1ca7821bd582',
            engine="premium",
            language="en",
            description="Say something about dogs",
            num_copies=1
        )
        response = sms.get_response_as_dict()
        print(response)
    except(requests.exceptions.HTTPError, requests.exceptions.ConnectionError, TypeError) as e:
        print(e)
    pass    
pass
