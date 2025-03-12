import streamlit as st
import pandas as pd

st.title("⚽ Soccer Distance Calculator ⚽")

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Hey there! Today we're going to learn about distances you ran in soccer and practice some math along the way.")
    st.write("Did you know that professional soccer players run about 7-10 kilometers in a single game?")

st.write("Let's learn how far you ran in your soccer games!")

# Show the code for loading data
with st.expander("👀 See the code that loads your data", expanded=False):
    st.code("""
    # This code loads all the player data from a file
    data = pd.read_csv('./data/BGCMP_data.csv')
    """)

# Load the data
data = pd.read_csv('./data/BGCMP_data.csv')

# Let's create a dropdown menu to select your name
all_players = data["Player Name"].unique().tolist()

with st.expander("👀 See the code that creates the dropdown menu", expanded=False):
    st.code("""
    # This code creates a dropdown with all player names
    all_players = data["Player Name"].unique().tolist()
    player_name = st.selectbox("Select your name:", all_players)
    """)

player_name = st.selectbox("Select your name:", all_players)

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write(f"Great! Now let's find just {player_name}'s data.")

# Get just your data
with st.expander("👀 See the code that filters for just your data", expanded=False):
    st.code("""
    # This code filters the data to show only your information
    my_data = data[data["Player Name"] == player_name]
    """)

my_data = data[data["Player Name"] == player_name]

# Show your total distance
total_km = my_data["Distance (km)"].sum()

st.subheader("Your Total Distance")

with st.expander("👀 See the code that calculates your total distance", expanded=False):
    st.code("""
    # This code adds up all the distances from your sessions
    total_km = my_data["Distance (km)"].sum()
    """)

st.write(f"You ran a total of {total_km:.2f} kilometers in all your sessions!")

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Now let's convert this distance to other units! This helps us practice math and understand different measurement systems.")

# Let's convert kilometers to other units
with st.expander("👀 See the code that converts between units", expanded=False):
    st.code("""
    # Converting kilometers to meters and miles
    total_meters = total_km * 1000         # 1 km = 1000 meters
    total_miles = total_km * 0.621371      # 1 km = 0.621371 miles
    """)

# 1 kilometer = 1000 meters
total_meters = total_km * 1000

# 1 kilometer = 0.621371 miles
total_miles = total_km * 0.621371

st.write(f"That's {total_meters:.0f} meters or {total_miles:.2f} miles!")

# Let's add a fun comparison
soccer_field_length = 100  # meters (average)
fields = total_meters / soccer_field_length

with st.expander("👀 See the code that calculates soccer field lengths", expanded=False):
    st.code("""
    # This code calculates how many soccer field lengths you ran
    soccer_field_length = 100  # meters (average)
    fields = total_meters / soccer_field_length
    """)

st.write(f"If you ran in a straight line, you would have run the length of a soccer field {fields:.1f} times!")

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Now let's use your data to practice working with fractions and percentages. These math skills are super important in data science!")

# Let's practice fractions and visual math
st.subheader("Understanding Fractions with Distance")

# Pick a specific session
if len(my_data) > 0:
    session = st.selectbox("Choose a session:", my_data["Session Title"].tolist())
    
    with st.expander("👀 See the code that gets data for your selected session", expanded=False):
        st.code("""
        # This code gets data for just the session you selected
        session_data = my_data[my_data["Session Title"] == session]
        """)
    
    session_data = my_data[my_data["Session Title"] == session]
    
    if len(session_data) > 0:
        # Get distances in different speed zones
        with st.expander("👀 See the code that gets your speed zone data", expanded=False):
            st.code("""
            # This code gets distances in each speed zone
            zone1 = session_data["Distance in Speed Zone 1  (km)"].iloc[0]  # Walking
            zone2 = session_data["Distance in Speed Zone 2  (km)"].iloc[0]  # Jogging
            zone3 = session_data["Distance in Speed Zone 3  (km)"].iloc[0]  # Running
            zone4 = session_data["Distance in Speed Zone 4  (km)"].iloc[0]  # Fast Running
            zone5 = session_data["Distance in Speed Zone 5  (km)"].iloc[0]  # Sprinting
            """)
        
        zone1 = session_data["Distance in Speed Zone 1  (km)"].iloc[0]
        zone2 = session_data["Distance in Speed Zone 2  (km)"].iloc[0]
        zone3 = session_data["Distance in Speed Zone 3  (km)"].iloc[0]
        zone4 = session_data["Distance in Speed Zone 4  (km)"].iloc[0]
        zone5 = session_data["Distance in Speed Zone 5  (km)"].iloc[0]
        
        session_total = session_data["Distance (km)"].iloc[0]
        
        coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
        with coach_message:
            st.write("The GPS tracker measures your movement in different speed zones:")
            st.write("- Zone 1: Walking")
            st.write("- Zone 2: Jogging")
            st.write("- Zone 3: Running")
            st.write("- Zone 4: Fast Running")
            st.write("- Zone 5: Sprinting")
        
        # Create a visual fraction representation
        st.write("Here's how your running distance was split into different speed zones:")
        
        # Calculate percentages (this practices division and percentages)
        with st.expander("👀 See the code that calculates percentages", expanded=False):
            st.code("""
            # This code calculates what percentage of your total distance was in each zone
            zone1_percent = (zone1 / session_total) * 100  # Convert to percentage
            zone2_percent = (zone2 / session_total) * 100
            zone3_percent = (zone3 / session_total) * 100
            zone4_percent = (zone4 / session_total) * 100
            zone5_percent = (zone5 / session_total) * 100
            """)
        
        zone1_percent = (zone1 / session_total) * 100
        zone2_percent = (zone2 / session_total) * 100
        zone3_percent = (zone3 / session_total) * 100
        zone4_percent = (zone4 / session_total) * 100
        zone5_percent = (zone5 / session_total) * 100
        
        # Show the fractions
        st.write(f"Walking (Zone 1): {zone1:.2f} km ({zone1_percent:.1f}% of total)")
        st.write(f"Jogging (Zone 2): {zone2:.2f} km ({zone2_percent:.1f}% of total)")
        st.write(f"Running (Zone 3): {zone3:.2f} km ({zone3_percent:.1f}% of total)")
        st.write(f"Fast Running (Zone 4): {zone4:.2f} km ({zone4_percent:.1f}% of total)")
        st.write(f"Sprinting (Zone 5): {zone5:.2f} km ({zone5_percent:.1f}% of total)")
        
        # Visual representation (like a bar)
        st.write("Visual representation:")
        
        with st.expander("👀 See the code that creates these progress bars", expanded=False):
            st.code("""
            # This code creates visual progress bars for each speed zone
            st.progress(zone1_percent/100)  # Divide by 100 because progress bars use 0-1 scale
            st.caption(f"Walking: {zone1_percent:.1f}%")
            """)
        
        st.progress(zone1_percent/100)
        st.caption(f"Walking: {zone1_percent:.1f}%")
        st.progress(zone2_percent/100)
        st.caption(f"Jogging: {zone2_percent:.1f}%")
        st.progress(zone3_percent/100)
        st.caption(f"Running: {zone3_percent:.1f}%")
        st.progress(zone4_percent/100)
        st.caption(f"Fast Running: {zone4_percent:.1f}%")
        st.progress(zone5_percent/100)
        st.caption(f"Sprinting: {zone5_percent:.1f}%")
        
        coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
        with coach_message:
            st.write("You've just used fractions and percentages to analyze your own soccer data! This is real data science in action.")
            st.write("Try changing to a different session and see how the numbers change!")
