import pandas as pd
import os
import time

start_time = time.time()
# Define the main folder path
main_folder_path = r"/home/rajashekar/Desktop/All_states_data/one_drive_data/Madhya Pradesh_color_data_from_onedrive"
files = os.listdir(main_folder_path)

# Initialize DataFrames
# concat_df_Name_mobile = pd.DataFrame()
concat_df_mobile = pd.DataFrame()

# Initialize dictionaries to store lengths
# constituency_lengths_Name_Mobile = {}
constituency_lengths_mobile = {}

# Initialize state counter
state_Number = 0

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
    state_Number += 1
    df = pd.read_excel(main_folder_path + '/' + file, usecols=["Mobile"],engine='openpyxl')
    constituency = file.split('-')[0]
    print("*****************************888",constituency,state_Number)

#     # Drop rows with missing mobile numbers
    df.dropna(subset=['Mobile'], inplace=True)
#
#     # Clean up names
#     df['Last Name'] = df['Last Name'].fillna('')
#     df['First Name'] = df['First Name'].astype(str).str.strip()
#     df['Last Name'] = df['Last Name'].astype(str).str.strip()
#     df['Names'] = (df['First Name'] + ' ' + df['Last Name']).str.title()
#
    # Clean mobile numbers
    df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
    df['Mobile'] = df['Mobile'].astype(str)
    df = df[df['Mobile'].str.isdigit()]

    # Remove country code if present
    df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)

    # Filter valid Indian mobile numbers
    df['Mobile'] = df['Mobile'].apply(lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)

    # Remove duplicates
    # df.drop_duplicates(subset=["Names", "Mobile"], inplace=True)
    df.dropna(subset=['Mobile'], inplace=True)
#
#     # Save constituency-level data
#     c = len(df)
#     print(f"{constituency} - Name and Mobile Count: {c}")
#     df = df[['Names','Mobile']]
#     df.to_excel(f"/home/rajashekar/Desktop/All_states_data/Name_and_Mobile_Number/Madhya_Pradesh/{constituency}_Names_and_Mobile.xlsx", index=False)
#
#     # Concatenate data for overall state
#     concat_df_Name_mobile = pd.concat([concat_df_Name_mobile, df], ignore_index=True)
#
#     # Prepare mobile-only DataFrame and save
    df_mobile = df[["Mobile"]].drop_duplicates()
    C = len(df_mobile)
    df_mobile.to_excel(f"/home/rajashekar/Desktop/All_states_data/Mobile_Number/Madhya_Pradesh/{constituency}_Mobile.xlsx", index=False)
    concat_df_mobile = pd.concat([concat_df_mobile, df_mobile], ignore_index=True)
#
    print(f"{constituency} - Mobile Count: {C}")
#
#     # Store lengths in dictionaries
#     constituency_lengths_Name_Mobile[constituency] = c
    constituency_lengths_mobile[constituency] = C
#     print(f"Processed file {state_Number}/{len(files)}: {file}")
#
# # Save constituency lengths
# constituency_df_n_m = pd.DataFrame(list(constituency_lengths_Name_Mobile.items()), columns=['Constituency', 'Length'])
constituency_df = pd.DataFrame(list(constituency_lengths_mobile.items()), columns=['Constituency', 'Length'])
#
# constituency_df_n_m.to_excel('/home/rajashekar/Desktop/All_states_data/State_constituency_lengths/Name_and_Mobile/Madhya_Pradesh_constituency_lengths_Name_and_Mobile.xlsx', index=False)
constituency_df.to_excel('/home/rajashekar/Desktop/All_states_data/State_constituency_lengths/Mobile/Madhya_Pradesh_constituency_lengths_Mobile.xlsx', index=False)
#
# # Print overall statistics before removing duplicates
# print("Overall State WITH DUPLICATES - Name and Mobile:", len(concat_df_Name_mobile))
# print("Overall State WITH DUPLICATES - Mobile:", len(concat_df_mobile))
#
# # Remove duplicates from concatenated DataFrames
# concat_df_Name_mobile.drop_duplicates(subset=["Names", "Mobile"], inplace=True)
concat_df_mobile.drop_duplicates(subset=["Mobile"], inplace=True)
#
# # Print overall statistics after removing duplicates
# print("Overall State WITHOUT DUPLICATES - Name and Mobile:", len(concat_df_Name_mobile))
print("Overall State WITHOUT DUPLICATES - Mobile:", len(concat_df_mobile))
#
# # # Save the overall concatenated data
# # concat_df_Name_mobile.to_excel("/home/rajashekar/Desktop/All_states_data/Overall_Name_and_Mobile_Andhra_Pradesh.xlsx", index=False)
# # concat_df_mobile.to_excel("/home/rajashekar/Desktop/All_states_data/Overall_Mobile_Andhra_Pradesh.xlsx", index=False)
#
# end_time = time.time()
# print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTt",end_time-start_time)
# print("Data processing completed successfully.")

