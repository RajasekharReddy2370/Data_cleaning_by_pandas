import pandas as pd
import os
from datetime import datetime

main_file_path = r"/home/rajashekar/Desktop/Andhra_State_Daily_data/Machilipatnam/Machilipatnam_imported_Data/IMPORTED_DATA2"
files = os.listdir(main_file_path)

concat_df = pd.DataFrame()
for file in files:
    constituency = file.split()[0]

    df = pd.read_excel(main_file_path+'/'+file, usecols=['DOB',"Mobile"])

    df.dropna(subset=["DOB"],inplace=True)
    df.dropna(subset=["Mobile"],inplace=True)

    df = df[df["DOB"].str.len() == 10]  # Assuming the format is DD-MM-YYYY

    # Convert 'DOB' column to datetime, handling errors
    df['DOB'] = pd.to_datetime(df['DOB'], format='%d-%m-%Y', errors='coerce')

    # Get current year
    current_year = datetime.now().year

    # Calculate age, ignoring NaT values
    df['Age'] = current_year - df['DOB'].dt.year

    # Filter age group between 35 and 70
    age_filtered_df = df[(df['Age'] >= 18) & (df['Age'] <= 25)]

    age_filtered_df.dropna(subset=['Mobile'], inplace=True)

    def clean_mobile_number(mobile):
        # Try to convert mobile to float to handle scientific notation and remove decimals
        try:
            mobile_float = float(mobile)
            # Convert scientific notation to normal form and remove ".0" if it exists
            mobile = "{:.0f}".format(mobile_float)
        except ValueError:
            # If conversion fails, it's likely already a string that doesn't need conversion
            mobile = str(mobile)

        # Remove any trailing ".0"
        if mobile.endswith(".0"):
            mobile = mobile[:-2]

        return mobile

    # Apply the clean_mobile_number function to the 'Mobile' column
    age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(clean_mobile_number)

    # Convert the 'Mobile' column back to string type
    age_filtered_df['Mobile'] = age_filtered_df['Mobile'].astype(str)

    # Filter out non-digit mobile numbers and fix formatting
    age_filtered_df = age_filtered_df[age_filtered_df['Mobile'].str.isdigit()]  # Keep only digit mobile numbers
    age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(
        lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)  # Remove '91' prefix
    age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(
        lambda x: x if x.startswith(('6', '7', '8', '9')) and len(
            x) == 10 else None)  # Keep only 10-digit numbers starting with 6, 7, 8, or 9

    # Drop duplicate mobile numbers
    age_filtered_df.drop_duplicates(subset=["Mobile"], inplace=True)
    age_filtered_df.dropna(inplace=True)
    DF = age_filtered_df[["Mobile"]]
    # concat_df = pd.concat([concat_df, DF], ignore_index=True)
    # print(age_filtered_df)
    print(DF)
    print(file, len(DF))
    # print(age_filtered_df)
    DF.to_excel(f"/home/rajashekar/Desktop/Andhra_State_Daily_data/Machilipatnam/Machilipatnam_18_25/import_data2/{constituency}_18_25_Age_group.xlsx",index=False)
concat_df.drop_duplicates(subset=["Mobile"],inplace=True)
print(len(concat_df))
print(concat_df)

concat_df.to_excel("/home/rajashekar/Desktop/Andhra_State_Daily_data/Machilipatnam/Machilipatnam_18_25/import_data2/z_Concat_18_25_Age_group.xlsx",index=False)


