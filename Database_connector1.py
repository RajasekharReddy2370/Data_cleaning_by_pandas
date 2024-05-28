import os
import mysql.connector
import pandas as pd
import re
import numpy as np

# Establish MySQL connection
conn = mysql.connector.connect(
    host='localhost',
    database='ap',
    user='RAJ',
    password='Raj@2370'
)
cur = conn.cursor()

# Get list of Excel files in folder
folder_path = r"/home/rajashekar/Desktop/New Folderdb1"
excel_files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]

# Iterate through each Excel file
for excel_file in excel_files:
    # Use part of Excel file name as table name
    # table_name1 = excel_file.split("-")[1]  # Use second part of file name as table name
    # table_name = table_name1.split(".")[0]  # Remove file extension
    table_name = excel_file.split("-")[1].split(".")[0].replace(" ", "_").title()
    print(table_name)

    # Read Excel file into a DataFrame
    df = pd.read_excel(os.path.join(folder_path, excel_file))

    # Create table if not exists with column names from Excel file
    if not df.empty:
        columns = ', '.join([f"`{col}` VARCHAR(255)" for col in df.columns])  # Backticks around column names
        cur.execute(f"CREATE TABLE IF NOT EXISTS `{table_name}` ({columns})")

        # Iterate through DataFrame and insert rows into MySQL table
        for _, row in df.iterrows():
            columns = ', '.join([f"`{col}`" for col in df.columns])  # Backticks around column names
            placeholders = ', '.join(['%s'] * len(df.columns))
            query = f"INSERT INTO `{table_name}` ({columns}) VALUES ({placeholders})"
            values = tuple(None if pd.isna(val) else val for val in row)  # Convert NaN to None
            cur.execute(query, values)

        # Commit the transaction
        conn.commit()

# Close cursor and connection
cur.close()
conn.close()
print("SUCCESS")
