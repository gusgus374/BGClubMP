import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Import our custom utility function
from utils import load_catapult_data

st.title("💪 Soccer Power Plays Counter 💪")

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Welcome to the Power Plays Counter! Today we'll learn about power plays in soccer and analyze your data.")
    st.write("Power plays are important moments in soccer where you quickly change speed or direction.")

st.write("Let's learn about power plays in soccer!")

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
    st.subheader("What is a 'Power Play' in soccer?")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("""
        A 'Power Play' is a burst of high-energy movement in soccer. 
        It happens when you quickly change speed or direction.
        Power plays are important because they often happen during key moments in the game,
        like when you're trying to beat a defender or sprint to get the ball.
        
        The GPS tracker counts a movement as a power play when you reach a certain power threshold.
        Let's look at your power play data!
        """)
    
    # Show their power play data
    sessions = my_data["Session Title"].tolist()
    
    # Get power play count for each session
    with st.expander("👀 See the code that gets your power play data", expanded=False):
        st.code("""
        # This gets power play counts for each session
        sessions = my_data["Session Title"].tolist()
        power_plays = my_data["Power Plays"].tolist()
        """)
    
    power_plays = my_data["Power Plays"].tolist()
    
    # Create a simple bar chart
    with st.expander("👀 See the code that creates the chart", expanded=False):
        st.code("""
        # This creates a bar chart showing power plays per session
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(sessions, power_plays, color='purple')
        
        # Add labels
        ax.set_xlabel('Session')
        ax.set_ylabel('Number of Power Plays')
        ax.set_title('Your Power Plays in Each Session')
        
        # Rotate session names
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        """)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sessions, power_plays, color='purple')
    
    # Add labels
    ax.set_xlabel('Session')
    ax.set_ylabel('Number of Power Plays')
    ax.set_title('Your Power Plays in Each Session')
    
    # Rotate session names
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    st.pyplot(fig)
    
    # Calculate totals and averages
    with st.expander("👀 See the code that calculates your stats", expanded=False):
        st.code("""
        # This calculates your total and average power plays
        total_power_plays = sum(power_plays)
        avg_power_plays = total_power_plays / len(power_plays)
        """)
    
    total_power_plays = sum(power_plays)
    avg_power_plays = total_power_plays / len(power_plays)
    
    st.write(f"You've made a total of {total_power_plays} power plays across all sessions!")
    st.write(f"That's an average of {avg_power_plays:.1f} power plays per session.")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write(f"Great job! {total_power_plays} power plays means you're making lots of explosive movements.")
        st.write("Now let's look at how long your power plays typically last. This can tell us about your playing style!")
    
    # Select a session for detailed analysis
    st.subheader("Power Play Duration Analysis")
    st.write("Power plays can last for different amounts of time.")
    
    with st.expander("👀 See the code that creates the session selector", expanded=False):
        st.code("""
        # This creates a dropdown to select a session for detailed analysis
        selected_session = st.selectbox("Choose a session for detailed analysis:", sessions)
        session_data = my_data[my_data["Session Title"] == selected_session].iloc[0]
        """)
    
    selected_session = st.selectbox("Choose a session for detailed analysis:", sessions)
    session_data = my_data[my_data["Session Title"] == selected_session].iloc[0]
    
    # Get power play duration zones
    with st.expander("👀 See the code that gets power play durations", expanded=False):
        st.code("""
        # This gets the count of power plays in different duration zones
        pp_zone1 = session_data["Power Play Duration Zones: 0 - 2.5 s (Power Plays)"]
        pp_zone2 = session_data["Power Play Duration Zones: 2.5 - 5 s (Power Plays)"]
        pp_zone3 = session_data["Power Play Duration Zones: 5 - 7.5 s (Power Plays)"]
        pp_zone4 = session_data["Power Play Duration Zones: 7.5 - 10 s (Power Plays)"]
        pp_zone5 = session_data["Power Play Duration Zones: > 10 s (Power Plays)"]
        """)
    
    pp_zone1 = session_data["Power Play Duration Zones: 0 - 2.5 s (Power Plays)"]
    pp_zone2 = session_data["Power Play Duration Zones: 2.5 - 5 s (Power Plays)"]
    pp_zone3 = session_data["Power Play Duration Zones: 5 - 7.5 s (Power Plays)"]
    pp_zone4 = session_data["Power Play Duration Zones: 7.5 - 10 s (Power Plays)"]
    pp_zone5 = session_data["Power Play Duration Zones: > 10 s (Power Plays)"]
    
    # Create labels for the zones
    with st.expander("👀 See the code that sets up the pie chart", expanded=False):
        st.code("""
        # This creates labels and values for the pie chart
        pp_zones = ["Very Short\\n(0-2.5s)", "Short\\n(2.5-5s)", "Medium\\n(5-7.5s)", 
                   "Long\\n(7.5-10s)", "Very Long\\n(>10s)"]
        pp_counts = [pp_zone1, pp_zone2, pp_zone3, pp_zone4, pp_zone5]
        """)
    
    pp_zones = ["Very Short\n(0-2.5s)", "Short\n(2.5-5s)", "Medium\n(5-7.5s)", 
               "Long\n(7.5-10s)", "Very Long\n(>10s)"]
    pp_counts = [pp_zone1, pp_zone2, pp_zone3, pp_zone4, pp_zone5]
    
    # Create a pie chart
    with st.expander("👀 See the code that creates the pie chart", expanded=False):
        st.code("""
        # This creates a pie chart
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Only include zones with non-zero values
        non_zero_zones = []
        non_zero_counts = []
        
        for zone, count in zip(pp_zones, pp_counts):
            if count > 0:
                non_zero_zones.append(zone)
                non_zero_counts.append(count)
        
        if sum(non_zero_counts) > 0:
            ax.pie(non_zero_counts, labels=non_zero_zones, autopct='%1.1f%%', 
                  startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
            
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        """)
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Only include zones with non-zero values
    non_zero_zones = []
    non_zero_counts = []
    
    for zone, count in zip(pp_zones, pp_counts):
        if count > 0:
            non_zero_zones.append(zone)
            non_zero_counts.append(count)
    
    if sum(non_zero_counts) > 0:
        ax.pie(non_zero_counts, labels=non_zero_zones, autopct='%1.1f%%', 
              startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
        
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        
        st.pyplot(fig)
        
        coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
        with coach_message:
            st.write("This pie chart shows the breakdown of your power plays by duration.")
            st.write("- Short power plays (0-5s) usually happen during quick direction changes or short sprints.")
            st.write("- Longer power plays (>5s) typically occur during extended sprints or high-intensity runs.")
            st.write("Now let's practice working with fractions and percentages!")
        
        # Let's do some fraction practice
        st.subheader("Fraction Practice")
        
        # Calculate what fraction each duration is of the total
        with st.expander("👀 See the code that calculates fractions", expanded=False):
            st.code("""
            # This calculates the fractions and percentages
            total_pp = sum(pp_counts)
            
            # Create a table
            pp_data = {
                "Duration": pp_zones,
                "Count": pp_counts,
                "Fraction": [f"{count}/{total_pp}" for count in pp_counts],
                "Decimal": [count/total_pp if total_pp > 0 else 0 for count in pp_counts],
                "Percentage": [count/total_pp*100 if total_pp > 0 else 0 for count in pp_counts]
            }
            """)
        
        total_pp = sum(pp_counts)
        
        # Create a table
        pp_data = {
            "Duration": pp_zones,
            "Count": pp_counts,
            "Fraction": [f"{count}/{total_pp}" for count in pp_counts],
            "Decimal": [count/total_pp if total_pp > 0 else 0 for count in pp_counts],
            "Percentage": [count/total_pp*100 if total_pp > 0 else 0 for count in pp_counts]
        }
        
        pp_df = pd.DataFrame(pp_data)
        st.table(pp_df)
        
        # Add a math challenge
        st.subheader("Math Challenge")
        
        coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
        with coach_message:
            st.write("Let's test your fraction skills with a challenge!")
        
        # Find the most common power play duration
        with st.expander("👀 See the code that finds the most common duration", expanded=False):
            st.code("""
            # This finds your most common power play duration
            max_index = pp_counts.index(max(pp_counts))
            most_common = pp_zones[max_index]
            most_common_count = pp_counts[max_index]
            """)
        
        max_index = pp_counts.index(max(pp_counts))
        most_common = pp_zones[max_index]
        most_common_count = pp_counts[max_index]
        
        st.write(f"Your most common power play duration is: {most_common} with {most_common_count} power plays.")
        
        # Create a fraction challenge
        st.write(f"What fraction of your power plays are {most_common}?")
        
        # The correct answer
        correct_fraction = most_common_count / total_pp
        
        with st.expander("👀 See the code that checks your answer", expanded=False):
            st.code("""
            # This sets up the fraction challenge
            user_answer = st.number_input("Enter your answer as a decimal:", 
                                        min_value=0.0, max_value=1.0, value=0.0, step=0.01)
            
            if st.button("Check my answer"):
                if abs(user_answer - correct_fraction) < 0.02:
                    st.success(f"Correct! The answer is {correct_fraction:.2f}")
                    st.balloons()
                else:
                    st.error(f"Not quite. The answer is {correct_fraction:.2f}")
                    st.write(f"To find this, we divide {most_common_count} by the total {total_pp}:")
                    st.write(f"{most_common_count} ÷ {total_pp} = {correct_fraction:.2f}")
            """)
        
        user_answer = st.number_input("Enter your answer as a decimal:", 
                                    min_value=0.0, max_value=1.0, value=0.0, step=0.01)
        
        if st.button("Check my answer"):
            if abs(user_answer - correct_fraction) < 0.02:
                st.success(f"Correct! The answer is {correct_fraction:.2f}")
                st.balloons()
            else:
                st.error(f"Not quite. The answer is {correct_fraction:.2f}")
                st.write(f"To find this, we divide {most_common_count} by the total {total_pp}:")
                st.write(f"{most_common_count} ÷ {total_pp} = {correct_fraction:.2f}")
                
                coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
                with coach_message:
                    st.write("Converting fractions to decimals is a key skill in data science.")
                    st.write("To find what fraction of the total something is, we divide the part by the whole.")
                    st.write("Keep practicing with different sessions to see how your power plays change!")
    else:
        st.write("No power plays recorded in this session.")
