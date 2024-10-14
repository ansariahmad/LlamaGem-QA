import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai
from llama_index.llms.gemini import Gemini
from exception.exception import customexception
from logger.logger import logging

load_dotenv()
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
    """
    try:
        model=Gemini(models='models/gemini-pro',api_key=GOOGLE_API_KEY)
        return model
    except Exception as e:
        raise customexception(e,sys)
        