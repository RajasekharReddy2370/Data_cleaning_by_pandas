import pandas as pd
import numpy as np

# Assuming df is your DataFrame with columns "Names", "Mobile", and "Gender"

# Create a DataFrame
data = {
    'Names': ['Alice', 'Bob', 'Charlie'],
    'Mobile': ['1234567890', '9876543210', '5555555555'],
    'Gender': ['Female', 'Male', 'nan']
}

df = pd.DataFrame(data)

# Filter the DataFrame to keep only 'Female' values and NaN in the 'Gender' column
df = df[(df['Gender'] != 'Male') | (df['Gender'].isna())]

print(df)
