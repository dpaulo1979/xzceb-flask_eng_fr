import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

def getInstance():
    '''
   Gets Watson translator service instance.

            Returns:
                    language_translator: The instance
    '''
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)    

    return language_translator

def english_to_french(english_text):
    '''
    Returns english to french translation.

            Parameters:
                    english_text (str): A text

            Returns:
                    french_text (str): The translated text
    '''    
    if english_text is None or english_text == '':
        return ''

    french_text = getInstance().translate(text=english_text, model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    '''
    Returns french to english translation.

            Parameters:
                    french_text (str): A text

            Returns:
                    english_text (str): The translated text
    '''
    if french_text is None or french_text == '':
        return ''

    english_text = getInstance().translate(text=french_text, model_id='fr-en').get_result()
    return english_text['translations'][0]['translation']

#print(english_to_french("")['translations'][0]['translation'])