# import pandas as pd
# import os
# import time
#
# start_time = time.time()
# # Define the main folder path
# main_folder_path = r"/home/rajashekar/Desktop/All_states_data/one_drive_data/Maharastra_color_data_from_onedrive"
# files = os.listdir(main_folder_path)
#
# # Initialize DataFrames
# concat_df_Name_mobile = pd.DataFrame()
# concat_df_mobile = pd.DataFrame()
#
# # Initialize dictionaries to store lengths
# constituency_lengths_Name_Mobile = {}
# constituency_lengths = {}
#
# # Initialize state counter
# state_Number = 0
#
# # Define the function to clean mobile numbers
# def clean_mobile_number(mobile):
#     try:
#         mobile_float = float(mobile)
#         mobile = "{:.0f}".format(mobile_float)
#     except ValueError:
#         mobile = str(mobile)
#
#     if mobile.endswith(".0"):
#         mobile = mobile[:-2]
#
#     return mobile
#
# # Process each file in the folder
# for file in files:
#     # print(file)
#     state_Number += 1
#     # print(state_Number)
#     df = pd.read_excel(main_folder_path + '/' + file, usecols=["First Name", "Last Name", "Mobile"],engine='openpyxl')
#     print(file,state_Number)
#     constituency = file.split('-')[0]
#
#     # Drop rows with missing mobile numbers
#     df.dropna(subset=['Mobile'], inplace=True)
#
#     # Clean up names
#     df['Last Name'] = df['Last Name'].fillna('')
#     df['First Name'] = df['First Name'].astype(str).str.strip()
#     df['Last Name'] = df['Last Name'].astype(str).str.strip()
#     df['Names'] = (df['First Name'] + ' ' + df['Last Name']).str.title()
#
#     # Clean mobile numbers
#     df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
#     df['Mobile'] = df['Mobile'].astype(str)
#     df = df[df['Mobile'].str.isdigit()]
#
#     # Remove country code if present
#     df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
#
#     # Filter valid Indian mobile numbers
#     df['Mobile'] = df['Mobile'].apply(lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
#
#     # Remove duplicates
#     df.drop_duplicates(subset=["Names", "Mobile"], inplace=True)
#     df.dropna(subset=['Mobile'], inplace=True)
#
#     # Save constituency-level data
#     c = len(df)
#     print(f"{constituency} - Name and Mobile Count: {c}")
#     df = df[['Names','Mobile']]
#     df.to_excel(f"/home/rajashekar/Desktop/All_states_data/Name_and_Mobile_Number/Maharastra/{constituency}_Names_and_Mobile.xlsx", index=False)
#
#     # Concatenate data for overall state
#     concat_df_Name_mobile = pd.concat([concat_df_Name_mobile, df], ignore_index=True)
#
#     # Prepare mobile-only DataFrame and save
#     # df_mobile = df[["Mobile"]].drop_duplicates()
#     # C = len(df_mobile)
#     # df_mobile.to_excel(f"/home/rajashekar/Desktop/All_states_data/Mobile_Number/Maharastra/{constituency}_Mobile.xlsx", index=False)
#     # concat_df_mobile = pd.concat([concat_df_mobile, df_mobile], ignore_index=True)
#
#     # print(f"{constituency} - Mobile Count: {C}")
#
#     # Store lengths in dictionaries
#     constituency_lengths_Name_Mobile[constituency] = c
#     # constituency_lengths[constituency] = C
#     print(f"Processed file {state_Number}/{len(files)}: {file}")
#
# # Save constituency lengths
# constituency_df_n_m = pd.DataFrame(list(constituency_lengths_Name_Mobile.items()), columns=['Constituency', 'Length'])
# # constituency_df = pd.DataFrame(list(constituency_lengths.items()), columns=['Constituency', 'Length'])
#
# constituency_df_n_m.to_excel('/home/rajashekar/Desktop/All_states_data/State_constituency_lengths/Name_and_Mobile/Maharastra_constituency_lengths_Name_and_Mobile.xlsx', index=False)
# # constituency_df.to_excel('/home/rajashekar/Desktop/All_states_data/State_constituency_lengths/Mobile/Maharastra_constituency_lengths_Mobile.xlsx', index=False)
#
# # Print overall statistics before removing duplicates
# print("Overall State WITH DUPLICATES - Name and Mobile:", len(concat_df_Name_mobile))
# # print("Overall State WITH DUPLICATES - Mobile:", len(concat_df_mobile))
#
# # Remove duplicates from concatenated DataFrames
# concat_df_Name_mobile.drop_duplicates(subset=["Names", "Mobile"], inplace=True)
# # concat_df_mobile.drop_duplicates(subset=["Mobile"], inplace=True)
#
# # Print overall statistics after removing duplicates
# print("Overall State WITHOUT DUPLICATES - Name and Mobile:", len(concat_df_Name_mobile))
# # print("Overall State WITHOUT DUPLICATES - Mobile:", len(concat_df_mobile))
#
# # # Save the overall concatenated data
# # concat_df_Name_mobile.to_excel("/home/rajashekar/Desktop/All_states_data/Overall_Name_and_Mobile_Andhra_Pradesh.xlsx", index=False)
# # concat_df_mobile.to_excel("/home/rajashekar/Desktop/All_states_data/Overall_Mobile_Andhra_Pradesh.xlsx", index=False)
#
# end_time = time.time()
# print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTt",end_time-start_time)
# print("Data processing completed successfully.")

