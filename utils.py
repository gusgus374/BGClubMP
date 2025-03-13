import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

def excel_date_to_datetime(excel_date):
    """
    Convert Excel date serial number to Python datetime object.
    
    Args:
        excel_date (float): Excel date serial number (e.g., 45723.693652535)
        
    Returns:
        datetime: Python datetime object
    """
    if pd.isna(excel_date):
        return pd.NaT
    
    # Excel dates start at January 1, 1900
    # The pandas method handles the Excel epoch and leap year bug correctly
    return pd.Timestamp('1899-12-30') + pd.Timedelta(days=excel_date)

def load_catapult_data(file_path):
    """
    Process a Catapult CSV file:
    1. Convert date columns to readable datetime
    2. Filter out unnecessary columns
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Processed DataFrame with converted dates and filtered columns
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Convert date columns to readable formats
    if 'Date' in df.columns:
        df['Date_Readable'] = df['Date'].apply(excel_date_to_datetime)
        # Replace the original Date column with the readable version
        df['Date'] = df['Date_Readable']
        df.drop('Date_Readable', axis=1, inplace=True)
    
    if 'Split Start Time' in df.columns:
        df['Split Start Time_Readable'] = df['Split Start Time'].apply(excel_date_to_datetime)
        df['Split Start Time'] = df['Split Start Time_Readable']
        df.drop('Split Start Time_Readable', axis=1, inplace=True)
    
    if 'Split End Time' in df.columns:
        df['Split End Time_Readable'] = df['Split End Time'].apply(excel_date_to_datetime)
        df['Split End Time'] = df['Split End Time_Readable']
        df.drop('Split End Time_Readable', axis=1, inplace=True)
    
    # Define columns to keep (essential for soccer analysis)
    essential_columns = [
        'Date', 'Session Title', 'Player Name', 'Split Name', 'Tags',
        'Split Start Time', 'Split End Time', 'Duration', 
        'Distance (km)', 'Sprint Distance (m)', 'Power Plays', 
        'Player Load', 'Top Speed (m/s)', 'Distance Per Min (m/min)',
        'Power Score (w/kg)', 'Work Ratio',
        'Max Deceleration (m/s/s)', 'Max Acceleration (m/s/s)',
        'Distance in Speed Zone 1  (km)', 'Distance in Speed Zone 2  (km)', 
        'Distance in Speed Zone 3  (km)', 'Distance in Speed Zone 4  (km)', 
        'Distance in Speed Zone 5  (km)',
        'Time in Speed Zone 1 (secs)', 'Time in Speed Zone 2 (secs)', 
        'Time in Speed Zone 3 (secs)', 'Time in Speed Zone 4 (secs)', 
        'Time in Speed Zone 5 (secs)',
        'Impacts', 'Energy (kcal)'
    ]
    
    # Filter to only keep necessary columns if they exist in the DataFrame
    columns_to_keep = [col for col in essential_columns if col in df.columns]
    df_filtered = df[columns_to_keep]
    
    return df_filtered 