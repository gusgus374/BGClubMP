# Copyright (c) [2024] DataRook, Inc. All rights reserved.
# This source code is licensed under the license found in the
# LICENSE.md file in the root directory of this source tree.
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import altair as alt
import time 
import os
import pathlib
import streamlit.components.v1 as components


st.title("CLASS PAGE - example")
st.code('''
st.title("CLASS PAGE - example")
        ''')
st.write("Using our magic analogy, we borrow some *spells* from our *spellbooks*:")
st.code(""" 
        import streamlit as st
        import pandas as pd
        """)
st.write('streamlit and pandas are just some of the spellbooks we will use. This is just python code other people have written and kindly made available for others to use. No need to reinvent the wheel right?')
st.caption('(instead of "spellbook" the technical term for the word after "import" is a **python library**)')
st.header("Python Libraries Used In This Page (the one you are literally reading right now):")
st.code('''
import streamlit as st
import pandas as pd
import os
import pathlib
import altair as alt
import streamlit.components.v1 as components
        ''')

st.divider()
st.header("Okay so, Soccer... and Data... *and* Science?")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Hi I'm Coach Gus and I love soccer and physics. I enjoy teaching others about my passions and believe learning math and science does not have to be boring!")
        st.write("My favorite club team in England is :red[Liverpool FC] and I admire how their data science team combined physics knowledge with soccer knowledge to help the coaching staff better analyze the game.")
st.subheader("One of the biggest soccer clubs in the world, Liverpool FC, hired particle physicists to help improve their soccer team")

col1, col2 = st.columns(2)
col1.write("They used their knowledge of charged particles and electric fields:")
col2.write("And combined it with soccer data to create this (known as the Pitch Control model):")
with col2:
        iframe_src2 = "https://www.youtube.com/embed/Nc3uFWnPlsQ?si=pUx4ouf0EhWYMrVE"
        components.iframe(iframe_src2,600,500)

with col1:
        iframe_src = "https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html"
        components.iframe(iframe_src,height=500)
        st.caption("Hint: make sure to click the 'Voltage' checkbox then drag and drop the red and blue particels around")
st.subheader("The invention of the Pitch Control model helps coaches answer questions like:")
st.write(':orange["when is the right moment in the game to press and try to win the ball back?"]')
st.subheader("or")
st.write(':orange["in what areas of the field do our oppenents have a weakness we should attack?"]')

with st.expander("_The code for what you see above_", icon=":material/code:"):
    st.code(
          '''
st.header("Okay so, Soccer... and Data... *and* Science?")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Hi I'm Coach Gus and I love soccer and physics. I enjoy teaching others about my passions and believe learning math and science does not have to be boring!")
        st.write("My favorite club team in England is :red[Liverpool FC] and I admire how their data science team combined physics knowledge with soccer knowledge to help the coaching staff better analyze the game.")
st.subheader("One of the biggest soccer clubs in the world, Liverpool FC, hired particle physicists to help improve their soccer team")

col1, col2 = st.columns(2)
col1.write("They used their knowledge of charged particles and electric fields:")
col2.write("And combined it with soccer data to create this (known as the Pitch Control model):")
with col2:
        iframe_src2 = "https://www.youtube.com/embed/Nc3uFWnPlsQ?si=pUx4ouf0EhWYMrVE"
        components.iframe(iframe_src2,600,500)

with col1:
        iframe_src = "https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html"
        components.iframe(iframe_src,height=500)
        st.caption("Hint: make sure to click the 'Voltage' checkbox then drag and drop the red and blue particels around")
st.subheader("The invention of the Pitch Control model helps coaches answer questions like:")
st.write(':orange["when is the right moment in the game to press and try to win the ball back?"]')
st.subheader("or")
st.write(':orange["in what areas of the field do our oppenents have a weakness we should attack?"]')
'''
    )
st.divider()
st.header("What about that data thing? What *is* data?")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Well first we collect information like: 'What are your hobbies? 'What is your favorite subject in school?' 'What is your favorite sport?' 'What kind of career(s) are intersting to you?'")
        st.write("and then we organize it!")
