import streamlit as st
import pandas as pd
# Import our custom utility function
from utils import load_catapult_data

st.title("⏱️ Speed and Distance Calculator ⏱️")

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Welcome to the Speed and Distance Calculator! Today we'll learn how speed, distance, and time are connected.")
    st.write("This is one of the most important relationships in physics and sports science!")

st.write("Let's learn how speed, distance, and time are related!")

# Load the data
with st.expander("👀 See the code that loads your data", expanded=False):
    st.code("""
    # This loads all player data from the file and processes it
    from utils import load_catapult_data
    data = load_catapult_data('./data/BGCMP_data.csv')
    """)

data = load_catapult_data('./data/BGCMP_data.csv')

# Create a dropdown to select a player
all_players = data["Player Name"].unique().tolist()

with st.expander("👀 See the code that creates the player selector", expanded=False):
    st.code("""
    # This creates a dropdown with all player names
    all_players = data["Player Name"].unique().tolist()
    player_name = st.selectbox("Select your name:", all_players)
    """)

player_name = st.selectbox("Select your name:", all_players)

# Get just your data
with st.expander("👀 See the code that filters for just your data", expanded=False):
    st.code("""
    # This filters the data to only show the selected player
    my_data = data[data["Player Name"] == player_name]
    """)

my_data = data[data["Player Name"] == player_name]

