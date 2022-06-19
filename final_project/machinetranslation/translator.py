# from ensurepip import version
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = '2018-05-01'

authenticators = IAMAuthenticator(apikey)
LanguageTranslator = LanguageTranslatorV3(version=version, authenticator=authenticators)

LanguageTranslator.set_service_url(url)

def english_to_french(english_text):
    """Translate English to French"""
    frenchtranslation = LanguageTranslator.translate(text=english_text, model_id='en-fr').get_result()
    return frenchtranslation['translations'][0]['translation']

def french_to_english(french_text):
  """Translate French to English"""
  englishtranslation = LanguageTranslator.translate(text=french_text, model_id='fr-en').get_result()
  return englishtranslation['translations'][0]['translation']