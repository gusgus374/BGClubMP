import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("🏃 Sprint Counter 🏃")

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Today we're going to count your sprints and learn about speed thresholds!")
    st.write("Sprinting is one of the most important skills in soccer. Let's analyze your sprint data!")

st.write("Let's count your sprints and learn about thresholds!")

# Load the data
with st.expander("👀 See the code that loads your data", expanded=False):
    st.code("""
    # This loads all player data from the file
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

if len(my_data) > 0:
    # Select a session
    sessions = my_data["Session Title"].tolist()
    
    with st.expander("👀 See the code that creates the session selector", expanded=False):
        st.code("""
        # This creates a dropdown to select which session to analyze
        sessions = my_data["Session Title"].tolist()
        selected_session = st.selectbox("Choose a session:", sessions)
        """)
    
    selected_session = st.selectbox("Choose a session:", sessions)
    
    # Get data for just that session
    with st.expander("👀 See the code that gets data for the selected session", expanded=False):
        st.code("""
        # This gets data for just the session you selected
        session_data = my_data[my_data["Session Title"] == selected_session].iloc[0]
        """)
    
    session_data = my_data[my_data["Session Title"] == selected_session].iloc[0]
    
    st.subheader("Sprint Zones")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("In soccer tracking, we divide your running into different 'speed zones':")
        st.write("- Zone 1: Walking")
        st.write("- Zone 2: Jogging") 
        st.write("- Zone 3: Running")
        st.write("- Zone 4: Fast Running")
        st.write("- Zone 5: Sprinting")
        st.write("Let's see how much distance you covered in each zone!")
    
    # Get the different speed zone distances
    with st.expander("👀 See the code that gets your speed zone data", expanded=False):
        st.code("""
        # This gets the distance you covered in each speed zone
        zone1 = session_data["Distance in Speed Zone 1  (km)"]
        zone2 = session_data["Distance in Speed Zone 2  (km)"]
        zone3 = session_data["Distance in Speed Zone 3  (km)"]
        zone4 = session_data["Distance in Speed Zone 4  (km)"]
        zone5 = session_data["Distance in Speed Zone 5  (km)"]
        
        # Convert to meters to make it easier to understand
        zone1_m = zone1 * 1000
        zone2_m = zone2 * 1000
        zone3_m = zone3 * 1000
        zone4_m = zone4 * 1000
        zone5_m = zone5 * 1000
        """)
    
    zone1 = session_data["Distance in Speed Zone 1  (km)"]
    zone2 = session_data["Distance in Speed Zone 2  (km)"]
    zone3 = session_data["Distance in Speed Zone 3  (km)"]
    zone4 = session_data["Distance in Speed Zone 4  (km)"]
    zone5 = session_data["Distance in Speed Zone 5  (km)"]
    
    # Convert to meters to make it easier to understand
    zone1_m = zone1 * 1000
    zone2_m = zone2 * 1000
    zone3_m = zone3 * 1000
    zone4_m = zone4 * 1000
    zone5_m = zone5 * 1000
    
    # Create a simple bar chart of speed zones
    with st.expander("👀 See the code that creates the chart", expanded=False):
        st.code("""
        # This creates a bar chart showing distance in each speed zone
        fig, ax = plt.subplots(figsize=(10, 5))
        
        zones = ["Walking", "Jogging", "Running", "Fast Running", "Sprinting"]
        distances = [zone1_m, zone2_m, zone3_m, zone4_m, zone5_m]
        
        # Create the bars with different colors
        ax.bar(zones, distances, color=['green', 'blue', 'yellow', 'orange', 'red'])
        
        # Add labels
        ax.set_xlabel('Speed Zone')
        ax.set_ylabel('Distance (meters)')
        ax.set_title('Distance in Each Speed Zone')
        """)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    zones = ["Walking", "Jogging", "Running", "Fast Running", "Sprinting"]
    distances = [zone1_m, zone2_m, zone3_m, zone4_m, zone5_m]
    
    # Create the bars with different colors
    ax.bar(zones, distances, color=['green', 'blue', 'yellow', 'orange', 'red'])
    
    # Add labels
    ax.set_xlabel('Speed Zone')
    ax.set_ylabel('Distance (meters)')
    ax.set_title('Distance in Each Speed Zone')
    
    # Show the chart
    st.pyplot(fig)
    
    # Explain what sprints are
    st.subheader("What is a Sprint?")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("A sprint is when you run at top speed for a short time.")
        st.write("In soccer tracking, we count runs as sprints when they reach a certain speed (Speed Zone 5).")
        st.write("Let's look at what fraction of your total running was sprinting!")
    
    # Calculate what fraction of total distance was sprinting
    with st.expander("👀 See the code that calculates sprinting fraction", expanded=False):
        st.code("""
        # This calculates what fraction of your total distance was sprinting
        total_distance_m = sum(distances)
        sprint_fraction = zone5_m / total_distance_m
        sprint_percentage = sprint_fraction * 100
        """)
    
    total_distance_m = sum(distances)
    sprint_fraction = zone5_m / total_distance_m
    sprint_percentage = sprint_fraction * 100
    
    st.write(f"You sprinted for {zone5_m:.0f} meters out of a total {total_distance_m:.0f} meters.")
    
    # Practice fractions
    st.write(f"That's a fraction of: {zone5_m:.0f}/{total_distance_m:.0f}")
    
    # Simplify the fraction (approximate)
    with st.expander("👀 See the code that simplifies the fraction", expanded=False):
        st.code("""
        # This code simplifies the fraction
        # Find greatest common divisor (GCD)
        from math import gcd
        approx_gcd = gcd(int(zone5_m), int(total_distance_m))
        simplified_numerator = int(zone5_m) // approx_gcd
        simplified_denominator = int(total_distance_m) // approx_gcd
        """)
    
    # Find greatest common divisor (GCD)
    from math import gcd
    approx_gcd = gcd(int(zone5_m), int(total_distance_m))
    simplified_numerator = int(zone5_m) // approx_gcd
    simplified_denominator = int(total_distance_m) // approx_gcd
    
    if approx_gcd > 1:
        st.write(f"Simplified fraction: {simplified_numerator}/{simplified_denominator}")
    
    st.write(f"As a percentage: {sprint_percentage:.1f}%")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("Professional soccer players typically sprint for about 7-12% of their total distance.")
        st.write("Now let's try changing our definition of what counts as a 'sprint'!")
    
    # Let's make it interactive with a threshold slider
    st.subheader("Sprint Threshold Explorer")
    st.write("What if we changed our definition of a 'sprint'?")
    
    # Let the user change what counts as a sprint
    with st.expander("👀 See the code that creates the sprint definition selector", expanded=False):
        st.code("""
        # This creates options for different sprint definitions
        sprint_options = [
            "Just Speed Zone 5 (Fastest)",
            "Speed Zones 4 and 5",
            "Speed Zones 3, 4, and 5"
        ]
        
        sprint_choice = st.selectbox("What should count as a sprint?", sprint_options)
        """)
    
    sprint_options = [
        "Just Speed Zone 5 (Fastest)",
        "Speed Zones 4 and 5",
        "Speed Zones 3, 4, and 5"
    ]
    
    sprint_choice = st.selectbox("What should count as a sprint?", sprint_options)
    
    # Recalculate based on their choice
    with st.expander("👀 See the code that recalculates based on your choice", expanded=False):
        st.code("""
        # This recalculates sprint distance based on your definition
        if sprint_choice == "Just Speed Zone 5 (Fastest)":
            sprint_distance = zone5_m
        elif sprint_choice == "Speed Zones 4 and 5":
            sprint_distance = zone4_m + zone5_m
        else:  # Zones 3, 4, and 5
            sprint_distance = zone3_m + zone4_m + zone5_m
        
        # Calculate new percentage
        new_sprint_percentage = (sprint_distance / total_distance_m) * 100
        """)
    
    if sprint_choice == "Just Speed Zone 5 (Fastest)":
        sprint_distance = zone5_m
    elif sprint_choice == "Speed Zones 4 and 5":
        sprint_distance = zone4_m + zone5_m
    else:  # Zones 3, 4, and 5
        sprint_distance = zone3_m + zone4_m + zone5_m
    
    # Calculate new percentage
    new_sprint_percentage = (sprint_distance / total_distance_m) * 100
    
    st.write(f"With this definition, you sprinted for {sprint_distance:.0f} meters.")
    st.write(f"That's {new_sprint_percentage:.1f}% of your total distance.")
    
    # Add a visual representation of the percentage
    with st.expander("👀 See the code that creates the progress bar", expanded=False):
        st.code("""
        # This creates a visual representation of the percentage
        st.write("Visual representation of your sprinting:")
        st.progress(new_sprint_percentage / 100)
        """)
    
    st.write("Visual representation of your sprinting:")
    st.progress(new_sprint_percentage / 100)
    
    # Challenge: Ask them to convert the percentage to a decimal
    st.subheader("Quick Math Challenge")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write(f"Let's practice converting percentages to decimals. This is an important skill in data science!")
        st.write(f"Can you convert {new_sprint_percentage:.1f}% to a decimal?")
    
    st.write(f"Convert {new_sprint_percentage:.1f}% to a decimal.")
    
    user_decimal = st.number_input("Enter your answer:", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
    
    # Correct answer
    correct_decimal = new_sprint_percentage / 100
    
    if st.button("Check my answer"):
        with st.expander("👀 See the code that checks your answer", expanded=False):
            st.code("""
            # This checks if your answer is close enough to correct
            if abs(user_decimal - correct_decimal) < 0.01:
                st.success("Correct! To convert from percent to decimal, divide by 100.")
                st.balloons()
            else:
                st.error(f"Not quite. The answer is {correct_decimal:.2f}. To convert {new_sprint_percentage:.1f}% to a decimal, divide by 100.")
            """)
        
        # Allow for a small margin of error
        if abs(user_decimal - correct_decimal) < 0.01:
            st.success("Correct! To convert from percent to decimal, divide by 100.")
            st.balloons()
        else:
            st.error(f"Not quite. The answer is {correct_decimal:.2f}. To convert {new_sprint_percentage:.1f}% to a decimal, divide by 100.")
            
            coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
            with coach_message:
                st.write(f"To convert a percentage to a decimal, we divide by 100. So {new_sprint_percentage:.1f} ÷ 100 = {correct_decimal:.2f}")
