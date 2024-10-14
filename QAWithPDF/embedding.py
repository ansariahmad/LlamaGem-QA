import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.gemini import GeminiEmbedding

from logger.logger import logging
from exception.exception import customexception


load_dotenv()
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

# GOOGLE_API_KEY = "AIzaSyBGcAjkkrrvgW2wl7t3h000nPvbtxfgs58"
genai.configure(api_key=GOOGLE_API_KEY)

def download_gemini_embedding(model,document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """

    try:
        logging.info("")
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001", api_key=GOOGLE_API_KEY)
            
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20
        
        logging.info("")
        index = VectorStoreIndex.from_documents(document)
        index.storage_context.persist()
        
        logging.info("")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise customexception(e,sys)
    
if __name__ == "__main__":
    pass