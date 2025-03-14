# Copyright (c) [2024] DataRook, Inc. All rights reserved.
# This source code is licensed under the license found in the
# LICENSE.md file in the root directory of this source tree.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import streamlit as st
import altair as alt
import streamlit.components.v1 as components
from streamlit_ace import st_ace
import time
from utils import load_catapult_data


st.title("Welcome to")
st.image(image="./media/footylab_v2_horizontal.png",width=600)
iframe_src3 = "https://www.youtube.com/embed/wBY0Qlk_djU?si=7yaVJXCdvYXkXxcq"
components.iframe(iframe_src3,600,400)
#if st.button("Best ever"):
#      st.image("https://www.si.com/.image/t_share/MTc5NTMwMzAxNjQ1NTMwMjQ5/gettyimages-891445.jpg")

st.header("Here, Coach Gus (yours truly), will provide information and examples to help you on your path to building your own app.")

#st.text("This is the home page of our currently-under-development app!")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.text("The goal is for us to explore the data we have been collecting on the soccer field right here in the footyLab.")
        st.subheader("BUT HOW ARE WE GONNA DO THIS?!")
        st.markdown("Magic. Well... actually by writing some *python code*... which feels like magic, I promise.")

        st.header("Hacking Skills = ~Computer Programming~ *Magic*")
        iframe_src2 = "https://www.youtube.com/embed/Qgr4dcsY-60?si=gsK8I_rpz0cpH5UO"
        components.iframe(iframe_src2,400,300)
        st.caption("This clip is a great example of what we mean by using proper _syntax_. Hermione used the correct syntax, :green[so the spell worked]! Seamus used incorrect syntax :red[so the spell didn't work] and now he needs a new feather. It is very normal to make mistakes when coding. :blue[If something isn't working, check to make sure you used the proper syntax.]")

coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Now I'm going to ``cast a spell`` (:wink:) to generate a button:")

        st.code("""
               #this spell is actually just python code
        st.button("I'm a Button")
                """)
        st.button("I'm a Button")

coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Okay cool! We can click on our newly casted button but... that's about it. Let's try a slightly more advanced spell:")

        st.code("""
        if st.button("Click me for a celebration"):
                st.balloons()
                """)

        if st.button("Click me for a celebration"):
                st.balloons()

st.subheader("See? Magic.")
st.page_link("https://docs.streamlit.io/develop/api-reference", label="Click me to read about more Streamlit ~~methods~~ spells", icon="🪄")
st.divider()

st.title("Your Brain, Electricity, Some Stuff Called 'Myelin', and Getting Better at Stuff.")
col1, col2 = st.columns(2)
with col2:
        st.image(image="./media/myelin_sheath.jpg",width=400)

with col1:
        iframe_src = "https://phet.colorado.edu/sims/html/resistance-in-a-wire/latest/resistance-in-a-wire_en.html"
        components.iframe(iframe_src,height=500)


st.divider()

#coach_message = st.chat_message(name="Coach Gus",avatar="./resources/profile_coachGus.JPG")
#coach_message.write("Below you'll find a *file uploader* and the *codeBox* where you can play around with data you upload!")

st.divider()
st.header("CODE EXAMPLES")
st.subheader("Learn to load a CSV file stored locally")
with st.expander("~~spellbooks~~ libraries used"):
       st.code(
              body= '''
              import streamlit as st
              import pandas as pd
              import os
              import pathlib
              ''',
              language="python"
       )
with st.echo():
        file_location = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')
        #using the os and path libraries (spellbooks), we save the location of our data file in the variable "file_location"
        #then we use our custom utility function to load and process the data file
        data = load_catapult_data(file_location)
        #then we make sure the data is in the right format (called a type) for us to work with, DataFrame, using the pandas method DataFrame(). We call our pandas DataFrame "ETFS_data"
        group_data = pd.DataFrame(data)
        #then we take a look at our data using st.dataframe()
        st.dataframe(group_data)
st.subheader("Isolate a single player's data - let's say Carolina")
with st.echo():
       player_data = group_data.loc[group_data["Player Name"] == "Carolina - SL"]      
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
       st.write('''the line of code above used the pandas "loc" method. It's asking the computer to keep only the rows of the dataframe where the values in the column "Player Name" match with the string "Ayden - ETFS".''')
       st.write("then we ask streamlit to show us our new dataframe using the st.dataframe spell (really called a _method_)")
with st.echo():
        st.dataframe(player_data)

coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Here we use the streamlit's line_chart method to plot Ayden's daily top speed")
        with st.echo():
                st.line_chart(player_data, x = "Session Title", y="Top Speed (m/s)")
st.subheader("Make your charts interactive!")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Now instead of using ``st.line_chart()``, we will us ``st.altair_chart()`` to make our plot interactive. As a bonus, I'll show you how to isolate multiple player's data at the same time.")
        st.write("first, let's get our player data")
        with st.echo():
                players_data = group_data.loc[(group_data["Player Name"] == "Olivia - SL") | (group_data["Player Name"] == "Kylie - SL") | (group_data["Player Name"] == "Dashley - SL")]
                st.dataframe(players_data)
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("We will use ``st.altair_chart()`` to vizualize their data. This is more complicated spell, but worth it! We will also need to borrow the altair library for this:")
        st.code("import altair as alt", language="python") 
        st.write("I want a line chart so:")
        with st.echo():
                lines = alt.Chart(players_data, title="My interactive chart").mark_line().encode(
                        x="Date:T",#the little ":T" after "Session Title" tells altair that this data is a time or date value
                        y="Top Speed (m/s)",
                        color="Player Name"
                )
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Then to actually see the lines we have to call upon ``st.altair_chart()``")
        with st.echo():
                st.altair_chart(lines, use_container_width=True)
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Not too different than before right? Well, let's add some circles so it's easier to read the data.")
        with st.echo():
                circles = alt.Chart(players_data).mark_circle().encode(
                        x="Date:T",
                        y="Top Speed (m/s)",
                        color="Player Name",
                        size=alt.Size("Distance (km)",legend=None),
                        tooltip=["Player Name","Session Title","Top Speed (m/s)", "Split Name", "Distance (km)"]
                )
        st.write("Now we put our lines and circles together!")
        with st.echo():
                st.altair_chart(lines + circles, use_container_width=True)
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("And now we make it interactive! Check out the final product:")
        with st.echo():
                combined_chart = (lines + circles).interactive()
                st.altair_chart(combined_chart, use_container_width=True)