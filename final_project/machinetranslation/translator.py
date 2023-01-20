"""Translate functions En/Fr."""

import os
from dotenv import load_dotenv
from ibm_watson import ApiException
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """Translate `english_text` to french"""
    if english_text is None:
        return None
    if english_text == '':
        return ''
    try:
        result = language_translator.translate(
            text=english_text,
            model_id='en-fr'
        ).get_result()
        french_text = result['translations'][0]['translation']
    except ApiException as ex:
        print(f'Method failed with status code {ex.code}: {ex.message}')
        return None
    except (IndexError, KeyError, ValueError) as ex:
        print(f'Wrong answer: {ex}')
        return None


    return french_text


def french_to_english(french_text):
    """Translate `french_text` to english"""
    if french_text is None:
        return None
    if french_text == '':
        return ''
    try:
        result = language_translator.translate(
            text=french_text,
            model_id='fr-en'
        ).get_result()
        english_text = result['translations'][0]['translation']
    except ApiException as ex:
        print(f'Method failed with status code {ex.code}: {ex.message}')
        return None
    except (IndexError, KeyError, ValueError) as ex:
        print(f'Wrong answer: {ex}')
        return None


    return english_text
