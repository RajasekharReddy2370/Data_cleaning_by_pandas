import os
import pandas as pd
# Define folder paths
folder_a = '/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary_Voter_Name_and_Mobile'  # Output files (already processed)
folder_b = '/home/rajashekar/Desktop/All_states_data/one_drive_data/Telangana_color_data_from_onedrive'  # Files to be processed

# Function to extract the prefix from filenames (before the first underscore or .xlsx)
def get_prefix(filename):
    # Check for underscore, then dash, then fall back to splitting by period
    if '_' in filename:
        return filename.split('_')[0]
    elif '-' in filename:
        return filename.split('-')[0]
    else:
        return filename.split('.')[0]

# Get the set of prefixes in folder A
prefixes_in_a = {get_prefix(f).strip() for f in os.listdir(folder_a) if f.endswith(".xlsx")}
print(f"Prefixes in Folder A: {len(prefixes_in_a)}")

# Get the dictionary of filenames in folder B (key: prefix, value: full filename)
files_in_b = {get_prefix(f).strip(): f for f in os.listdir(folder_b) if f.endswith(".xlsx") or f.endswith(".xls")}
print(f"Files in Folder B: {len(files_in_b)}")

# # Find files in B whose prefixes are not in A
files_to_process = [filename for prefix, filename in files_in_b.items() if prefix not in prefixes_in_a]
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
# # Output the files to process
if files_to_process:
    c=0
    print("Files in Folder B not in Folder A:")
    for file_name in files_to_process:
        c+=1
        df = pd.read_excel(folder_b + '/' + file_name, usecols=["First Name", "Last Name","Mobile"],  engine='openpyxl')
        print(file_name,c)
#         # df = pd.read_excel(folder_b + '/' + file_name, usecols=["Mobile"],  engine='openpyxl')
#
#         constituency = file_name.split('-')[0]
#
#         # Drop rows with missing mobile numbers
#         df.dropna(subset=['Mobile'], inplace=True)
#
#         # # Clean up names
#         df['Last Name'] = df['Last Name'].fillna('')
#         df['First Name'] = df['First Name'].astype(str).str.strip()
#         df['Last Name'] = df['Last Name'].astype(str).str.strip()
#         df['Names'] = (df['First Name'] + ' ' + df['Last Name']).str.title()
#
#         # Clean mobile numbers
#         df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
#         df['Mobile'] = df['Mobile'].astype(str)
#         df = df[df['Mobile'].str.isdigit()]
#
#         # Remove country code if present
#         df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
#
#         # Filter valid Indian mobile numbers
#         df['Mobile'] = df['Mobile'].apply(lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
#
#         # Remove duplicates
#         df.drop_duplicates(subset=["Names", "Mobile"], inplace=True)
#         # df.drop_duplicates(subset=["Mobile"], inplace=True)
#         df.dropna(subset=['Mobile'], inplace=True)
#
#         # Save constituency-level data
#         c = len(df)
#         print(f"{constituency} - Name and Mobile Count: {c}")
#         df = df[['Names', 'Mobile']]
#         # df = df[['Mobile']]
#         df.to_excel(
#             f"/home/rajashekar/Desktop/All_states_data/one_drive_data/marasta/{constituency}_Name_and_Mobile.xlsx",
#             index=False)
#         print(file_name,c)
# else:
#     print("No new files to process.")

# import os
#
# # Define folder path
# folder_path = '/home/rajashekar/Desktop/All_states_data/one_drive_data/Madhya Pradesh_color_data_from_onedrive'  # Replace with your folder path
#
# # List all files in the folder except those that end with .xlsx
# files_to_process = [f for f in os.listdir(folder_path) if not f.endswith('.xlsx')]
#
# # Print the filenames that are not .xlsx
# if files_to_process:
#     print("Files not ending with .xlsx:")
#     for file_name in files_to_process:
#         print(file_name)
# else:
#     print("All files are .xlsx.")

