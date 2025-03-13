# This is a comment! Comments help explain what the code does.
# The computer doesn't run comments - they're just for humans to read.

# First, we need to import some tools (called libraries)
import streamlit as st
import pandas as pd
# Import our custom utility function
from utils import load_catapult_data

# This makes a title at the top of our app
st.title("My First Soccer Data App!")

# Create a chat message from Coach Gus
coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Welcome to your first coding project! Today we'll look at your soccer data from those GPS trackers you wore.")
    st.write("Don't worry if you've never coded before - I'll walk you through every step.")

# Let's explain what this app does
st.write("This app shows your soccer data from the GPS tracker you wore.")
st.write("Let's see what we can learn about your game!")

# Show the code for loading data
with st.expander("👀 Click here to see how we load your data", expanded=False):
    st.code("""
    # This code loads data from a CSV file and processes it
    from utils import load_catapult_data
    data = load_catapult_data('./data/BGCMP_data.csv')
    """)

# Now we'll load your data from a file
data = load_catapult_data('./data/BGCMP_data.csv')

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Great! We've loaded all the soccer data. Now let's find just YOUR data!")

# Let's pick your data out of everyone's data
player_name = st.text_input("Type your name exactly as it appears in the data:")

if player_name:
    # Show the code for filtering data
    with st.expander("👀 Click here to see how we filter for just your data", expanded=False):
        st.code("""
        # This code filters the data to show only your information
        my_data = data[data["Player Name"] == player_name]
        """)
    
    # This shows only your data, not everyone's
    my_data = data[data["Player Name"] == player_name]
    
    # Check if we found your data
    if len(my_data) > 0:
        st.success(f"Found your data, {player_name}!")
        
        coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
        with coach_message:
            st.write("Success! Now we can look at just your data. Let's see some of your stats!")
        
        # Show the most basic information
        st.subheader("Here's a quick look at your soccer sessions:")
        
        # Show the code for displaying the data
        with st.expander("👀 Click here to see how we display your data in a table", expanded=False):
            st.code("""
            # This code shows selected columns in a table
            st.dataframe(my_data[["Session Title", "Date", "Distance (km)", "Top Speed (m/s)"]])
            """)
        
        st.dataframe(my_data[["Session Title", "Date", "Distance (km)", "Top Speed (m/s)"]])
        
        # Show one interesting fact
        top_speed = my_data["Top Speed (m/s)"].max()
        # Convert meters per second to miles per hour
        top_speed_mph = top_speed * 2.237
        
        st.subheader("Did you know?")
        
        # Show the code for calculating speed
        with st.expander("👀 Click here to see how we calculate your top speed", expanded=False):
            st.code("""
            # This code finds your maximum speed and converts it to mph
            top_speed = my_data["Top Speed (m/s)"].max()
            top_speed_mph = top_speed * 2.237
            """)
        
        st.write(f"Your fastest speed was {top_speed:.2f} meters per second!")
        st.write(f"That's about {top_speed_mph:.2f} miles per hour!")
        
        coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
        with coach_message:
            st.write(f"Wow! {top_speed_mph:.2f} mph is pretty fast! Professional soccer players reach about 22-23 mph at their maximum.")
        
        if st.button("Show me more!"):
            with st.expander("👀 Click here to see the code for the balloons", expanded=False):
                st.code("""
                # This code shows balloons when you click the button
                st.balloons()
                """)
            
            st.balloons()
            st.write("Great job! Try the next example to learn more about your data!")
    else:
        st.error("Hmm, I couldn't find that name. Make sure you type it exactly as it appears.")
        
        coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
        with coach_message:
            st.write("Don't worry! Try checking for any spaces or special characters in your name as it appears in the data.")
