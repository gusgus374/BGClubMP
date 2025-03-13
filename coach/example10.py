import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Import our custom utility function
from utils import load_catapult_data

st.title("🎮 My Soccer Dashboard 🎮")

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Welcome to your personal Soccer Dashboard! This is where we bring all your data together in one place.")
    st.write("Data dashboards are what real data scientists use to track important information. Let's create your own!")

st.write("Let's put everything together to create your soccer dashboard!")

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
    # Sort by date
    with st.expander("👀 See the code that sorts your data by date", expanded=False):
        st.code("""
        # This sorts the data from oldest to newest
        my_data = my_data.sort_values("Date")
        """)
    
    my_data = my_data.sort_values("Date")
    
    # Get the most recent session
    with st.expander("👀 See the code that gets your latest session", expanded=False):
        st.code("""
        # This gets your most recent session data
        latest_session = my_data.iloc[-1]
        """)
    
    latest_session = my_data.iloc[-1]
    
    # Show a personal welcome message
    st.write(f"## Welcome to your dashboard, {player_name}!")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("Let's start by showing your key stats! These numbers give a quick summary of all your sessions.")
    
    # Create 3 columns for key stats
    with st.expander("👀 See the code that creates your key stats", expanded=False):
        st.code("""
        # This creates three columns with your total distance, top speed, and session count
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_distance = my_data["Distance (km)"].sum()
            st.metric("Total Distance", f"{total_distance:.2f} km")
        
        with col2:
            top_speed = my_data["Top Speed (m/s)"].max()
            top_speed_mph = top_speed * 2.237
            st.metric("Top Speed", f"{top_speed_mph:.2f} mph")
        
        with col3:
            total_sessions = len(my_data)
            st.metric("Total Sessions", total_sessions)
        """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_distance = my_data["Distance (km)"].sum()
        st.metric("Total Distance", f"{total_distance:.2f} km")
    
    with col2:
        top_speed = my_data["Top Speed (m/s)"].max()
        top_speed_mph = top_speed * 2.237
        st.metric("Top Speed", f"{top_speed_mph:.2f} mph")
    
    with col3:
        total_sessions = len(my_data)
        st.metric("Total Sessions", total_sessions)
    
    # Create tabs for different sections
    with st.expander("👀 See the code that creates the tabs", expanded=False):
        st.code("""
        # This creates three tabs to organize different types of information
        tab1, tab2, tab3 = st.tabs(["Distance & Speed", "Sprints & Power", "Achievements"])
        """)
    
    tab1, tab2, tab3 = st.tabs(["Distance & Speed", "Sprints & Power", "Achievements"])
    
    with tab1:
        st.subheader("Distance Over Time")
        
        coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
        with coach_message:
            st.write("This chart shows how far you ran in each session. Looking for patterns can help you understand your training.")
        
        # Create a line chart of distance
        with st.expander("👀 See the code that creates the distance chart", expanded=False):
            st.code("""
            # This creates a line chart showing distance in each session
            sessions = my_data["Session Title"].tolist()
            distances = my_data["Distance (km)"].tolist()
            
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(sessions, distances, marker='o', linestyle='-', color='blue')
            
            # Add labels
            ax.set_xlabel('Session')
            ax.set_ylabel('Distance (km)')
            ax.set_title('Distance Run in Each Session')
            
            # Rotate x-axis labels
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            """)
        
        sessions = my_data["Session Title"].tolist()
        distances = my_data["Distance (km)"].tolist()
        
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(sessions, distances, marker='o', linestyle='-', color='blue')
        
        # Add labels
        ax.set_xlabel('Session')
        ax.set_ylabel('Distance (km)')
        ax.set_title('Distance Run in Each Session')
        
        # Rotate x-axis labels
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        st.pyplot(fig)
        
        st.subheader("Top Speed Progression")
        
        coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
        with coach_message:
            st.write("This chart shows your top speed for each session. Are you getting faster over time?")
        
        # Create a line chart of top speed
        with st.expander("👀 See the code that creates the speed chart", expanded=False):
            st.code("""
            # This creates a line chart showing top speed in each session
            top_speeds = my_data["Top Speed (m/s)"].tolist()
            top_speeds_mph = [speed * 2.237 for speed in top_speeds]
            
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(sessions, top_speeds_mph, marker='o', linestyle='-', color='green')
            
            # Add labels
            ax.set_xlabel('Session')
            ax.set_ylabel('Top Speed (mph)')
            ax.set_title('Top Speed in Each Session')
            
            # Rotate x-axis labels
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            """)
        
        top_speeds = my_data["Top Speed (m/s)"].tolist()
        top_speeds_mph = [speed * 2.237 for speed in top_speeds]
        
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(sessions, top_speeds_mph, marker='o', linestyle='-', color='green')
        
        # Add labels
        ax.set_xlabel('Session')
        ax.set_ylabel('Top Speed (mph)')
        ax.set_title('Top Speed in Each Session')
        
        # Rotate x-axis labels
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        st.pyplot(fig)
        
        # Calculate improvement
        if len(top_speeds) >= 2:
            with st.expander("👀 See the code that calculates your improvement", expanded=False):
                st.code("""
                # This calculates how much your speed has improved
                first_speed = top_speeds[0]
                last_speed = top_speeds[-1]
                
                speed_change = ((last_speed - first_speed) / first_speed) * 100
                
                if speed_change > 0:
                    st.success(f"Your top speed has improved by {speed_change:.1f}% since your first session!")
                elif speed_change < 0:
                    st.warning(f"Your top speed has decreased by {abs(speed_change):.1f}% since your first session.")
                else:
                    st.info("Your top speed has remained the same.")
                """)
            
            first_speed = top_speeds[0]
            last_speed = top_speeds[-1]
            
            speed_change = ((last_speed - first_speed) / first_speed) * 100
            
            if speed_change > 0:
                st.success(f"Your top speed has improved by {speed_change:.1f}% since your first session!")
            elif speed_change < 0:
                st.warning(f"Your top speed has decreased by {abs(speed_change):.1f}% since your first session.")
            else:
                st.info("Your top speed has remained the same.")
            
            coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
            with coach_message:
                if speed_change > 0:
                    st.write("Great improvement! Keep up the good work!")
                elif speed_change < 0:
                    st.write("Don't worry about the decrease - speed can vary from session to session based on many factors.")
                else:
                    st.write("Consistency is key! Your speed has remained stable.")
    
    with tab2:
        st.subheader("Sprint Distance")
        
        coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
        with coach_message:
            st.write("Sprinting is crucial in soccer. This chart shows how much sprinting you did in each session.")
        
        # Get sprint distances
        with st.expander("👀 See the code that creates the sprint chart", expanded=False):
            st.code("""
            # This creates a bar chart showing sprint distance in each session
            sprint_distances = my_data["Sprint Distance (m)"].tolist()
            
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.bar(sessions, sprint_distances, color='purple')
            
            # Add labels
            ax.set_xlabel('Session')
            ax.set_ylabel('Sprint Distance (m)')
            ax.set_title('Sprint Distance in Each Session')
            
            # Rotate x-axis labels
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            """)
        
        sprint_distances = my_data["Sprint Distance (m)"].tolist()
        
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.bar(sessions, sprint_distances, color='purple')
        
        # Add labels
        ax.set_xlabel('Session')
        ax.set_ylabel('Sprint Distance (m)')
        ax.set_title('Sprint Distance in Each Session')
        
        # Rotate x-axis labels
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        st.pyplot(fig)
        
        st.subheader("Power Plays")
        
        coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
        with coach_message:
            st.write("Power plays are quick bursts of energy. This chart shows how many you performed in each session.")
        
        # Get power plays
        with st.expander("👀 See the code that creates the power plays chart", expanded=False):
            st.code("""
            # This creates a bar chart showing power plays in each session
            power_plays = my_data["Power Plays"].tolist()
            
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.bar(sessions, power_plays, color='orange')
            
            # Add labels
            ax.set_xlabel('Session')
            ax.set_ylabel('Number of Power Plays')
            ax.set_title('Power Plays in Each Session')
            
            # Rotate x-axis labels
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            """)
        
        power_plays = my_data["Power Plays"].tolist()
        
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.bar(sessions, power_plays, color='orange')
        
        # Add labels
        ax.set_xlabel('Session')
        ax.set_ylabel('Number of Power Plays')
        ax.set_title('Power Plays in Each Session')
        
        # Rotate x-axis labels
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        st.pyplot(fig)
        
        # Show a comparison of average vs. latest session
        st.subheader("Your Last Session vs. Average")
        
        coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
        with coach_message:
            st.write("This table compares your most recent session with your overall average. This helps track your progress.")
        
        with st.expander("👀 See the code that creates the comparison table", expanded=False):
            st.code("""
            # This creates a comparison table between your latest session and your average
            metrics = ["Distance (km)", "Sprint Distance (m)", "Power Plays", "Top Speed (m/s)"]
            latest_values = [
                latest_session["Distance (km)"],
                latest_session["Sprint Distance (m)"],
                latest_session["Power Plays"],
                latest_session["Top Speed (m/s)"]
            ]
            
            avg_values = [
                my_data["Distance (km)"].mean(),
                my_data["Sprint Distance (m)"].mean(),
                my_data["Power Plays"].mean(),
                my_data["Top Speed (m/s)"].mean()
            ]
            
            # Create a comparison table
            comparison = {
                "Metric": metrics,
                "Latest Session": [f"{val:.2f}" for val in latest_values],
                "Your Average": [f"{val:.2f}" for val in avg_values]
            }
            
            comparison_df = pd.DataFrame(comparison)
            """)
        
        metrics = ["Distance (km)", "Sprint Distance (m)", "Power Plays", "Top Speed (m/s)"]
        latest_values = [
            latest_session["Distance (km)"],
            latest_session["Sprint Distance (m)"],
            latest_session["Power Plays"],
            latest_session["Top Speed (m/s)"]
        ]
        
        avg_values = [
            my_data["Distance (km)"].mean(),
            my_data["Sprint Distance (m)"].mean(),
            my_data["Power Plays"].mean(),
            my_data["Top Speed (m/s)"].mean()
        ]
        
        # Create a comparison table
        comparison = {
            "Metric": metrics,
            "Latest Session": [f"{val:.2f}" for val in latest_values],
            "Your Average": [f"{val:.2f}" for val in avg_values]
        }
        
        comparison_df = pd.DataFrame(comparison)
        st.table(comparison_df)
    
    with tab3:
        st.subheader("Your Achievements")
        
        coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
        with coach_message:
            st.write("Achievements help track your progress and make learning more fun. Let's see what you've earned!")
        
        # Define some achievements
        with st.expander("👀 See the code that creates the achievements", expanded=False):
            st.code("""
            # This creates a list of achievements you can earn
            achievements = []
            
            # Distance achievements
            if total_distance >= 10:
                achievements.append({
                    "name": "10K Club",
                    "description": "Run a total of 10 kilometers or more",
                    "earned": True
                })
            else:
                achievements.append({
                    "name": "10K Club",
                    "description": f"Run a total of 10 kilometers (currently {total_distance:.2f} km)",
                    "earned": False,
                    "progress": total_distance / 10
                })
            
            # Speed achievements
            if top_speed * 2.237 >= 15:  # Convert to mph
                achievements.append({
                    "name": "Speed Demon",
                    "description": "Reach a top speed of 15 mph or higher",
                    "earned": True
                })
            else:
                achievements.append({
                    "name": "Speed Demon",
                    "description": f"Reach a top speed of 15 mph (currently {top_speed * 2.237:.2f} mph)",
                    "earned": False,
                    "progress": (top_speed * 2.237) / 15
                })
            
            # Session achievements
            if total_sessions >= 5:
                achievements.append({
                    "name": "Consistent Player",
                    "description": "Complete 5 or more sessions",
                    "earned": True
                })
            else:
                achievements.append({
                    "name": "Consistent Player",
                    "description": f"Complete 5 sessions (currently {total_sessions})",
                    "earned": False,
                    "progress": total_sessions / 5
                })
            
            # Power play achievements
            total_power_plays = my_data["Power Plays"].sum()
            if total_power_plays >= 50:
                achievements.append({
                    "name": "Power Player",
                    "description": "Complete 50 or more power plays",
                    "earned": True
                })
            else:
                achievements.append({
                    "name": "Power Player",
                    "description": f"Complete 50 power plays (currently {total_power_plays})",
                    "earned": False,
                    "progress": total_power_plays / 50
                })
            """)
        
        achievements = []
        
        # Distance achievements
        if total_distance >= 10:
            achievements.append({
                "name": "10K Club",
                "description": "Run a total of 10 kilometers or more",
                "earned": True
            })
        else:
            achievements.append({
                "name": "10K Club",
                "description": f"Run a total of 10 kilometers (currently {total_distance:.2f} km)",
                "earned": False,
                "progress": total_distance / 10
            })
        
        # Speed achievements
        if top_speed * 2.237 >= 15:  # Convert to mph
            achievements.append({
                "name": "Speed Demon",
                "description": "Reach a top speed of 15 mph or higher",
                "earned": True
            })
        else:
            achievements.append({
                "name": "Speed Demon",
                "description": f"Reach a top speed of 15 mph (currently {top_speed * 2.237:.2f} mph)",
                "earned": False,
                "progress": (top_speed * 2.237) / 15
            })
        
        # Session achievements
        if total_sessions >= 5:
            achievements.append({
                "name": "Consistent Player",
                "description": "Complete 5 or more sessions",
                "earned": True
            })
        else:
            achievements.append({
                "name": "Consistent Player",
                "description": f"Complete 5 sessions (currently {total_sessions})",
                "earned": False,
                "progress": total_sessions / 5
            })
        
        # Power play achievements
        total_power_plays = my_data["Power Plays"].sum()
        if total_power_plays >= 50:
            achievements.append({
                "name": "Power Player",
                "description": "Complete 50 or more power plays",
                "earned": True
            })
        else:
            achievements.append({
                "name": "Power Player",
                "description": f"Complete 50 power plays (currently {total_power_plays})",
                "earned": False,
                "progress": total_power_plays / 50
            })
        
        # Display achievements
        with st.expander("👀 See the code that displays your achievements", expanded=False):
            st.code("""
            # This calculates and displays your achievement progress
            earned_count = sum(1 for a in achievements if a["earned"])
            st.write(f"You've earned {earned_count} out of {len(achievements)} achievements!")
            
            # Show earned achievements
            st.write("### Earned Achievements")
            for achievement in achievements:
                if achievement["earned"]:
                    st.success(f"**{achievement['name']}**: {achievement['description']}")
            
            # Show in-progress achievements
            st.write("### Achievements In Progress")
            for achievement in achievements:
                if not achievement["earned"]:
                    st.info(f"**{achievement['name']}**: {achievement['description']}")
                    st.progress(min(1.0, achievement["progress"]))
            """)
        
        earned_count = sum(1 for a in achievements if a["earned"])
        st.write(f"You've earned {earned_count} out of {len(achievements)} achievements!")
        
        # Show earned achievements
        st.write("### Earned Achievements")
        for achievement in achievements:
            if achievement["earned"]:
                st.success(f"**{achievement['name']}**: {achievement['description']}")
        
        # Show in-progress achievements
        st.write("### Achievements In Progress")
        for achievement in achievements:
            if not achievement["earned"]:
                st.info(f"**{achievement['name']}**: {achievement['description']}")
                st.progress(min(1.0, achievement["progress"]))
        
        # Add a math challenge related to achievements
        st.subheader("Achievement Math Challenge")
        
        coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
        with coach_message:
            st.write("Let's test your math skills with a challenge related to your achievements!")
        
        # Pick an in-progress achievement for the challenge
        in_progress = [a for a in achievements if not a["earned"]]
        
        if in_progress:
            with st.expander("👀 See the code that creates the math challenge", expanded=False):
                st.code("""
                # This creates a math challenge based on your achievements
                challenge = in_progress[0]
                
                if "10K Club" in challenge["name"]:
                    remaining = 10 - total_distance
                    st.write(f"You've run {total_distance:.2f} km out of 10 km needed for the 10K Club achievement.")
                    st.write(f"How many more kilometers do you need to run?")
                    
                    user_answer = st.number_input("Enter your answer in km:", 
                                                min_value=0.0, max_value=10.0, value=0.0, step=0.1)
                """)
            
            challenge = in_progress[0]
            
            if "10K Club" in challenge["name"]:
                remaining = 10 - total_distance
                st.write(f"You've run {total_distance:.2f} km out of 10 km needed for the 10K Club achievement.")
                st.write(f"How many more kilometers do you need to run?")
                
                user_answer = st.number_input("Enter your answer in km:", 
                                            min_value=0.0, max_value=10.0, value=0.0, step=0.1)
                
                if st.button("Check my answer"):
                    if abs(user_answer - remaining) < 0.2:
                        st.success(f"Correct! You need {remaining:.2f} more kilometers.")
                        st.balloons()
                    else:
                        st.error(f"Not quite. You need {remaining:.2f} more kilometers.")
                        st.write(f"To solve this, we subtract: 10 - {total_distance:.2f} = {remaining:.2f}")
            
            elif "Speed Demon" in challenge["name"]:
                current = top_speed * 2.237  # mph
                remaining = 15 - current
                st.write(f"Your top speed is {current:.2f} mph, and you need 15 mph for the Speed Demon achievement.")
                st.write(f"How much faster do you need to go?")
                
                user_answer = st.number_input("Enter your answer in mph:", 
                                            min_value=0.0, max_value=10.0, value=0.0, step=0.1)
                
                if st.button("Check my answer"):
                    if abs(user_answer - remaining) < 0.2:
                        st.success(f"Correct! You need to go {remaining:.2f} mph faster.")
                        st.balloons()
                    else:
                        st.error(f"Not quite. You need to go {remaining:.2f} mph faster.")
                        st.write(f"To solve this, we subtract: 15 - {current:.2f} = {remaining:.2f}")
            
            coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
            with coach_message:
                st.write("Great job working through this dashboard! You've now seen how data scientists use dashboards to track important information.")
                st.write("Keep playing soccer and checking your data - you'll earn more achievements and see your progress over time!")
