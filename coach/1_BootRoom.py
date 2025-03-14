# Copyright (c) [2024] DataRook, Inc. All rights reserved.
# This source code is licensed under the license found in the
# LICENSE.md file in the root directory of this source tree.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#from mplsoccer import Sbopen, Pitch
import statsmodels.api as sm
import statsmodels.formula.api as smf
from matplotlib import colors
#from itscalledsoccer.client import AmericanSoccerAnalysis
import os
import pathlib
from scipy import stats
#from mplsoccer import PyPizza, FontManager
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import altair as alt
# Import our custom utility function
from utils import load_catapult_data


#with st.container():
 #       col1, col2 = st.columns([1,2])
  #      with col1:
   #          st.image('./resources/DSC_0352.JPG')
    #    with col2:
     #        st.write("Wanna know the secret, Rookie?") 
      #       st.write("The secret is... there is no secret.") 
       #      st.write("No hacks.")
        #     st.write("No shortcuts.")
         #    st.write("So, we focus on _fundamentals not fads_. We strive _for progress not perfection_")
#st.divider()
with st.expander("Catapult Login Info",icon=":material/passkey:"):
    st.subheader(":orange[Email Address:] footylab.1@datarook.com")
    st.subheader(":orange[password:] Play2Learn!")
st.title("Let's Boot Up. Have a look at your last session's data:")
components.iframe('https://oneapp.catapultsports.com/?embed=true', height=800, scrolling=True)
with st.sidebar:
    st.header("What's happening! I'm Coach Gus")
    coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
    coach_message.write("Can't wait to see what you can do!")
    st.image('./media/profile_coachGus.JPG',caption='Coach Gus is passionate about using data to analyze & improve player performance!')
    coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
    coach_message.write("_Consistency_ means showing up, _even when you don't want to._")
    coach_message.write("It makes you better at not only your craft but also the skill of exerting effort itself.")
    coach_message.write("The best diet is the one you can stick to _consitently_. The best exercise program is the one you can stick to _consistently_. The best routine is the one you can stick to _consistently_.")
    coach_message.write("Sustainable excellence isn't about being consistently great. _It's about being great at being consistent._")
    
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
coach_message.write("Pick a session above and figure out how to export the data in CSV format. Then I want you to upload that data file using the button below.")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
coach_message.write('Alternatively, you can click the "Download Last 30 Days GPS Data" button at the bottom of the page and use that file instead!')
#use_cloud_file = st.checkbox('Use "last30days_GPS.csv" instead of your own file')
with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    #if use_cloud_file:
    #    uploaded_file = pd.read_csv("./data/last30days_GPS.csv")
     #   uploaded_file = pd.DataFrame(uploaded_file)
    #else:
        #uploaded_file = st.file_uploader("Choose a file")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        dataframe = load_catapult_data(uploaded_file)
    elif os.path.exists('./data/last30days_GPS.csv'):
        # Use default file if no upload and default file exists
        dataframe = load_catapult_data('./data/last30days_GPS.csv')

if uploaded_file is not None:    
    with st.echo():
        dataframe = dataframe.loc[dataframe['Split Name'] == 'game']
        dataframe = dataframe.set_index('Player Name', drop=False)
        #let's see where we are at now
        st.dataframe(dataframe,use_container_width=True)
        #coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
        #coach_message.write("We're getting there! But I think we can do better a little better:")
if uploaded_file is not None:
    #with st.echo():
     #   dataframe = dataframe.drop(['Date','Split Name','Tags','Hr Load','Time In Red Zone (min)','Hr Max (bpm)'],axis=1)
      #  st.dataframe(dataframe)
    coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
    coach_message.write("I'm interested in the relationship between distance covered and sprint distance. Here's the code to create the graph:")

