import os
import sys
import tempfile
from llama_index.core import SimpleDirectoryReader
from exception.exception import customexception
from logger.logger import logging

def load_data(data):
    """
    Load a PDF or TXT document from a file object.
    Parameters:
    - file_object: A file-like object (e.g., from st.file_uploader)
    Returns:
    - A list containing the loaded document.
    """
    try:
        logging.info("data loading started...")

        print("Data-->", data)
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save the uploaded file to the temporary directory
            temp_file_path = os.path.join(temp_dir, data.name)
            with open(temp_file_path, "wb") as f:
                f.write(data.getvalue())
            
            # Use SimpleDirectoryReader to load the file from the temporary directory
            loader = SimpleDirectoryReader(temp_dir)
            documents = loader.load_data()
        logging.info("data loading completed...")
        return documents
    except Exception as e:
        logging.info("exception in loading data...")
        raise customexception(e,sys)



    