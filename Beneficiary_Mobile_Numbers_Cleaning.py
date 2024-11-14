import os
import pandas as pd
import re
import time

# Start time
start_time = time.time()

# File path
file_path = r"/home/rajashekar/Desktop/RAJA_LAPTOP/Telangana/TELANGANA/TELANGANA_MOBILE_NUMBERS_from_Drive_data_and_schemes/Beneficiary_Data_All_schemes"
all_folders = os.listdir(file_path)
constituency_lengths = {}
cdff = pd.DataFrame()
c = 0


def clean_mobile_number(mobile):
    try:
        mobile_float = float(mobile)
        mobile = "{:.0f}".format(mobile_float)
    except ValueError:
        mobile = str(mobile)

    if mobile.endswith(".0"):
        mobile = mobile[:-2]

    return mobile


for folder in all_folders:
    c += 1
    print(f"Processing folder: {folder} ({c}/{len(all_folders)})")

    # Skip unwanted folders (e.g., 'ts')
    if folder != 'ts':
        constituency_name = folder.split('_')[0]
        all_files_in_folder = os.listdir(os.path.join(file_path, folder))
        cdf = pd.DataFrame()

        # Process each file in the folder
        for file in all_files_in_folder:
            fil = file.split('.xlsx')[0]
            if file.endswith('.xlsx') and ('Bandhu' in file):
                try:
                    # Read the Excel file
                    df = pd.read_excel(file_path + '/' + folder + '/' + file)
                    # print(f"Columns in {file}: {df.columns}")  # Debugging: Check column names

                    # Check if 'Mobile' column exists
                    if 'Mobile' in df.columns:
                        df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
                        df['Mobile'] = df['Mobile'].astype('str')
                        df = df[df['Mobile'].str.isdigit()]
                        df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
                        df['Mobile'] = df['Mobile'].apply(
                            lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
                        df = df[df["Mobile"].notna()]  # Remove rows where Mobile is None
                        df["Mobile"] = df["Mobile"].astype(int)
                        df.drop_duplicates(subset=["Mobile"], inplace=True)
                        df = df[["Mobile"]]
                        cdf = pd.concat([cdf, df], ignore_index=True)
                    else:
                        # print(f"Column 'Mobile' not found in {file}")
                        continue
                except Exception as e:
                    print(f"Error processing file {file}: {e}")
                    continue

            elif file.endswith('.csv'):
                try:
                    df = pd.read_csv(file_path + '/' + folder + '/' + file, low_memory=False)

                    # Check if 'Mobile' column exists
                    if 'Mobile' in df.columns:
                        df.dropna(subset=["Mobile"], inplace=True)
                        df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
                        df['Mobile'] = df['Mobile'].astype('str')
                        df = df[df['Mobile'].str.isdigit()]
                        df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
                        df['Mobile'] = df['Mobile'].apply(
                            lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
                        df = df[df["Mobile"].notna()]  # Remove rows where Mobile is None
                        df["Mobile"] = df["Mobile"].astype(int)
                        df.drop_duplicates(subset=["Mobile"], inplace=True)
                        df = df[["Mobile"]]
                        cdf = pd.concat([cdf, df], ignore_index=True)
                    else:
                        # print(f"Column 'Mobile' not found in {file}")
                        continue
                except Exception as e:
                    print(f"Error processing CSV file {file}: {e}")
                    continue

        # Save cleaned mobile numbers for the constituency
        cdf.drop_duplicates(subset=['Mobile'], inplace=True)
        output_path = f"/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/Mobile/{constituency_name}.xlsx"
        cdf.to_excel(output_path, index=False)
        cdff = pd.concat([cdff, cdf], ignore_index=True)

        # Update constituency lengths
        l = len(cdf)
        print(f"Processed constituency: {constituency_name}, Total mobile numbers: {l}")
        constituency_lengths[constituency_name] = l

# Save the summary of mobile numbers for each constituency
lengths_df = pd.DataFrame(list(constituency_lengths.items()), columns=['Constituency', 'Length'])
lengths_output_path = "/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/constituency_lengths/Mobile/Telangana_Beneficiary_Mobile_constituency_lengths.xlsx"
lengths_df.to_excel(lengths_output_path, index=False)

# Remove duplicates from the overall DataFrame
cdff.drop_duplicates(subset=["Mobile"], inplace=True)
print(f"Total unique mobile numbers across all constituencies: {len(cdff)}")

# Print total time taken
end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")

######################################################################################################################################

# import os
# import pandas as pd
# import re
# import time
#
# # Start time
# start_time = time.time()
#
# # File path
# file_path = r"/home/rajashekar/Desktop/RAJA_LAPTOP/Telangana/TELANGANA/TELANGANA_MOBILE_NUMBERS_from_Drive_data_and_schemes/Beneficiary_Data_All_schemes"
# all_folders = os.listdir(file_path)
# constituency_lengths = {}
# cdff = pd.DataFrame()
# c = 0
# for folder in all_folders:
#     c += 1
#     print(f"Processing folder: {folder} ({c}/{len(all_folders)})")
#
#
#     # Skip unwanted folders (e.g., 'ts')
#     if folder != 'ts':
#         # continue
#
#         constituency_name = folder.split('_')[0]
#         all_files_in_folder = os.listdir(os.path.join(file_path, folder))
#         cdf = pd.DataFrame()
#
#         # Process each file in the folder
#         for file in all_files_in_folder:
#             fil = file.split('.xlsx')[0]
#             # print('file','-----------------------',file)
#             if file.endswith('.xlsx') and ('Bandhu' in file):
#                 df = pd.read_excel(file_path + '/' + folder + '/' + file,usecols=["Mobile"])
#
#                 def clean_mobile_number(mobile):
#                     try:
#                         mobile_float = float(mobile)
#                         mobile = "{:.0f}".format(mobile_float)
#                     except ValueError:
#                         mobile = str(mobile)
#
#                     if mobile.endswith(".0"):
#                         mobile = mobile[:-2]
#
#                     return mobile
#
#                 # Assuming df is your DataFrame
#                 df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
#
#                 df['Mobile'] = df['Mobile'].astype('str')
#                 df = df[df['Mobile'].str.isdigit()]
#                 df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
#                 df['Mobile'] = df['Mobile'].apply(
#                     lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
#                 df = df[df["Mobile"].notna()]  # Remove rows where Mobile is None
#                 df["Mobile"] = df["Mobile"].astype(int)
#                 df.drop_duplicates(subset=["Mobile"],inplace=True)
#                 df = df[["Mobile"]]
#                 cdf = pd.concat([cdf,df],ignore_index=True)
#
#             elif file.endswith('.csv'):
#                 df = pd.read_csv(file_path + '/' + folder + '/' + file,low_memory=False)
#
#                 if 'Mobile' in df.columns:
#                     df.dropna(subset=["Mobile"], inplace=True)
#
#                     def clean_mobile_number(mobile):
#                         try:
#                             mobile_float = float(mobile)
#                             mobile = "{:.0f}".format(mobile_float)
#                         except ValueError:
#                             mobile = str(mobile)
#
#                         if mobile.endswith(".0"):
#                             mobile = mobile[:-2]
#
#                         return mobile
#
#                     # Assuming df is your DataFrame
#                     df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
#
#                     df['Mobile'] = df['Mobile'].astype('str')
#                     df = df[df['Mobile'].str.isdigit()]
#                     df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
#                     df['Mobile'] = df['Mobile'].apply(
#                         lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
#                     df = df[df["Mobile"].notna()]  # Remove rows where Mobile is None
#
#                     df["Mobile"] = df["Mobile"].astype(int)
#                     df.drop_duplicates(subset=["Mobile"], inplace=True)
#                     df = df[["Mobile"]]
#                     cdf = pd.concat([cdf,df],ignore_index=True)
#                 else :
#                     pass
#
#     # Save cleaned mobile numbers for the constituency
#         cdf.drop_duplicates(subset=['Mobile'], inplace=True)
#         output_path = f"/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/Mobile/{constituency_name}.xlsx"
#         cdf.to_excel(output_path, index=False)
#         cdff = pd.concat([cdff,cdf],ignore_index=True)
#     # Update constituency lengths
#         l = len(cdf)
#         print(f"Processed constituency: {constituency_name}, Total mobile numbers: {l}")
#         constituency_lengths[constituency_name] = l
#
# # Save the summary of mobile numbers for each constituency
# lengths_df = pd.DataFrame(list(constituency_lengths.items()), columns=['Constituency', 'Length'])
# lengths_output_path = "/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/constituency_lengths/Mobile/Telangana_Beneficiary_Mobile_constituency_lengths.xlsx"
# lengths_df.to_excel(lengths_output_path, index=False)
# cdff.drop_duplicates(subset=["Mobile"],inplace = True)
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@cdff",len(cdff))
#
# # Print total time taken
# end_time = time.time()
# print(f"Total time taken: {end_time - start_time:.2f} seconds")
