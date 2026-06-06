# import libraries
import json
from pathlib import Path
import streamlit as st
import crud
import pandas as pd


#JSON Sample Structure For Appending 
#{
#    "id": 1,
#    "name": "Percy Jackson",
#    "finished": True,
#    "notes": "Better than Harry Potter"
#}


db = {
    "books": []
}

#define the file path
file_path = Path("database.json")

#check if the file exists, if not, create a new one and assign the core JSON stucture
if not file_path.is_file():
    file_path.write_text(json.dumps(db, indent = 4))

#Set Page Info
st.set_page_config(
    page_title="PyBookLogger",
    page_icon="📚",
    layout="wide"
)

#Defining Title and subheader
st.title("📚 My Books Dashboard")
st.subheader("Reading List")


#Create a structure which displays each item in the JSON database
for item in db["books"]:
    with st.container(border=True):
        st.markdown(f"## {item['id']}) {item['name']}")
        
        c1, c2 = st.columns(2)
        c1.metric(label="Status", value=item["finished"])
        c2.metric(label="Notes", value=item["notes"])
