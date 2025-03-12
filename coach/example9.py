import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("🚀 Soccer Acceleration Explorer 🚀")

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Welcome to the Acceleration Explorer! Today we'll learn about acceleration in soccer and how it affects your game.")
    st.write("Acceleration is one of the most important skills for soccer players - it's how quickly you can change your speed.")

st.write("Let's learn about acceleration in soccer!")

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
    st.subheader("What is Acceleration?")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("""
        Acceleration is how quickly you change your speed. It's measured in meters per second squared (m/s²).
        
        - Positive acceleration means you're speeding up
        - Negative acceleration (deceleration) means you're slowing down
        
        In soccer, quick acceleration helps you:
        - Beat defenders to the ball
        - Create space for yourself
        - React quickly to game situations
        
        Let's look at your acceleration data!
        """)
    
    # Select a session
    sessions = my_data["Session Title"].tolist()
    
    with st.expander("👀 See the code that creates the session selector", expanded=False):
        st.code("""
        # This creates a dropdown to select which session to analyze
        sessions = my_data["Session Title"].tolist()
        selected_session = st.selectbox("Choose a session:", sessions)
        """)
    
    selected_session = st.selectbox("Choose a session:", sessions)
    
    # Get data for the selected session
    with st.expander("👀 See the code that gets session data", expanded=False):
        st.code("""
        # This gets data for just the session you selected
        session_data = my_data[my_data["Session Title"] == selected_session].iloc[0]
        """)
    
    session_data = my_data[my_data["Session Title"] == selected_session].iloc[0]
    
    # Show acceleration and deceleration
    with st.expander("👀 See the code that displays your metrics", expanded=False):
        st.code("""
        # This displays your acceleration and deceleration in two columns
        col1, col2 = st.columns(2)
        
        with col1:
            max_accel = session_data["Max Acceleration (m/s/s)"]
            st.metric("Maximum Acceleration", f"{max_accel:.2f} m/s²")
            st.caption("How quickly you sped up")
        
        with col2:
            max_decel = session_data["Max Deceleration (m/s/s)"]
            st.metric("Maximum Deceleration", f"{max_decel:.2f} m/s²")
            st.caption("How quickly you slowed down")
        """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        max_accel = session_data["Max Acceleration (m/s/s)"]
        st.metric("Maximum Acceleration", f"{max_accel:.2f} m/s²")
        st.caption("How quickly you sped up")
    
    with col2:
        max_decel = session_data["Max Deceleration (m/s/s)"]
        st.metric("Maximum Deceleration", f"{max_decel:.2f} m/s²")
        st.caption("How quickly you slowed down")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        if max_accel > 3:
            st.write(f"Wow! {max_accel:.2f} m/s² is excellent acceleration! Professional soccer players typically accelerate at 3-4 m/s².")
        else:
            st.write(f"Your acceleration of {max_accel:.2f} m/s² shows good effort. With practice, you can increase this toward the 3-4 m/s² that professional players achieve.")
    
    # Create a visual explanation of what these numbers mean
    st.subheader("What do these numbers mean?")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("Let's see what your acceleration numbers actually mean in a real soccer situation.")
        st.write("I'll show you how quickly you can reach different speeds based on your acceleration!")
    
    # Explain acceleration with a simple example
    st.write("### Example of Acceleration")
    
    with st.expander("👀 See the code that calculates speed examples", expanded=False):
        st.code("""
        # This calculates how long it takes to reach certain speeds
        st.write(f"Your max acceleration was {max_accel:.2f} m/s².")
        st.write("This means:")
        
        # Calculate how long it takes to reach certain speeds
        time_to_reach_10kph = (10/3.6) / max_accel  # 10 kph converted to m/s
        time_to_reach_20kph = (20/3.6) / max_accel  # 20 kph converted to m/s
        
        st.write(f"- Starting from 0, you could reach 10 km/h in {time_to_reach_10kph:.2f} seconds")
        st.write(f"- Starting from 0, you could reach 20 km/h in {time_to_reach_20kph:.2f} seconds")
        """)
    
    st.write(f"Your max acceleration was {max_accel:.2f} m/s².")
    st.write("This means:")
    
    # Calculate how long it takes to reach certain speeds
    time_to_reach_10kph = (10/3.6) / max_accel  # 10 kph converted to m/s
    time_to_reach_20kph = (20/3.6) / max_accel  # 20 kph converted to m/s
    
    st.write(f"- Starting from 0, you could reach 10 km/h in {time_to_reach_10kph:.2f} seconds")
    st.write(f"- Starting from 0, you could reach 20 km/h in {time_to_reach_20kph:.2f} seconds")
    
    # Create a visual showing speed over time
    with st.expander("👀 See the code that creates the acceleration graph", expanded=False):
        st.code("""
        # This creates a graph showing how your speed increases over time
        times = np.linspace(0, 4, 100)
        speeds_mps = max_accel * times  # Speed in m/s
        speeds_kph = speeds_mps * 3.6   # Convert to km/h
        
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(times, speeds_kph, 'b-')
        
        # Add points for 10 kph and 20 kph
        ax.plot(time_to_reach_10kph, 10, 'ro', markersize=8)
        ax.plot(time_to_reach_20kph, 20, 'ro', markersize=8)
        
        # Add annotations
        ax.annotate(f'10 km/h at {time_to_reach_10kph:.2f}s', 
                   (time_to_reach_10kph, 10), 
                   xytext=(time_to_reach_10kph+0.2, 10+2),
                   arrowprops=dict(facecolor='black', shrink=0.05))
        
        ax.annotate(f'20 km/h at {time_to_reach_20kph:.2f}s', 
                   (time_to_reach_20kph, 20), 
                   xytext=(time_to_reach_20kph+0.2, 20+2),
                   arrowprops=dict(facecolor='black', shrink=0.05))
        
        # Add labels
        ax.set_xlabel('Time (seconds)')
        ax.set_ylabel('Speed (km/h)')
        ax.set_title('How Your Acceleration Affects Your Speed')
        ax.grid(True)
        """)
    
    times = np.linspace(0, 4, 100)
    speeds_mps = max_accel * times  # Speed in m/s
    speeds_kph = speeds_mps * 3.6   # Convert to km/h
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(times, speeds_kph, 'b-')
    
    # Add points for 10 kph and 20 kph
    ax.plot(time_to_reach_10kph, 10, 'ro', markersize=8)
    ax.plot(time_to_reach_20kph, 20, 'ro', markersize=8)
    
    # Add annotations
    ax.annotate(f'10 km/h at {time_to_reach_10kph:.2f}s', 
               (time_to_reach_10kph, 10), 
               xytext=(time_to_reach_10kph+0.2, 10+2),
               arrowprops=dict(facecolor='black', shrink=0.05))
    
    ax.annotate(f'20 km/h at {time_to_reach_20kph:.2f}s', 
               (time_to_reach_20kph, 20), 
               xytext=(time_to_reach_20kph+0.2, 20+2),
               arrowprops=dict(facecolor='black', shrink=0.05))
    
    # Add labels
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Speed (km/h)')
    ax.set_title('How Your Acceleration Affects Your Speed')
    ax.grid(True)
    
    st.pyplot(fig)
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("This graph shows how your speed increases over time with your acceleration.")
        st.write("The blue line shows your speed, and the red dots show when you reach 10 km/h and 20 km/h.")
        st.write("Now let's look at how much distance you covered while accelerating at different rates!")
    
    # Explore acceleration zones
    st.subheader("Acceleration Zones")
    st.write("Let's look at how much distance you covered while accelerating at different rates.")
    
    # Get acceleration zone data
    with st.expander("👀 See the code that gets acceleration zone data", expanded=False):
        st.code("""
        # This gets data about how much distance you covered at different acceleration rates
        accel_zone1 = session_data["Distance in Acceleration Zones: 0 - 1 m/s/s  (km)"]
        accel_zone2 = session_data["Distance in Acceleration Zones: 1 - 2 m/s/s  (km)"]
        accel_zone3 = session_data["Distance in Acceleration Zones: 2 - 3 m/s/s  (km)"]
        accel_zone4 = session_data["Distance in Acceleration Zones: 3 - 4 m/s/s  (km)"]
        accel_zone5 = session_data["Distance in Acceleration Zones: > 4 m/s/s  (km)"]
        
        # Convert to meters for easier understanding
        accel_zones = ["0-1 m/s²", "1-2 m/s²", "2-3 m/s²", "3-4 m/s²", ">4 m/s²"]
        accel_distances = [
            accel_zone1 * 1000, 
            accel_zone2 * 1000, 
            accel_zone3 * 1000, 
            accel_zone4 * 1000, 
            accel_zone5 * 1000
        ]
        """)
    
    accel_zone1 = session_data["Distance in Acceleration Zones: 0 - 1 m/s/s  (km)"]
    accel_zone2 = session_data["Distance in Acceleration Zones: 1 - 2 m/s/s  (km)"]
    accel_zone3 = session_data["Distance in Acceleration Zones: 2 - 3 m/s/s  (km)"]
    accel_zone4 = session_data["Distance in Acceleration Zones: 3 - 4 m/s/s  (km)"]
    accel_zone5 = session_data["Distance in Acceleration Zones: > 4 m/s/s  (km)"]
    
    # Convert to meters for easier understanding
    accel_zones = ["0-1 m/s²", "1-2 m/s²", "2-3 m/s²", "3-4 m/s²", ">4 m/s²"]
    accel_distances = [
        accel_zone1 * 1000, 
        accel_zone2 * 1000, 
        accel_zone3 * 1000, 
        accel_zone4 * 1000, 
        accel_zone5 * 1000
    ]
    
    # Create a bar chart
    with st.expander("👀 See the code that creates the chart", expanded=False):
        st.code("""
        # This creates a bar chart showing distance at different acceleration rates
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(accel_zones, accel_distances, color=['lightblue', 'blue', 'green', 'orange', 'red'])
        
        # Add labels
        ax.set_xlabel('Acceleration Zone')
        ax.set_ylabel('Distance (meters)')
        ax.set_title('Distance Covered While Accelerating')
        """)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(accel_zones, accel_distances, color=['lightblue', 'blue', 'green', 'orange', 'red'])
    
    # Add labels
    ax.set_xlabel('Acceleration Zone')
    ax.set_ylabel('Distance (meters)')
    ax.set_title('Distance Covered While Accelerating')
    
    st.pyplot(fig)
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("This chart shows how much distance you covered while accelerating at different rates.")
        st.write("- Low acceleration (0-1 m/s²) is like jogging at a steady pace")
        st.write("- Medium acceleration (1-3 m/s²) is like speeding up to run")
        st.write("- High acceleration (>3 m/s²) is like explosive sprinting")
        st.write("Now let's test what you've learned with a math challenge!")
    
    # Math challenge related to acceleration
    st.subheader("Acceleration Math Challenge")
    
    # Create a simple problem about calculating final speed
    with st.expander("👀 See the code that creates the math challenge", expanded=False):
        st.code("""
        # This creates a problem about calculating final speed
        initial_speed = 5  # m/s
        accel = 3  # m/s²
        time = 2  # seconds
        
        st.write(f"If you're running at {initial_speed} m/s (about {initial_speed*3.6:.1f} km/h),")
        st.write(f"and you accelerate at {accel} m/s² for {time} seconds,")
        st.write("what will your final speed be?")
        
        # Formula: final_speed = initial_speed + acceleration * time
        correct_answer = initial_speed + accel * time
        """)
    
    initial_speed = 5  # m/s
    accel = 3  # m/s²
    time = 2  # seconds
    
    st.write(f"If you're running at {initial_speed} m/s (about {initial_speed*3.6:.1f} km/h),")
    st.write(f"and you accelerate at {accel} m/s² for {time} seconds,")
    st.write("what will your final speed be?")
    
    # Formula: final_speed = initial_speed + acceleration * time
    correct_answer = initial_speed + accel * time
    
    user_answer = st.number_input("Enter your answer in m/s:", 
                                min_value=0.0, max_value=50.0, value=0.0, step=0.1)
    
    if st.button("Check my answer"):
        with st.expander("👀 See the code that checks your answer", expanded=False):
            st.code("""
            # This checks if your answer is close to correct
            if abs(user_answer - correct_answer) < 0.2:
                st.success(f"Correct! The answer is {correct_answer} m/s (about {correct_answer*3.6:.1f} km/h)")
                st.balloons()
            else:
                st.error(f"Not quite. The answer is {correct_answer} m/s")
                st.write("To solve this problem, we use the formula:")
                st.write("Final Speed = Initial Speed + (Acceleration × Time)")
                st.write(f"Final Speed = {initial_speed} + ({accel} × {time})")
                st.write(f"Final Speed = {initial_speed} + {accel*time}")
                st.write(f"Final Speed = {correct_answer} m/s")
            """)
        
        if abs(user_answer - correct_answer) < 0.2:
            st.success(f"Correct! The answer is {correct_answer} m/s (about {correct_answer*3.6:.1f} km/h)")
            st.balloons()
        else:
            st.error(f"Not quite. The answer is {correct_answer} m/s")
            st.write("To solve this problem, we use the formula:")
            st.write("Final Speed = Initial Speed + (Acceleration × Time)")
            st.write(f"Final Speed = {initial_speed} + ({accel} × {time})")
            st.write(f"Final Speed = {initial_speed} + {accel*time}")
            st.write(f"Final Speed = {correct_answer} m/s")
            
            coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
            with coach_message:
                st.write("In soccer, understanding acceleration helps us figure out how quickly players can reach top speed.")
                st.write("This formula is actually something NASA uses when launching rockets too!")
                st.write("Keep practicing, and you'll master both soccer skills and the math that explains them.")