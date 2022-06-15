""" Create an instance of the translator """

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey='v5K1dSfWaO7mMWRvSOtqZPi23HQAdBxJmxRp6hLy5Q7D'
url="https://api.us-south.language-translator.watson.cloud.ibm.com/instances/a63a3d55-22a2-4f58-a9c5-819d0ed14f3a"
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    translation = language_translator.translate(
    text = english_text,
    model_id='en-fr').get_result()
    return translation["translations"][0]["translation"]

def french_to_english(french_text):
    translation = language_translator.translate(
    text = french_text,
    model_id ='fr-en').get_result()
    return translation["translations"][0]["translation"]