import streamlit as st
from tkinter import filedialog, Tk
import asyncio
from llama_index.core import SimpleDirectoryReader




def main():
    st.set_page_config("QA with Documents")




    data = []
    doc=st.file_uploader("upload your document", accept_multiple_files=True)
    # st.write(doc.read())
    input_files = []
    for file in doc:
        data.append(file.read().decode('utf-8'))
        input_files.append(file)
    
    # st.write("\n\n".join(data))
          
    loader = SimpleDirectoryReader(input_dir="Data")
    documents=loader.load_data()
    st.write(documents)
                
                
if __name__=="__main__":
    main()          
                
    
    
    
    
    