if len(my_data) > 0:
    # First, show some of your actual data
    st.subheader("Your Speed and Distance")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("Let's look at your actual data from one of your sessions. Then we'll learn how to calculate speed, distance, and time.")
    
    # Select a session
    sessions = my_data["Session Title"].tolist()
    
    with st.expander("👀 See the code that creates the session selector", expanded=False):
        st.code("""
        # This creates a dropdown to select which session to analyze
        sessions = my_data["Session Title"].tolist()
        selected_session = st.selectbox("Choose a session:", sessions)
        """)
    
    selected_session = st.selectbox("Choose a session:", sessions)
    
    # Get the data for that session
    with st.expander("👀 See the code that gets session data", expanded=False):
        st.code("""
        # This gets data for just the session you selected
        session_data = my_data[my_data["Session Title"] == selected_session].iloc[0]
        """)
    
    session_data = my_data[my_data["Session Title"] == selected_session].iloc[0]
    
    # Show the key metrics
    with st.expander("👀 See the code that displays your metrics", expanded=False):
        st.code("""
        # This creates three columns to display your metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            distance_km = session_data["Distance (km)"]
            st.metric("Distance", f"{distance_km:.2f} km")
        
        with col2:
            # Duration is in seconds, convert to minutes
            duration_sec = session_data["Duration"]
            duration_min = duration_sec / 60
            st.metric("Time", f"{duration_min:.1f} min")
        
        with col3:
            # Calculate average speed
            avg_speed = distance_km / (duration_sec / 3600)  # km/h
            st.metric("Average Speed", f"{avg_speed:.2f} km/h")
        """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        distance_km = session_data["Distance (km)"]
        st.metric("Distance", f"{distance_km:.2f} km")
    
    with col2:
        # Duration is in seconds, convert to minutes
        duration_sec = session_data["Duration"]
        duration_min = duration_sec / 60
        st.metric("Time", f"{duration_min:.1f} min")
    
    with col3:
        # Calculate average speed
        avg_speed = distance_km / (duration_sec / 3600)  # km/h
        st.metric("Average Speed", f"{avg_speed:.2f} km/h")
    
    # Explain the relationship
    st.subheader("Understanding Speed, Distance, and Time")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("These three measurements are connected by an important formula that scientists, engineers, and athletes use all the time:")
        st.write("**Speed = Distance ÷ Time**")
        st.write("If we know any two of these values, we can find the third using these formulas:")
        st.write("**Distance = Speed × Time**")
        st.write("**Time = Distance ÷ Speed**")
    
    # Show the calculation with their data
    st.write("### Let's see how it works with your data:")
    
    with st.expander("👀 See the code that calculates your speed", expanded=False):
        st.code("""
        # This calculates your average speed from distance and time
        st.write(f"Distance: {distance_km:.2f} km")
        st.write(f"Time: {duration_min:.1f} minutes = {duration_sec/3600:.2f} hours")
        st.write(f"Speed = {distance_km:.2f} km ÷ {duration_sec/3600:.2f} hours = {avg_speed:.2f} km/h")
        """)
    
    st.write(f"Distance: {distance_km:.2f} km")
    st.write(f"Time: {duration_min:.1f} minutes = {duration_sec/3600:.2f} hours")
    st.write(f"Speed = {distance_km:.2f} km ÷ {duration_sec/3600:.2f} hours = {avg_speed:.2f} km/h")
    
    # Now let's make an interactive calculator
    st.subheader("Speed Calculator")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("Now it's your turn! Try changing two values and we'll calculate the third.")
        st.write("This is a great way to practice the relationship between speed, distance, and time.")
    
    calc_type = st.radio("What do you want to calculate?", 
                        ["Speed", "Distance", "Time"])
    
    if calc_type == "Speed":
        # Calculate speed from distance and time
        with st.expander("👀 See the code for calculating speed", expanded=False):
            st.code("""
            # This creates input fields for distance and time
            calc_distance = st.number_input("Distance (km):", min_value=0.1, max_value=100.0, value=5.0, step=0.1)
            calc_time = st.number_input("Time (hours):", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            
            if st.button("Calculate Speed"):
                # Calculate speed using the formula: Speed = Distance ÷ Time
                calc_speed = calc_distance / calc_time
                st.success(f"Speed = {calc_speed:.2f} km/h")
            """)
        
        calc_distance = st.number_input("Distance (km):", min_value=0.1, max_value=100.0, value=5.0, step=0.1)
        calc_time = st.number_input("Time (hours):", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
        
        if st.button("Calculate Speed"):
            calc_speed = calc_distance / calc_time
            st.success(f"Speed = {calc_speed:.2f} km/h")
            st.write(f"The formula is: Speed = {calc_distance:.2f} km ÷ {calc_time:.2f} h = {calc_speed:.2f} km/h")
            
            # Compare to your actual speed
            if calc_speed > avg_speed:
                st.write(f"That's {calc_speed/avg_speed:.1f} times faster than your average in the selected session!")
            else:
                st.write(f"That's {avg_speed/calc_speed:.1f} times slower than your average in the selected session.")
    
    elif calc_type == "Distance":
        # Calculate distance from speed and time
        with st.expander("👀 See the code for calculating distance", expanded=False):
            st.code("""
            # This creates input fields for speed and time
            calc_speed = st.number_input("Speed (km/h):", min_value=0.1, max_value=50.0, value=10.0, step=0.1)
            calc_time = st.number_input("Time (hours):", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            
            if st.button("Calculate Distance"):
                # Calculate distance using the formula: Distance = Speed × Time
                calc_distance = calc_speed * calc_time
                st.success(f"Distance = {calc_distance:.2f} km")
            """)
        
        calc_speed = st.number_input("Speed (km/h):", min_value=0.1, max_value=50.0, value=10.0, step=0.1)
        calc_time = st.number_input("Time (hours):", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
        
        if st.button("Calculate Distance"):
            calc_distance = calc_speed * calc_time
            st.success(f"Distance = {calc_distance:.2f} km")
            st.write(f"The formula is: Distance = {calc_speed:.2f} km/h × {calc_time:.2f} h = {calc_distance:.2f} km")
            
            # Compare to your actual distance
            if calc_distance > distance_km:
                st.write(f"That's {calc_distance/distance_km:.1f} times farther than you ran in the selected session!")
            else:
                st.write(f"That's {distance_km/calc_distance:.1f} times less than you ran in the selected session.")
    
    else:  # Calculate Time
        # Calculate time from distance and speed
        with st.expander("👀 See the code for calculating time", expanded=False):
            st.code("""
            # This creates input fields for distance and speed
            calc_distance = st.number_input("Distance (km):", min_value=0.1, max_value=100.0, value=5.0, step=0.1)
            calc_speed = st.number_input("Speed (km/h):", min_value=0.1, max_value=50.0, value=10.0, step=0.1)
            
            if st.button("Calculate Time"):
                # Calculate time using the formula: Time = Distance ÷ Speed
                calc_time = calc_distance / calc_speed
                calc_time_min = calc_time * 60
                
                st.success(f"Time = {calc_time:.2f} hours ({calc_time_min:.1f} minutes)")
            """)
        
        calc_distance = st.number_input("Distance (km):", min_value=0.1, max_value=100.0, value=5.0, step=0.1)
        calc_speed = st.number_input("Speed (km/h):", min_value=0.1, max_value=50.0, value=10.0, step=0.1)
        
        if st.button("Calculate Time"):
            calc_time = calc_distance / calc_speed
            calc_time_min = calc_time * 60
            
            st.success(f"Time = {calc_time:.2f} hours ({calc_time_min:.1f} minutes)")
            st.write(f"The formula is: Time = {calc_distance:.2f} km ÷ {calc_speed:.2f} km/h = {calc_time:.2f} h")
            
            # Compare to your actual time
            actual_time_h = duration_sec / 3600
            if calc_time > actual_time_h:
                st.write(f"That's {calc_time/actual_time_h:.1f} times longer than your selected session!")
            else:
                st.write(f"That's {actual_time_h/calc_time:.1f} times shorter than your selected session.")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("Great job using the speed, distance, and time formulas!")
        st.write("These calculations are used by coaches, scientists, and even NASA engineers to plan everything from soccer training to rocket launches!")