info = {
      'Name': ['Taylor','Kade','Gabe','Carolina','Kylie','Lucas','Teddy','Olivia','Alex','Dashley','Jameson','Evan','Kellan','Gregory'], 
      'Hobby':['soccer','soccer and basketball','soccer', 'swimming, playing basketball and reading.', 'soccer' ,'soccer, football, video games', 'soccer', 'soccer', 'soccer','soccer, cooking', 'soccer, musical theater','Art, Track, Soccer','Soccer and Legos', 'video game designer'], 
      'Favorite school subject': ['Math','Math','Math','Science','Science','Math','History','Math','Social Studies','Math','Social Studies','Math','History','History'], 
      'Favorite Sport': ['Soccer', 'Basketball', 'Soccer', 'Basketball/Tennis', 'Soccer', 'Football', 'Football', 'Soccer', 'Soccer', 'Soccer', 'Soccer','Soccer','Soccer','Soccer'], 
      'Year Born': ['2012','2012','2013','2014','2011','2012','2012','2012','2012','2013','2011','2013','2013','2013'], 
      'Career Interest':['Soccer','NBA player', 'Soccer', 'Veterinarian', 'Physical Therapy', 'Soccer', 'Soccer', 'Engineer, almost any type', 'Soccer', 'Soccer Player', 'Soccer, Architecture','Brain Surgery','History Teacher','Video Game Programmer']
      }

campers_db = pd.DataFrame(data=info)
st.dataframe(campers_db)
st.header("So, Data is a *Collection* of *Structured* *Information*")

with st.expander("_enter the matrix_", icon=":material/code:"):
      st.code('''
st.header("What about that data thing? What *is* data?")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Well first we collect information like: 'What are your hobbies? 'What is your favorite subject in school?' 'What is your favorite sport?' 'What kind of career(s) are intersting to you?'")
        st.write("and then we organize it!")
info = {
      'Name': ['Taylor','Kade','Gabe','Carolina','Kylie','Lucas','Teddy','Olivia','Alex','Dashley','Jameson'], 
      'Hobby':['soccer','soccer and basketball','soccer', 'swimming, playing basketball and reading.', 'soccer' ,'soccer, football, video games', 'soccer', 'soccer', 'soccer','soccer, cooking', 'soccer, musical theater'], 
      'Favorite school subject': ['Math','Math','Math','Science','Science','Math','History','Math','Social Studies','Math','Social Studies'], 
      'Favorite Sport': ['Soccer', 'Basketball', 'Soccer', 'Basketball/Tennis', 'Soccer', 'Football', 'Football', 'Soccer', 'Soccer', 'Soccer', 'Soccer'], 
      'Year Born': ['2012','2012','2013','2014','2011','2012','2012','2012','2012','2013','2011'], 
      'Career Interest':['Soccer','NBA player', 'Soccer', 'Veterinarian', 'Physical Therapy', 'Soccer', 'Soccer', 'Engineer, almost any type', 'Soccer', 'Soccer Player', 'Soccer, Architecture']
      }

campers_db = pd.DataFrame(data=info)
st.dataframe(campers_db)
st.header("So, Data is a *Collection* of *Structured* *Information*")
''')


st.divider()
with st.echo("below"):
        st.header("Okay, so I know what Soccer is but what do we mean by ''Data Science''?")
        st.image("./media/datascience.png")

st.header("Soccer Data Science")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Looking back at the Venn Diagram above, Data Science is Hacking Skills + Substantive Expertise + Math & Statistics Knowledge ")
        st.write("Let's define these terms in our own words:")
        st.write(":red[**Hacking Skills**] = making the computer do stuff with code")
        st.write(":blue[**Substantive Expertise**] = Deep knowledge about a specific topic, like the game of soccer")
        st.write(":green[**Math and Statistics Knowledge**] = The ability to analyze things using mathematical tools")

        st.subheader('So Soccer Data Scientists ask questions like')
        st.subheader('"In 2023 who was the best attacker in MLS?"')
        st.subheader("They follow the scientific method, do math, write code, and learn that it is...")
        st.page_link("./coach/2_US_Pro_Soccer.py", label="Can you find an answer for this question?", icon="🤔")
st.divider()
with st.echo("below"):
    st.header("Graph example")

    file_location = "./data/last30days_GPS.csv"
    
    data = pd.read_csv(file_location)

    group_data = pd.DataFrame(data)

    players_data = group_data.loc[(group_data["Player Name"] == "Lucas - SL") | (group_data["Player Name"] == "Gregory - SL") | (group_data["Player Name"] == "Teddy - SL") | (group_data["Player Name"] == "Bowman - SL")]
    with st.expander("See the dataframe as a table"):
        st.dataframe(players_data)

    lines = alt.Chart(players_data, title="My interactive chart").mark_line().encode(
            x="Session Title:T",#the little ":T" after "Session Title" tells altair that this data is a time or date value
            y="Top Speed (m/s)",
            color="Player Name"
    )

    circles = alt.Chart(players_data).mark_circle().encode(
            x="Session Title:T",
            y="Top Speed (m/s)",
            color="Player Name",
            size=alt.Size("Distance (km)",legend=None),
            tooltip=["Player Name","Session Title","Top Speed (m/s)", "Split Name", "Distance (km)"]
    )

    combined_chart = (lines + circles).interactive()
    st.altair_chart(combined_chart, use_container_width=True)