#####################################################################################################################################################################
import pandas as pd
import os
import time
from openpyxl import load_workbook

start_time = time.time()
# Define the main folder path
main_folder_path = r"/home/rajashekar/Desktop/All_states_data/one_drive_data/Maharastra_color_data_from_onedrive"
files = os.listdir(main_folder_path)

# Initialize DataFrames
concat_df_Name_mobile = pd.DataFrame()
# concat_df_mobile = pd.DataFrame()

# Initialize dictionaries to store lengths
constituency_lengths_Name_Mobile = {}
# constituency_lengths = {}

# Initialize state counter
state_Number = 0

# List to keep track of problematic files
error_files = []

# Define the function to clean mobile numbers
def clean_mobile_number(mobile):
    try:
        mobile_float = float(mobile)
        mobile = "{:.0f}".format(mobile_float)
    except ValueError:
        mobile = str(mobile)

    if mobile.endswith(".0"):
        mobile = mobile[:-2]

    return mobile

# Process each file in the folder
for file in files:
    file_path = os.path.join(main_folder_path, file)
    state_Number += 1

    # Skip non-Excel files
    if not file.lower().endswith(('.xls', '.xlsx')):
        print(f"Skipping non-Excel file: {file}")
        continue

    # Check if the file is a valid Excel file using openpyxl
    try:
        load_workbook(file_path)
    except Exception as e:
        error_files.append(file)
        print(f"File validation failed for {file}: {e}")
        continue

    try:
        df = pd.read_excel(file_path, usecols=["First Name", "Last Name", "Mobile"], engine='openpyxl')
        print(file, state_Number)
    except Exception as e:
        error_files.append(file)
        print(f"Error reading file {file}: {e}")
        continue

    constituency = file.split('-')[0]

    # Drop rows with missing mobile numbers
    df.dropna(subset=['Mobile'], inplace=True)

    # Clean up names
    df['Last Name'] = df['Last Name'].fillna('')
    df['First Name'] = df['First Name'].astype(str).str.strip()
    df['Last Name'] = df['Last Name'].astype(str).str.strip()
    df['Names'] = (df['First Name'] + ' ' + df['Last Name']).str.title()

    # Clean mobile numbers
    df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
    df['Mobile'] = df['Mobile'].astype(str)
    df = df[df['Mobile'].str.isdigit()]

    # Remove country code if present
    df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)

    # Filter valid Indian mobile numbers
    df['Mobile'] = df['Mobile'].apply(lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)

    # Remove duplicates
    df.drop_duplicates(subset=["Names", "Mobile"], inplace=True)
    df.dropna(subset=['Mobile'], inplace=True)

    # Save constituency-level data
    c = len(df)
    print(f"{constituency} - Name and Mobile Count: {c}")
    df = df[['Names', 'Mobile']]
    df.to_excel(f"/home/rajashekar/Desktop/All_states_data/Name_and_Mobile_Number/Maharastra/{constituency}_Names_and_Mobile.xlsx", index=False)

    # Concatenate data for overall state
    concat_df_Name_mobile = pd.concat([concat_df_Name_mobile, df], ignore_index=True)

    # Store lengths in dictionaries
    constituency_lengths_Name_Mobile[constituency] = c
    print(f"Processed file {state_Number}/{len(files)}: {file}")

# Save constituency lengths
constituency_df_n_m = pd.DataFrame(list(constituency_lengths_Name_Mobile.items()), columns=['Constituency', 'Length'])
constituency_df_n_m.to_excel('/home/rajashekar/Desktop/All_states_data/State_constituency_lengths/Name_and_Mobile/Maharastra_constituency_lengths_Name_and_Mobile.xlsx', index=False)

# Print overall statistics before removing duplicates
print("Overall State WITH DUPLICATES - Name and Mobile:", len(concat_df_Name_mobile))

# Remove duplicates from concatenated DataFrame
concat_df_Name_mobile.drop_duplicates(subset=["Names", "Mobile"], inplace=True)

# Print overall statistics after removing duplicates
print("Overall State WITHOUT DUPLICATES - Name and Mobile:", len(concat_df_Name_mobile))

# Save the overall concatenated data
# concat_df_Name_mobile.to_excel("/home/rajashekar/Desktop/All_states_data/Overall_Name_and_Mobile_Maharastra.xlsx", index=False)

# Log any problematic files
if error_files:
    print("Files that caused errors:", error_files)
    with open("/home/rajashekar/Desktop/All_states_data/Error_Files_Log.txt", "w") as log_file:
        for error_file in error_files:
            log_file.write(f"{error_file}\n")

end_time = time.time()
print(f"Total processing time: {end_time - start_time:.2f} seconds")
print("Data processing completed successfully.")

