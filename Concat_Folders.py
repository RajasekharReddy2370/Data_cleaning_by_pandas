import os
import pandas as pd

# Specify the paths to the two folders
folder1_path = "/home/rajashekar/Desktop/AP_CPU/CONSTITUENCY_ORIGINAL/Machilipatnam"
folder2_path = "/home/rajashekar/Desktop/Andhra_State_Daily_data/Machilipatnam/Machilipatnam_imported_Data/constituencies_To_be_cleaned/Machalipatnam_imported_data_Names_Mobile"
MP_Constituency = folder1_path.split('/')[-1]

# Get the list of files in each folder
folder1_files = os.listdir(folder1_path)
folder2_files = os.listdir(folder2_path)

# Sort the file lists to ensure consistency in file order
folder1_files.sort()
folder2_files.sort()

# Initialize an empty list to store DataFrames
dfs = []

# Loop through the first seven files in each folder and concatenate them
for file1, file2 in zip(folder1_files[:7], folder2_files[:7]):
    print(file1,file2)
    file = file1.split('_')[0]
    # Read the first file from each folder into a DataFrame
    df1 = pd.read_excel(os.path.join(folder1_path, file1))
    df2 = pd.read_excel(os.path.join(folder2_path, file2))
    #
    df = pd.concat([df1,df2],ignore_index=True)
    # df.drop_duplicates(subset=["Mobile"],inplace=True)
    # df.dropna(subset=["Mobile"],inplace=True)
    # print(file,'----------------------',len(df))
    # df.to_excel(f"/home/rajashekar/Desktop/AP_CPU/CONSTITUENCY_UNIQUE/Machilipatnam_updated_constituency_wise/{file}_Constituency_Names_Mobile_Numbers.xlsx",index = False)
    # df.to_excel('M_T_M.xlsx',index=False)
    # Append the DataFrames to the list
    dfs.append(df)
# # print(dfs)
# # Concatenate the DataFrames
concatenated_df = pd.concat(dfs, ignore_index=True)
# # concatenated_df.drop_duplicates(subset = ["Mobile"],inplace = True)
#
concatenated_df.dropna(inplace=True)
concatenated_df.to_excel("M_T_M.xlsx",index=False)
# print(len(concatenated_df))

# l = len(concatenated_df)
#
# if l > 1000000:
#     first_part = concatenated_df.iloc[:1000000, :]
#     second_part = concatenated_df.iloc[1000001:, :]
#
#     first_file_path = f"/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/Beneficiary_Voter_Mp_Constituency/Nalgonda/{MP_Constituency}_MP_Mobile_Numbers_Part1.xlsx"
#     first_part.to_excel(first_file_path, index=False)
#
#     print("............................................first_part")
#
#     second_file_path = f"/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/Beneficiary_Voter_Mp_Constituency/Nalgonda/{MP_Constituency}_MP_Mobile_Numbers_Part2.xlsx"
#     second_part.to_excel(second_file_path, index=False)
#     print("............................................second_part")
# else:
#     file_path = f"/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/Beneficiary_Voter_Mp_Constituency/Nalgonda/{MP_Constituency}_MP_Mobile_Numbers.xlsx"
#     concatenated_df.to_excel(file_path, index=False)
#     print("File......................stored_Successfully")

# concatenated_df.to_excel(f"/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Machilipatnam_imported_Data/Machilipatnam_each_constituency_with_Duplicates/Machilipatnam_MP_Mobile_Numbers_with_Duplicates1.xlsx",index=False)

# Display or further process the concatenated DataFrame
