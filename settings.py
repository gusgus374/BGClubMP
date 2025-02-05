import streamlit as st

st.title("Session Info")
st.write(f"You are logged in as {st.session_state.user}.")