if uploaded_file is not None:
    with st.echo():
        dataframe['pp/km'] = dataframe['Power Plays']/dataframe['Distance (km)']
        dataframe['sprint/total distance']=(dataframe['Sprint Distance (m)']/1000)/dataframe['Distance (km)']
        chart = alt.Chart(dataframe).mark_circle().encode(
            x='Distance (km)',
            y='Sprint Distance (m)',
            size=alt.Size('sprint/total distance',legend=None),
            color=alt.Color('Player Name',legend=None),
            tooltip=["Player Name","Session Title"]).properties(height=500).interactive()
        '''
        ## Sprint Distance vs Total Distance
        '''
        with st.expander(label="Sprint Distance vs Total Distance Graph", expanded=True):
            st.altair_chart(chart, theme="streamlit", use_container_width=True)
    coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
    coach_message.write("Lastly, let's look at max acceleration, max deceleration, and top speed for this game:")
if uploaded_file is not None:
    chart = alt.Chart(dataframe).mark_circle().encode(
        x='Max Deceleration (m/s/s)',
        y='Max Acceleration (m/s/s)',
        size=alt.Size('Top Speed (m/s)',legend=None),
        color=alt.Color('Player Name',legend=None),
        tooltip=["Player Name", "Session Title"]).properties(height=500).interactive()
    '''
    ## Max Acceleration vs Deceleration
    '''
    with st.expander(label="Max Acceleration vs Max Deceleartion Graph", expanded=True):
        st.altair_chart(chart, theme="streamlit", use_container_width=True)
st.divider()
#uploaded_file = st.file_uploader("Choose a file again")
if uploaded_file is not None:
    #dataframe = pd.read_csv(uploaded_file)
    with st.expander(label="Collapse/Expand",expanded=False):
        st.write(dataframe)
    #dataframe = dataframe.loc[dataframe['Split Name'] == 'game']
    #dataframe = dataframe.drop(['Date','Split Name','Tags','Hr Load','Time In Red Zone (min)','Hr Max (bpm)'],axis=1)
    with st.popover("Change the graph variables"):
        mycol = dataframe.columns.tolist()
        #        all_data = load_catapult_data(uploaded_file)
        xvar = st.selectbox("Pick Variable #1",mycol)
        yvar = st.selectbox("Pick Variable #2",mycol,5)
        dotsize = st.selectbox("Size of data point",mycol,6)
        dotcolor = st.selectbox("Color of data point",mycol,1)
    chart = alt.Chart(dataframe).mark_circle().encode(
            x=xvar,
            y=yvar,
            size=alt.Size(dotsize, legend=None),
            color=alt.Color(dotcolor,legend=None),
            tooltip=["Player Name","Session Title",xvar,yvar,dotsize,dotcolor]).properties(height=500).interactive()
    '''
    ## Your Graph
    '''
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
st.divider()
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
coach_message.write("Caring deeply makes you vulnerable because things don't always go your way.")
coach_message.write("And caring deeply is also key to a rich and meaningful life.")
coach_message.write("Don't be like the kids in gym class who were too cool to try. Don't be afraid to put yourslef out there. The best stuff comes on the other side of that.")
#uploaded_file = st.file_uploader("Choose a data file")
#if uploaded_file is not None:
        # use the Pandas read_csv method to read the gps_data and turn into a dataframe
#        all_data = pd.read_csv(uploaded_file)
        # keep only the rows were the column 'Split Name' has a value equal to 'all'
 #       game_data = all_data.loc[all_data['Split Name'] == "game"]
        #game_data = game_data.loc[game_data['Tags'] == 'game']
  #      game_data = game_data.set_index('Player Name', drop=False)
        #game_data["day"] = game_data["Date"] - 45150
        #game_data = game_data.loc[game_data["day"] > 0]
   #     with st.expander(label="View Your Data",expanded=False):
                #display the uploaded data
    #            st.write(game_data)
     #   variable_x = st.selectbox("Pick Your X Variable!",game_data.columns.to_list(),1)
      #  variable_y = st.selectbox("Pick Your Y Variable!",game_data.columns.to_list(),8)
       # variable_size = st.selectbox("Pick Your Size Variable!",game_data.columns.to_list(),9)
#if uploaded_file is not None:
 #   chart = alt.Chart(game_data).mark_circle().encode(
  #      x=variable_x,
   #     y=variable_y,
    #    size=alt.Size(variable_size,legend=None),
     #   color=alt.Color('Player Name',legend=None),
      #  tooltip=["Player Name","Session Title",]).properties(height=500).interactive()
    #st.altair_chart(chart, theme="streamlit", use_container_width=True)