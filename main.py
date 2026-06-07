# import libraries
import json
from pathlib import Path
import streamlit as st
import crud
import pandas as pd



db = {
    "books": []
}

#define the file path
file_path = Path("database.json")

#check if the file exists, if not, create a new one and assign the core JSON stucture
if not file_path.is_file():
    file_path.write_text(json.dumps(db, indent = 4))
else:
    db = json.loads(file_path.read_text())

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
if not db["books"]:
    st.markdown("### Your reading list is empty. Go pick up some book! [Here](https://ryanholiday.net/the-reading-list/) are some recommendations.")
for item in db["books"]:
    with st.container(border=True):
        st.markdown(f"## {item['name']}")
        
        c1, c2, c3 = st.columns(3)
        c1.metric(label="Status", value=crud.read_status((item["finished"])))
        c2.metric(label="Notes", value=item["notes"])
        c3.metric(label="ID", value=item["id"])

with st.popover("Add Entry"):
    st.markdown("## Add New Book") 
    with st.form("book_form", clear_on_submit=True):
        title = st.text_input("Book Title")
        read_checkbox = st.checkbox("Have you finished this book?")
        comments = st.text_input("Notes")
        if st.form_submit_button("Add"):
            if not title:
                st.error("You cannot leave title empty.")
            else:
                st.success("Added!")
                db["books"].append(crud.new_book(title, read_checkbox, comments))
                file_path.write_text(json.dumps(db, indent = 4))
                st.rerun()

#Delete entire database
with st.popover("🚨 DELETE DATABASE", type="primary"):
    st.write("### Warning!")
    st.write("This will delete all logs!")
    confirm = st.text_input('Type "DELETE" to confirm.')
    if st.button("Confirm Delete", type="primary"):
        if confirm == "DELETE":
            file_path.unlink(missing_ok=True)
            st.rerun()
