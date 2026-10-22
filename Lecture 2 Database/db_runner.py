# import library (install first in terminal: pip install pandas)
import pandas as pd
import sqlite3
import os

# define path relative to this script, so it runs from any working directory
base_dir = os.path.dirname(os.path.abspath(__file__))
rawdata = os.path.join(base_dir, 'raw_data', 'db_booking_example_data.csv')
db_folder = os.path.join(base_dir, 'database')
db_path = os.path.join(db_folder, 'booking_db.db')
os.makedirs(db_folder, exist_ok=True)

# read csv then connect with sqlite3
dataframe = pd.read_csv(rawdata) 
conn = sqlite3.connect(db_path)

# change format to sql 
dataframe.to_sql('booking_sql', conn, if_exists='replace', index=False)

# query data with this command
cursor = conn.cursor() # 
query = """
SELECT room_type FROM booking_sql ; 
"""
cursor.execute(query)

results = cursor.fetchall()
for row in results:
    print(row[0])

conn.close()