#############################################################################################################################

# import pandas as pd
# import os
#
# main_folder_path = r"/home/rajashekar/Desktop/All_states_data/one_drive_data/Andhra Pradesh_color_data_from_one_drive"
# files = os.listdir(main_folder_path)
#
# concat_df_Name_mobile = pd.DataFrame()
# concat_df_mobile = pd.DataFrame()
#
# constituency_lengths_Name_Mobile = {}
# constituency_lengths = {}
#
#
# # name = "Andhra_Mobile_Numbers"
# state_Number = 0
# for file in files:
#     state_Number = state_Number+1
#     # df = pd.read_excel(main_folder_path + '/' + file, usecols=['Age', "Mobile"])
#     df = pd.read_excel(main_folder_path + '/' + file, usecols=["First Name","Last Name","Mobile"])
#     # print(file)
#     constituency = file.split('-')[0]
#
#     # df = df[(df['Age'] >= 18) & (df['Age'] <= 40)].copy()
#     # df.dropna(subset=['Age'], inplace=True)
#     df.dropna(subset=['Mobile'], inplace=True)
#
#     df['Last Name'] = df['Last Name'].fillna('')
#     df['First Name'] = df['First Name'].astype(str)
#     df['Last Name'] = df['Last Name'].astype(str)
#     df['First Name'] = df['First Name'].str.strip()
#     df['Last Name'] = df['Last Name'].str.strip()
#     df['Names'] = df['First Name'] + ' ' + df['Last Name']
#     df["Names"] = df["Names"].str.title()
#
#
#     def clean_mobile_number(mobile):
#         try:
#             mobile_float = float(mobile)
#             mobile = "{:.0f}".format(mobile_float)
#         except ValueError:
#             mobile = str(mobile)
#
#         if mobile.endswith(".0"):
#             mobile = mobile[:-2]
#
#         return mobile
#
#
#     df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
#     df['Mobile'] = df['Mobile'].astype(str)
#     df = df[df['Mobile'].str.isdigit()]
#     df['Mobile'] = df['Mobile'].apply(
#         lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
#     df['Mobile'] = df['Mobile'].apply(
#         lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
#
#     df.drop_duplicates(subset=["Names","Mobile"], inplace=True)
#     df.dropna(inplace=True)
#     c = len(df)
#     print(constituency, "--------------------Name_and_Mobile-----------------------------------", c)
#
#     df.to_excel(f"/home/rajashekar/Desktop/All_states_data/Name_and_Mobile_Number/Andhra_Pradesh/{constituency}_Names_and_Mobile.xlsx",index = False)
#     concat_df_Name_mobile = pd.concat([concat_df_Name_mobile,df],ignore_index=True)
#     DF = df[["Mobile"]]
#     df.drop_duplicates(subset=["Mobile"], inplace=True)
#     C = len(DF)
#     DF.to_excel(f"/home/rajashekar/Desktop/All_states_data/Mobile_Number/Andhra_Pradesh/{constituency}_Mobile.xlsx",index = False)
#     concat_df_mobile = pd.concat([concat_df_mobile, DF], ignore_index=True)
#     print(constituency, "----------------------------Mobile--------------------------------------", C)
#
#     constituency_lengths_Name_Mobile[constituency] = len(df)
#     constituency_lengths[constituency] = len(DF)
#     print("############################################################################## state_Number",state_Number)
#
# constituency_df_n_m = pd.DataFrame(list(constituency_lengths_Name_Mobile.items()), columns=['Constituency', 'Length'])
# constituency_df = pd.DataFrame(list(constituency_lengths.items()), columns=['Constituency', 'Length'])
# constituency_df_n_m.to_excel('/home/rajashekar/Desktop/All_states_data/State_constituency_lengths/Name_and_Mobile/Andhra_pradesh_constituency_lengths_Name_and_Mobile.xlsx', index=False)
# constituency_df.to_excel('/home/rajashekar/Desktop/All_states_data/State_constituency_lengths/Mobile/Andhra_pradesh_constituency_lengths_Mobile.xlsx', index=False)
#
# print("Overall State WITH DUPLICATES-----------------------------------------------",len(concat_df_Name_mobile))
# print("Overall State WITH DUPLICATES-----------------------------------------------",len(concat_df_mobile))
# #
# concat_df_Name_mobile.drop_duplicates(subset=["Names","Mobile"],inplace=True)
# concat_df_mobile.drop_duplicates(subset=["Mobile"],inplace=True)
# print("Overall State WITH out DUPLICATES-----------------------------------------------",len(concat_df_Name_mobile))
# print("Overall State WITH out DUPLICATES-----------------------------------------------",len(concat_df_mobile))
# # print(concat_df_mobile)
# # print(concat_df_mobile)
#
# l_n_m = len(concat_df_Name_mobile)
# l = len(concat_df_mobile)
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Name_and_Mobile",l_n_m)
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@_Mobile",l)
# # if l > 1000000:
# #     first_part = concat_df.iloc[:1000000, :]
# #     second_part = concat_df.iloc[1000000:2000000, :]
# #     third_part = concat_df.iloc[2000000:3000000, :]
# #     fourth_part = concat_df.iloc[3000000:, :]
# #
# #     first_file_path = f"{name}_1st_part.xlsx"
# #     first_part.to_excel(first_file_path, index=False)
# #
# #     print("............................................first_part")
# #
# #     second_file_path = f"{name}_2nd_part.xlsx"
# #     second_part.to_excel(second_file_path, index=False)
# #     print("............................................second_part")
# #
# #     third_file_path = f"{name}_3rd_part.xlsx"
# #     third_part.to_excel(third_file_path, index=False)
# #
# #     print("............................................third_part")
# #
# #     fourth_file_path = f"{name}_4th_part.xlsx"
# #     fourth_part.to_excel(fourth_file_path, index=False)
# #
# #     print("............................................four_part")
# # else:
# #     file_path = f"{name}.xlsx"
# #     concat_df.to_excel(file_path, index=False)
# #     print("*******************************************original file stored successfully")
# # concat_df.to_excel('Telangana_18_30_Age_group_Mobile_Numbers.xlsx',index = False)
#
# # file_count = (len(concat_df) // 1_000_000) + 1  # Calculate number of files needed
# # file_prefix = f"{name}"
# #
# # # Loop to save DataFrame parts
# # for i in range(file_count):
# #     start_idx = i * 1_000_000
# #     end_idx = (i + 1) * 1_000_000
# #     part_df = concat_df.iloc[start_idx:end_idx]
# #
# #     # Define the filename (e.g., 'name_1.xlsx', 'name_2.xlsx', etc.)
# #     file_path = f"{file_prefix}_part_{i + 1}.xlsx"
# #     part_df.to_excel(file_path, index=False)
# #     print(f"Part {i + 1} saved successfully: {file_path}")
# #
# # print("File(s) stored successfully.")
#
