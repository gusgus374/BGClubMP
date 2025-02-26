import streamlit as st

st.title("Dry pistachio piget")
if st.button("HEY GUYS!"):
    st.balloons()
    st.write("henry")
    st.write(":smile:")
    st.toast("HEY COLIN!!! :angry:")

with st.expander("See Jaiden's Code!"):
    st.code(
        body='''
import streamlit as st

st.title("Dry pistachio piget")
if st.button("HEY GUYS!"):
    st.balloons()
    st.write("henry")
    st.write(":smile:")
    st.toast("HEY COLIN!!! :angry:")
        ''',
        language="python",
        line_numbers=True,
        #wrap_lines=True
    )