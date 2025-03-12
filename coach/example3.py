import streamlit as st
import pandas as pd

st.title("🚀 Soccer Speed Converter 🚀")

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Today we're going to explore speed! We'll look at your top speeds and learn how to convert between different units.")
    st.write("When you see scientists talking about speed, they often use meters per second (m/s). But when you watch sports on TV, they usually show miles per hour (mph) or kilometers per hour (km/h).")

st.write("Let's learn about different ways to measure speed!")

# Load the data
with st.expander("👀 See the code that loads your data", expanded=False):
    st.code("""
    # This loads all the player data from the CSV file
    data = pd.read_csv('./data/BGCMP_data.csv')
    """)

data = pd.read_csv('./data/BGCMP_data.csv')

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

# First, let's find your top speed
with st.expander("👀 See the code that finds your top speed", expanded=False):
    st.code("""
    # This finds the maximum speed in all your sessions
    top_speed_mps = my_data["Top Speed (m/s)"].max()
    """)

top_speed_mps = my_data["Top Speed (m/s)"].max()

st.subheader("Your Top Speed")

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Let's show your top speed in different units! This is where math skills become really useful.")

# Create columns for different speed units
with st.expander("👀 See the code that creates these columns", expanded=False):
    st.code("""
    # This creates three columns to display different units side by side
    col1, col2, col3 = st.columns(3)
    """)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Meters per Second", f"{top_speed_mps:.2f} m/s")
    st.caption("This is how the GPS tracker measures speed")

with col2:
    with st.expander("👀 See the code that converts to mph", expanded=False):
        st.code("""
        # Convert to miles per hour: 1 m/s = 2.237 mph
        top_speed_mph = top_speed_mps * 2.237
        """)
    
    # Convert to miles per hour: 1 m/s = 2.237 mph
    top_speed_mph = top_speed_mps * 2.237
    st.metric("Miles per Hour", f"{top_speed_mph:.2f} mph")
    st.caption("This is how speed is shown in the United States")

with col3:
    with st.expander("👀 See the code that converts to km/h", expanded=False):
        st.code("""
        # Convert to kilometers per hour: 1 m/s = 3.6 km/h
        top_speed_kmh = top_speed_mps * 3.6
        """)
    
    # Convert to kilometers per hour: 1 m/s = 3.6 km/h
    top_speed_kmh = top_speed_mps * 3.6
    st.metric("Kilometers per Hour", f"{top_speed_kmh:.2f} km/h")
    st.caption("This is how speed is shown in most countries")

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write(f"Wow! Your top speed was {top_speed_mph:.2f} mph! For comparison, Usain Bolt reached about 27.8 mph during his world record 100m sprint.")
    st.write("Now let's create a calculator where you can practice converting between different speed units.")

# Let's make an interactive speed converter to practice math
st.subheader("Speed Converter Calculator")
st.write("Now you try converting speeds! Type a number in any box and see the other units.")

# Create three columns for input
with st.expander("👀 See the code that creates the calculator", expanded=False):
    st.code("""
    # This creates three columns for the speed inputs
    input_col1, input_col2, input_col3 = st.columns(3)
    
    with input_col1:
        user_mps = st.number_input("Meters per Second (m/s)", min_value=0.0, value=5.0, step=0.1)
    
    with input_col2:
        user_mph = st.number_input("Miles per Hour (mph)", min_value=0.0, value=11.2, step=0.1)
    
    with input_col3:
        user_kmh = st.number_input("Kilometers per Hour (km/h)", min_value=0.0, value=18.0, step=0.1)
    """)

input_col1, input_col2, input_col3 = st.columns(3)

with input_col1:
    user_mps = st.number_input("Meters per Second (m/s)", min_value=0.0, value=5.0, step=0.1)

with input_col2:
    user_mph = st.number_input("Miles per Hour (mph)", min_value=0.0, value=11.2, step=0.1)

with input_col3:
    user_kmh = st.number_input("Kilometers per Hour (km/h)", min_value=0.0, value=18.0, step=0.1)

# Add a button to do the conversion
with st.expander("👀 See the code that does the conversion", expanded=False):
    st.code("""
    # This does the actual conversion when you click the button
    if st.button("Convert!"):
        # Convert from m/s to the others
        calculated_mph = user_mps * 2.237
        calculated_kmh = user_mps * 3.6
        
        st.write("### Conversion Results")
        st.write(f"{user_mps} m/s = {calculated_mph:.2f} mph = {calculated_kmh:.2f} km/h")
        
        # Show the math
        st.write("### Here's the math:")
        st.write(f"To convert m/s to mph: {user_mps} × 2.237 = {calculated_mph:.2f}")
        st.write(f"To convert m/s to km/h: {user_mps} × 3.6 = {calculated_kmh:.2f}")
    """)

if st.button("Convert!"):
    # Depending on which one the user changed, convert to the others
    # This is a simplification - in a real app, you'd track which one changed
    
    # Convert from m/s to the others
    calculated_mph = user_mps * 2.237
    calculated_kmh = user_mps * 3.6
    
    st.write("### Conversion Results")
    st.write(f"{user_mps} m/s = {calculated_mph:.2f} mph = {calculated_kmh:.2f} km/h")
    
    # Show the math
    st.write("### Here's the math:")
    st.write(f"To convert m/s to mph: {user_mps} × 2.237 = {calculated_mph:.2f}")
    st.write(f"To convert m/s to km/h: {user_mps} × 3.6 = {calculated_kmh:.2f}")
    
    # See if you beat your record
    with st.expander("👀 See the code that compares to your record", expanded=False):
        st.code("""
        # This compares the speed to your personal record
        if user_mps > top_speed_mps:
            st.success(f"Wow! {user_mps} m/s would be a new personal record for you!")
        else:
            st.info(f"Your current record is {top_speed_mps:.2f} m/s. Keep working hard!")
        """)
    
    if user_mps > top_speed_mps:
        st.success(f"Wow! {user_mps} m/s would be a new personal record for you!")
    else:
        st.info(f"Your current record is {top_speed_mps:.2f} m/s. Keep working hard!")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("Great job with these conversions! These math skills will be useful in many areas of data science.")
        st.write("Try entering different speeds and see what happens!")
