# import libraries
import json
from pathlib import Path
import streamlit as st

db = {
    "books": []
}

#define the file path
file_path = Path("database.json")

#check if the file exists, if not, create a new one and assign the core JSON stucture
if not file_path.is_file():
    file_path.write_text(json.dumps(db, indent = 4))