st.divider()

#st.header("BONUS - PLAYER DATA EXPLORER")
#coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
#with coach_message:
#    st.write("You can change the variables to see the relationship between different metrics!")

#use the Pandas read_csv method to read the gps_data and turn into a dataframe
# Read the CSV file
#file_path = './data/last30days_GPS.csv'
#all_data = pd.read_csv(file_path)
# Replace ":" with "_" in the column names
#all_data.columns = [col.replace(':', ' ') for col in all_data.columns]
#keep only the rows were the column 'Split Name' has a value equal to 'all'
#game_data = all_data.loc[all_data['Split Name'] == "game"]
#game_data = game_data.loc[game_data['Tags'] == 'game']
#game_data = game_data.set_index('Player Name', drop=False)
#game_data["day"] = game_data["Date"] - 45150
#game_data = game_data.loc[game_data["day"] > 0]
#with st.expander(label="View Your Data",expanded=False):
    #display the uploaded data
#    st.write(game_data)
#variable_x = st.selectbox("Pick Your X Variable!",game_data.columns.to_list(),1)
#variable_y = st.selectbox("Pick Your Y Variable!",game_data.columns.to_list(),8)
#variable_size = st.selectbox("Pick Your Size Variable!",game_data.columns.to_list(),9)
#if variable_x == 'Session Title':
#    chart = alt.Chart(game_data).mark_circle().encode(
#    x='Session Title:T',
#    y=variable_y,
#    size=alt.Size(variable_size,legend=None),
#    color=alt.Color('Player Name',legend=None),
#    tooltip=["Player Name",]).properties(height=500).interactive()
#else:
#    chart = alt.Chart(game_data).mark_circle().encode(
#    x=variable_x,
#    y=variable_y,
#    size=alt.Size(variable_size,legend=None),
#    color=alt.Color('Player Name',legend=None),
#    tooltip=["Player Name","Session Title"]).properties(height=500).interactive()
#st.altair_chart(chart, theme="streamlit", use_container_width=True)

#with st.expander("How did coach make this data explorer?"):
#      st.code(
#            '''
#st.header("BONUS - PLAYER DATA EXPLORER")
#coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
#with coach_message:
#    st.write("You can change the variables to see the relationship between different metrics!")

#use the Pandas read_csv method to read the gps_data and turn into a dataframe
# Read the CSV file
#file_path = './data/last30days_GPS.csv'
#all_data = pd.read_csv(file_path)
# Replace ":" with "_" in the column names
#all_data.columns = [col.replace(':', ' ') for col in all_data.columns]
#keep only the rows were the column 'Split Name' has a value equal to 'all'
#game_data = all_data.loc[all_data['Split Name'] == "game"]
#game_data = game_data.loc[game_data['Tags'] == 'game']
#game_data = game_data.set_index('Player Name', drop=False)
#game_data["day"] = game_data["Date"] - 45150
#game_data = game_data.loc[game_data["day"] > 0]
#with st.expander(label="View Your Data",expanded=False):
    #display the uploaded data
#    st.write(game_data)
#variable_x = st.selectbox("Pick Your X Variable!",game_data.columns.to_list(),1)
#variable_y = st.selectbox("Pick Your Y Variable!",game_data.columns.to_list(),8)
#variable_size = st.selectbox("Pick Your Size Variable!",game_data.columns.to_list(),9)
#if variable_x == 'Session Title':
#    chart = alt.Chart(game_data).mark_circle().encode(
#    x='Session Title:T',
#    y=variable_y,
#    size=alt.Size(variable_size,legend=None),
#    color=alt.Color('Player Name',legend=None),
#    tooltip=["Player Name",]).properties(height=500).interactive()
#else:
#    chart = alt.Chart(game_data).mark_circle().encode(
#    x=variable_x,
#    y=variable_y,
#    size=alt.Size(variable_size,legend=None),
#    color=alt.Color('Player Name',legend=None),
#    tooltip=["Player Name","Session Title"]).properties(height=500).interactive()
#st.altair_chart(chart, theme="streamlit", use_container_width=True)
#''')
#      )