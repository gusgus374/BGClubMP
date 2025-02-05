# Copyright (c) [2024] DataRook, Inc. All rights reserved.
# This source code is licensed under the license found in the
# LICENSE.md file in the root directory of this source tree.
import streamlit as st

from streamlit_metrics import metric, metric_row
from streamlit_ace import st_ace

import pandas as pd
import numpy as np
import altair as alt
import os
import pathlib
from notion_client import Client
import datetime

# Initialize Notion client using secrets
notion = Client(auth=st.secrets["notion_api_token"])

# Function to find a page by student name
def find_page_by_name(student_name):
    query = notion.databases.query(
        **{
            "database_id": st.secrets["notion_database_id"],
            "filter": {
                "property": "Name",
                "title": {
                    "equals": student_name
                }
            }
        }
    )
    results = query.get("results")
    if results:
        return results[0]["id"]
    return None

# Function to update an existing page with a new code block
def update_page(page_id, code):
    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "object": "block",
                "type": "code",
                "code": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": code
                            }
                        }
                    ],
                    "language": "python"
                }
            }
        ]
    )

# Function to create a new page in the Notion database
def create_page(student_name, code):
    database_id = st.secrets["notion_database_id"]
    notion.pages.create(
        parent={"database_id": database_id},
        properties={
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": student_name
                        }
                    }
                ]
            },
            "Date": {
                "date": {
                    "start": datetime.datetime.now().isoformat()
                }
            }
        },
        children=[
            {
                "object": "block",
                "type": "code",
                "code": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": code
                            }
                        }
                    ],
                    "language": "python"
                }
            }
        ]
    )

# Function to save code to Notion
def save_code_to_notion(student_name, code):
    page_id = find_page_by_name(student_name)
    if page_id:
        update_page(page_id, code)
    else:
        create_page(student_name, code)


if 'code' not in st.session_state:
     st.session_state['code'] = None
if 'old_code' not in st.session_state:
     st.session_state['old_code'] = None

st.title("footyLab codeBox")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("**Stuck**? :green[Embrace it], :orange[cuz that's part of it!] You gotta just _**try stuff**_")
    st.write("If you're struggling, try finding examples in other pages. Try making a button like the one in the example below.")
    with st.echo():
        if st.button('Bray turns on the JETS'):
            st.video("./media/bray_jets.mp4")
st.subheader("_Don't forget to save your code!!_")
with st.sidebar:
    file = st.file_uploader("upload python script",type=[".py"])

if st.session_state.old_code is not None:
    if file is not None:
        old_code = file.read()
        decoded_string = old_code.decode("utf-8")
        if st.session_state.old_code != decoded_string:
            st.session_state.old_code = decoded_string
        st.session_state.code = st.session_state.old_code
    else:
        st.session_state.code = st.session_state.old_code

if st.session_state.old_code is None:
    if file is not None:
        old_code = file.read()
        decoded_string = old_code.decode("utf-8")
        st.session_state.old_code = decoded_string
        INITIAL_CODE = st.session_state.old_code
            
    else:
        INITIAL_CODE = """# write code below!
import streamlit as st

st.title("What do you want to build today?")

"""
     


editor = st.container(border=False)
if st.session_state.code is None:
    with editor:
        code = st_ace(
            value=INITIAL_CODE,
            language="python",
            placeholder="st.header('Hello world!')",
            theme="tomorrow_night_eighties",
            show_gutter=True,
            wrap=True,
            show_print_margin=True,
            auto_update=False,
            readonly=False,
            key="ace-editor",
        )
        #st.write("Hit `CTRL+ENTER` to refresh")
if st.session_state.code is not None:
    with editor:
        code = st_ace(
            value=st.session_state.code,
            language="python",
            placeholder="st.header('Hello world!')",
            theme="tomorrow_night_eighties",
            show_gutter=True,
            wrap=True,
            show_print_margin=True,
            auto_update=False,
            readonly=False,
            key="ace-editor",
        )

st.session_state.code = code
st.session_state.old_code = st.session_state.code



with st.expander("Expand me to preview your app!",icon=":material/preview:",expanded=True):
    app = st.container(border=False)
    with app:
        exec(st.session_state.code)

        # Save code to Notion when the save button is clicked
if st.button("SAVE YOUR CODE!"):
    student_name = st.session_state.user if st.session_state.user else "Unknown Student"
    save_code_to_notion(student_name, code)
    st.success("Code saved successfully!")

#with st.popover(f"{st.session_state.user}, SAVE YOUR WORK!"):
 #   file_name = st.text_input("Name your file",f"{st.session_state.user}")
  #  btn = st.download_button(
   #                 label="Download Python File",
    #                data = code,
     #               file_name=f"{file_name}.py"
    #)