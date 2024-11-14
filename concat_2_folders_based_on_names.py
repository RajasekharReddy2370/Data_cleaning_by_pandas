import os
import pandas as pd

# Define paths to the two folders
folder1 = "/home/rajashekar/Desktop/All_states_data/Name_and_Mobile_Number/tb"
folder2 = "/home/rajashekar/Desktop/All_states_data/Name_and_Mobile_Number/tv"
# output_folder = "/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary_Voter_Name_and_Mobile/"

# constituency_lengths_Name_Mobile = {}
# concat_df = pd.DataFrame()

# Ensure the output folder exists
# os.makedirs(output_folder, exist_ok=True)

# Function to extract the prefix from filenames (before the first underscore or .xlsx)
def get_prefix(filename):
    return filename.split('_')[0] if '_' in filename else filename.split('.')[0]

# Function to read Excel files
def read_excel(file_path):
    return pd.read_excel(file_path, usecols=["Names", "Mobile"])

# Get list of files in both folders
files1 = {get_prefix(f): f for f in os.listdir(folder1) if f.endswith(".xlsx")}
files2 = {get_prefix(f): f for f in os.listdir(folder2) if f.endswith(".xlsx")}
print(files1)
print(files2)
# Iterate over the prefixes found in folder1 and check for matching files in folder2

cout = 0
for prefix, file1 in files1.items():
    if prefix in files2:
        # Construct file paths
        file_path1 = os.path.join(folder1, file1)
        file_path2 = os.path.join(folder2, files2[prefix])

        # Read data from both files
        df1 = read_excel(file_path1)
        df2 = read_excel(file_path2)

        # Concatenate and remove duplicates based on 'Mobile' column
        combined_df = pd.concat([df1, df2], ignore_index=True).drop_duplicates(subset=["Names","Mobile"])

        # Save the combined data to a new Excel file
        output_file = f"/home/rajashekar/Desktop/All_states_data/Name_and_Mobile_Number/t/{prefix}.xlsx"
        combined_df.to_excel(output_file, index=False)
        C = len(combined_df)
        # concat_df = pd.concat([concat_df, combined_df], ignore_index=True)
        # constituency_lengths_Name_Mobile[prefix] = C
        cout += 1
        print(f"Combined file saved for prefix '{prefix}'",C,cout)
# constituency_df_n_m = pd.DataFrame(list(constituency_lengths_Name_Mobile.items()), columns=['Constituency', 'Length'])
# constituency_df_n_m.to_excel('/home/rajashekar/Desktop/All_states_data/State_constituency_lengths/Name_and_Mobile/Telangana_constituency_lengths_Name_and_Mobile.xlsx', index=False)
# df3 = pd.read_excel(r"/home/rajashekar/Desktop/All_states_data/Telangana/Voter/Names_Mobile/Bodhan_Names_and_Mobile.xlsx",usecols = ["Names","Mobile"])
# print("############################BODHAN",len(df3))
# concat_df.drop_duplicates(subset=["Names","Mobile"],inplace=True)
# df4 = pd.concat([df3,concat_df],ignore_index=True)
# df4.drop_duplicates(subset=["Names","Mobile"])

# print(len(df4))


