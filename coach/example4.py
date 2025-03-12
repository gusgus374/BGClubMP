import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Soccer Stats Chart Maker 📊")

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Welcome to the Chart Maker! Today, we'll learn how to create visual charts from your soccer data.")
    st.write("Data scientists use charts to understand patterns and trends that might be hard to see in just numbers.")

st.write("Let's create your first chart to visualize soccer data!")

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

# Sort the data by date
with st.expander("👀 See the code that sorts your data by date", expanded=False):
    st.code("""
    # This sorts the data by date (oldest to newest)
    my_data = my_data.sort_values("Date")
    """)

my_data = my_data.sort_values("Date")

st.subheader("Chart Creator")
st.write("Let's make a chart to see how different stats changed over time.")

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Charts help us visualize data. With your soccer data, we can see how different stats like distance or speed changed from session to session.")
    st.write("Choose what you want to see from the dropdown below:")

# Let the user pick what to show
with st.expander("👀 See the code that creates the stat selector", expanded=False):
    st.code("""
    # This creates a dropdown to select which stat to chart
    stat_options = [
        "Distance (km)", 
        "Top Speed (m/s)", 
        "Sprint Distance (m)",
        "Power Plays",
        "Player Load"
    ]
    selected_stat = st.selectbox("What do you want to see in your chart?", stat_options)
    """)

stat_options = [
    "Distance (km)", 
    "Top Speed (m/s)", 
    "Sprint Distance (m)",
    "Power Plays",
    "Player Load"
]
selected_stat = st.selectbox("What do you want to see in your chart?", stat_options)

if len(my_data) > 0:
    # Create a simple bar chart
    with st.expander("👀 See the code that creates the chart", expanded=False):
        st.code("""
        # This creates a bar chart
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # Get just the columns we need
        sessions = my_data["Session Title"].tolist()
        values = my_data[selected_stat].tolist()
        
        # Create the bars
        ax.bar(sessions, values, color='blue')
        
        # Add labels
        ax.set_xlabel('Session')
        ax.set_ylabel(selected_stat)
        ax.set_title(f'Your {selected_stat} in Each Session')
        
        # Rotate the session labels so they don't overlap
        plt.xticks(rotation=45, ha='right')
        
        # Make sure everything fits
        plt.tight_layout()
        """)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Get just the columns we need
    sessions = my_data["Session Title"].tolist()
    values = my_data[selected_stat].tolist()
    
    # Create the bars
    ax.bar(sessions, values, color='blue')
    
    # Add labels
    ax.set_xlabel('Session')
    ax.set_ylabel(selected_stat)
    ax.set_title(f'Your {selected_stat} in Each Session')
    
    # Rotate the session labels so they don't overlap
    plt.xticks(rotation=45, ha='right')
    
    # Make sure everything fits
    plt.tight_layout()
    
    # Show the chart
    st.pyplot(fig)
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("Great! You just created your first data visualization chart!")
        st.write("Now let's use your data to practice some important math concepts like finding minimums, maximums, averages, and ranges.")
    
    # Explain the chart
    st.subheader("Understanding Your Chart")
    st.write("A bar chart shows values as bars. Taller bars mean higher values.")
    
    # Calculate some basic stats to introduce mean and range
    with st.expander("👀 See the code that calculates your stats", expanded=False):
        st.code("""
        # This calculates basic statistics from your data
        min_value = min(values)
        max_value = max(values)
        avg_value = sum(values) / len(values)  # This is how you calculate an average
        """)
    
    min_value = min(values)
    max_value = max(values)
    avg_value = sum(values) / len(values)
    
    st.write(f"Your lowest {selected_stat} was: {min_value:.2f}")
    st.write(f"Your highest {selected_stat} was: {max_value:.2f}")
    st.write(f"Your average {selected_stat} was: {avg_value:.2f}")
    
    # Introduce the concept of range (max - min)
    with st.expander("👀 See the code that calculates the range", expanded=False):
        st.code("""
        # This calculates the range (difference between highest and lowest)
        range_value = max_value - min_value
        """)
    
    range_value = max_value - min_value
    st.write(f"The range of your {selected_stat} was: {range_value:.2f}")
    st.write("The range tells us how much your performance varied from session to session.")
    
    # Let's add a fun challenge about the math
    st.subheader("Quick Math Challenge")
    
    coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
    with coach_message:
        st.write("Let's practice working with ratios! Ratios help us compare different values.")
        st.write("Can you figure out how many times bigger your highest value is compared to your lowest?")
    
    # Calculate the ratio between max and min
    if min_value > 0:
        with st.expander("👀 See the code that calculates the ratio", expanded=False):
            st.code("""
            # This calculates the ratio between highest and lowest values
            ratio = max_value / min_value
            """)
        
        ratio = max_value / min_value
        st.write(f"Your highest {selected_stat} was {ratio:.1f} times your lowest.")
        
        # Let's check if they can figure out the ratio
        user_ratio = st.number_input("What's the ratio of your highest to lowest value? (Try to calculate it!)", 
                                    min_value=0.1, max_value=100.0, value=1.0, step=0.1)
        
        if st.button("Check my answer"):
            # Allow for a small error margin
            with st.expander("👀 See the code that checks your answer", expanded=False):
                st.code("""
                # This checks if your answer is close enough to correct
                if abs(user_ratio - ratio) < 0.2:
                    st.success("That's correct! Great job!")
                    st.balloons()
                else:
                    st.error(f"Not quite. The answer is {ratio:.1f}. Try dividing {max_value:.2f} by {min_value:.2f}")
                """)
            
            if abs(user_ratio - ratio) < 0.2:
                st.success("That's correct! Great job!")
                st.balloons()
            else:
                st.error(f"Not quite. The answer is {ratio:.1f}. Try dividing {max_value:.2f} by {min_value:.2f}")
                
                coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
                with coach_message:
                    st.write(f"To find the ratio, we divide the larger number by the smaller one: {max_value:.2f} ÷ {min_value:.2f} = {ratio:.1f}")
                    st.write("Keep practicing! This kind of math is really useful in data science.")
