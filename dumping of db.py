import pandas as pd
from sqlalchemy import create_engine

# Read the Excel file into a DataFrame
excel_file = 'your_excel_file.xlsx'
df = pd.read_excel(excel_file)

# Mapping columns from Excel to database columns
column_mapping = {
    'Excel_Column1': 'Database_Column1',
    'Excel_Column2': 'Database_Column2',
    # Add more mappings for other columns as needed
}

# Rename columns according to the mapping
df.rename(columns=column_mapping, inplace=True)

# Connect to the MySQL database
db_username = 'your_username'
db_password = 'your_password'
db_host = 'localhost'  # Change this if MySQL server is hosted elsewhere
db_name = 'your_database_name'
db_port = '3306'  # Default MySQL port

db_url = f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(db_url)

# Insert data into the database
df.to_sql('your_table_name', con=engine, if_exists='append', index=False)

# Close the database connection
engine.dispose()
