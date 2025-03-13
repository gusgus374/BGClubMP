import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Import our custom utility function
from utils import load_catapult_data

st.title("📅 My Soccer Calendar 📅")

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Welcome to your Soccer Calendar! Today we'll track your soccer activities over time.")
    st.write("Tracking patterns in your training and games is important for improving as a player and understanding your data.")

st.write("Let's track your soccer activities over time!")

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
    # Convert Date column to a readable format
    with st.expander("👀 See the code that creates readable dates", expanded=False):
        st.code("""
        # In the Catapult data, Date is stored as an integer offset
        # This code creates a simple readable date for display
        my_data["ReadableDate"] = my_data["Date"].apply(lambda x: f"Day {x - min(my_data['Date']) + 1}")
        """)
    
    # In the Catapult data, Date is stored as an integer offset
    # Let's create a simple readable date for display
    my_data["ReadableDate"] = my_data["Date"].apply(lambda x: f"Day {x - min(my_data['Date']) + 1}")
    
    # Sort by date
    with st.expander("👀 See the code that sorts your data by date", expanded=False):
        st.code("""
        # This sorts the data from oldest to newest
        my_data = my_data.sort_values("Date")
        """)
    
    my_data = my_data.sort_values("Date")
    
    st.subheader("Your Soccer Sessions")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("Let's create a simple calendar view of your soccer sessions. This helps us see how often you train and how much distance you cover each time.")
    
    # Create a simple calendar view
    with st.expander("👀 See the code that creates your calendar", expanded=False):
        st.code("""
        # This creates lists of your session information
        dates = my_data["ReadableDate"].tolist()
        session_types = my_data["Split Name"].tolist()
        distances = my_data["Distance (km)"].tolist()
        
        # Create a table with this information
        calendar_data = {
            "Day": dates,
            "Session Type": session_types,
            "Distance (km)": [f"{d:.2f}" for d in distances]
        }
        
        calendar_df = pd.DataFrame(calendar_data)
        """)
    
    dates = my_data["ReadableDate"].tolist()
    session_types = my_data["Split Name"].tolist()
    distances = my_data["Distance (km)"].tolist()
    
    # Create a table
    calendar_data = {
        "Day": dates,
        "Session Type": session_types,
        "Distance (km)": [f"{d:.2f}" for d in distances]
    }
    
    calendar_df = pd.DataFrame(calendar_data)
    st.table(calendar_df)
    
    # Calculate some patterns
    st.subheader("Activity Patterns")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("Now let's look for patterns in your training. How many days do you usually have between sessions? Do you run more or less distance over time?")
    
    # Count days between sessions
    with st.expander("👀 See the code that calculates days between sessions", expanded=False):
        st.code("""
        # This calculates how many days between each session
        days_between = []
        prev_day = None
        
        for day in my_data["Date"]:
            if prev_day is not None:
                days_between.append(day - prev_day)
            prev_day = day
        
        if len(days_between) > 0:
            avg_days_between = sum(days_between) / len(days_between)
        """)
    
    days_between = []
    prev_day = None
    
    for day in my_data["Date"]:
        if prev_day is not None:
            days_between.append(day - prev_day)
        prev_day = day
    
    if len(days_between) > 0:
        avg_days_between = sum(days_between) / len(days_between)
        st.write(f"On average, you had {avg_days_between:.1f} days between sessions.")
        
        # Create a pattern visual
        st.write("Your activity pattern (distance per session):")
        
        # Create a line chart
        with st.expander("👀 See the code that creates your pattern chart", expanded=False):
            st.code("""
            # This creates a line chart showing distance over time
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(dates, distances, marker='o', linestyle='-', color='blue')
            
            # Add labels
            ax.set_xlabel('Session')
            ax.set_ylabel('Distance (km)')
            ax.set_title('Distance Run in Each Session')
            
            # Rotate x-axis labels
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            """)
        
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(dates, distances, marker='o', linestyle='-', color='blue')
        
        # Add labels
        ax.set_xlabel('Session')
        ax.set_ylabel('Distance (km)')
        ax.set_title('Distance Run in Each Session')
        
        # Rotate x-axis labels
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        st.pyplot(fig)
        
        # Calculate your weekly totals (if we have enough data)
        if len(my_data) >= 7:
            st.subheader("Weekly Totals")
            
            coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
            with coach_message:
                st.write("Let's look at your weekly totals. This helps us see if you're running more or less each week.")
                st.write("This is important for tracking training load and making sure you're not doing too much too quickly.")
            
            # Try to group by week (this is simplified)
            with st.expander("👀 See the code that calculates weekly totals", expanded=False):
                st.code("""
                # This groups your sessions approximately by week
                weeks = []
                week_distances = []
                
                # Group approximately by 7 days
                for i in range(0, len(my_data), 7):
                    week_data = my_data.iloc[i:i+7]
                    weeks.append(f"Week {i//7 + 1}")
                    week_distances.append(week_data["Distance (km)"].sum())
                """)
            
            # Group approximately by 7 days
            weeks = []
            week_distances = []
            
            for i in range(0, len(my_data), 7):
                week_data = my_data.iloc[i:i+7]
                weeks.append(f"Week {i//7 + 1}")
                week_distances.append(week_data["Distance (km)"].sum())
            
            # Create a bar chart for weekly totals
            with st.expander("👀 See the code that creates the weekly chart", expanded=False):
                st.code("""
                # This creates a bar chart for weekly totals
                fig, ax = plt.subplots(figsize=(10, 4))
                ax.bar(weeks, week_distances, color='green')
                
                # Add labels
                ax.set_xlabel('Week')
                ax.set_ylabel('Total Distance (km)')
                ax.set_title('Total Distance Run Each Week')
                """)
            
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.bar(weeks, week_distances, color='green')
            
            # Add labels
            ax.set_xlabel('Week')
            ax.set_ylabel('Total Distance (km)')
            ax.set_title('Total Distance Run Each Week')
            
            st.pyplot(fig)
            
            # Add some fraction practice with weekly data
            if len(weeks) > 1:
                st.subheader("Weekly Comparison")
                
                coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
                with coach_message:
                    st.write("Let's practice comparing your weeks using ratios and percentages!")
                
                # Let's compare two weeks
                with st.expander("👀 See the code that compares weeks", expanded=False):
                    st.code("""
                    # This compares your first two weeks
                    week1 = week_distances[0]
                    week2 = week_distances[1] if len(week_distances) > 1 else 0
                    
                    # Calculate the ratio
                    if week1 > 0 and week2 > 0:
                        ratio = week2 / week1
                        
                        # Calculate percentage change
                        percent_change = (week2 - week1) / week1 * 100
                    """)
                
                week1 = week_distances[0]
                week2 = week_distances[1] if len(week_distances) > 1 else 0
                
                st.write(f"Week 1 distance: {week1:.2f} km")
                st.write(f"Week 2 distance: {week2:.2f} km")
                
                # Calculate the ratio
                if week1 > 0 and week2 > 0:
                    ratio = week2 / week1
                    
                    st.write(f"Week 2 was {ratio:.2f} times Week 1.")
                    
                    # Let's phrase it as a percentage increase/decrease
                    percent_change = (week2 - week1) / week1 * 100
                    
                    if percent_change > 0:
                        st.write(f"That's a {percent_change:.1f}% increase from Week 1 to Week 2.")
                    else:
                        st.write(f"That's a {abs(percent_change):.1f}% decrease from Week 1 to Week 2.")
                    
                    # Math challenge
                    st.subheader("Quick Math Challenge")
                    
                    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
                    with coach_message:
                        st.write("Let's practice finding the difference between two values.")
                        st.write(f"If Week 1 was {week1:.2f} km and Week 2 was {week2:.2f} km, what's the difference?")
                    
                    st.write(f"If Week 1 was {week1:.2f} km and Week 2 was {week2:.2f} km, what's the difference?")
                    
                    user_diff = st.number_input("Enter the difference in km:", 
                                              min_value=0.0, max_value=20.0, value=0.0, step=0.1)
                    
                    actual_diff = abs(week2 - week1)
                    
                    if st.button("Check my answer"):
                        with st.expander("👀 See the code that checks your answer", expanded=False):
                            st.code("""
                            # This checks if your answer is close to correct
                            actual_diff = abs(week2 - week1)
                            
                            if abs(user_diff - actual_diff) < 0.1:
                                st.success(f"Correct! The difference is {actual_diff:.2f} km.")
                                st.balloons()
                            else:
                                st.error(f"Not quite. The difference is {actual_diff:.2f} km.")
                                st.write(f"To find the difference, we subtract: {max(week1, week2):.2f} - {min(week1, week2):.2f} = {actual_diff:.2f}")
                            """)
                        
                        if abs(user_diff - actual_diff) < 0.1:
                            st.success(f"Correct! The difference is {actual_diff:.2f} km.")
                            st.balloons()
                        else:
                            st.error(f"Not quite. The difference is {actual_diff:.2f} km.")
                            st.write(f"To find the difference, we subtract: {max(week1, week2):.2f} - {min(week1, week2):.2f} = {actual_diff:.2f}")
                            
                            coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
                            with coach_message:
                                st.write("Finding the difference between two numbers is important for comparing values in data science.")
                                st.write("You can always find the difference by subtracting the smaller number from the larger one.")
