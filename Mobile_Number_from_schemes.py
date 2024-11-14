import os
import pandas as pd
import re

# Define file path and list of mobile number columns
file_path = r"/home/rajashekar/Desktop/RAJA_LAPTOP/Telangana/TELANGANA/TELANGANA_MOBILE_NUMBERS_from_Drive_data_and_schemes/Beneficiary_Data_All_schemes"
PhoneNumbers = ['Mobile Number', 'Contact_Number', 'Contact Number', 'CONTACT_NO', 'Mobile NO',
                'Phone Number', 'MOBILE_NUMBER', 'MOBILE', 'Phone number', 'Mobile No.', 'Mobile']

# List all folders in the directory
all_folders = os.listdir(file_path)

# Dictionary to store constituency lengths
constituency_lengths_Mobile = {}
c = 0
# Iterate through each folder
for folder in all_folders:
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",folder)
    if folder != 'Ts':  # Change folder name based on your need
        constituency_name = folder.split('_')[0]
        all_files_in_folder = os.listdir(os.path.join(file_path, folder))

        result_df = pd.DataFrame()

        # Process each file in the folder
        for file in all_files_in_folder:
            # print('Processing file:', file)
            file_path_full = os.path.join(file_path, folder, file)
            try:
                if file.endswith('.xlsx'):
                    # Try multiple headers to find the correct one
                    for header_index in range(4):
                        df = pd.read_excel(file_path_full, header=header_index)
                        selected_columns = [col for col in df.columns if col.strip().lower() in [col.strip().lower() for col in PhoneNumbers]]
                        if selected_columns:
                            filtered_df = df[selected_columns].copy()
                            column_mapping = {col: 'Mobile' for col in selected_columns}
                            filtered_df.rename(columns=column_mapping, inplace=True)
                            result_df = pd.concat([result_df, filtered_df], axis=0, ignore_index=True)
                            # break

                elif file.endswith('.csv'):
                    df = pd.read_csv(file_path_full,low_memory=False)
                    selected_columns = [col for col in df.columns if col.strip().lower() in [col.strip().lower() for col in PhoneNumbers]]
                    if selected_columns:
                        filtered_df = df[selected_columns].copy()
                        column_mapping = {col: 'Mobile' for col in selected_columns}
                        filtered_df.rename(columns=column_mapping, inplace=True)
                        result_df = pd.concat([result_df, filtered_df], axis=0, ignore_index=True)

            except Exception as e:
                print(f"Exception while processing {file}: {e}")

        # Function to clean and format mobile numbers
        def clean_mobile_number(mobile):
            try:
                mobile_float = float(mobile)
                mobile = "{:.0f}".format(mobile_float)
            except ValueError:
                mobile = str(mobile)

            if mobile.endswith(".0"):
                mobile = mobile[:-2]

            return mobile

        # Clean and filter mobile numbers
        if not result_df.empty and 'Mobile' in result_df.columns:
            result_df['Mobile'] = result_df['Mobile'].apply(clean_mobile_number)
            result_df['Mobile'] = result_df['Mobile'].astype(str)
            result_df = result_df[result_df['Mobile'].str.isdigit()]
            result_df['Mobile'] = result_df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
            result_df['Mobile'] = result_df['Mobile'].apply(lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)

            # Remove invalid and duplicate mobile numbers
            result_df.dropna(subset=['Mobile'], inplace=True)
            result_df.drop_duplicates(subset=['Mobile'], inplace=True)

            print(f"Total valid mobile numbers in {constituency_name}: {len(result_df)}")

            # Save the resulting dataframe to an Excel file
            output_path = f"/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/Mobile/{constituency_name}.xlsx"
            result_df.to_excel(output_path, index=False)
            print(f"Mobile numbers extracted and saved successfully for {constituency_name}.")
            c +=1
            print("#######################################################################################",c)

            # Update the constituency lengths dictionary
            constituency_lengths_Mobile[constituency_name] = len(result_df)

# Save the constituency lengths to an Excel file
if constituency_lengths_Mobile:
    constituency_Mobile_df = pd.DataFrame(list(constituency_lengths_Mobile.items()), columns=['Constituency', 'Length'])
    output_length_path = f"/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/constituency_lengths/Mobile/Telangana_Beneficiary_Mobile_constituency_lengths.xlsx"
    constituency_Mobile_df.to_excel(output_length_path, index=False)
    print("Constituency lengths saved successfully.")

# List all processed folders
# print("Processed folders:")
# for folder in all_folders:
#     print(folder)






######################################################################################################################################################

# import os
# import pandas as pd
# import re
#
# # Define file path and list of mobile number columns
# file_path = r"/home/rajashekar/Desktop/RAJA_LAPTOP/Telangana/TELANGANA/TELANGANA_MOBILE_NUMBERS_from_Drive_data_and_schemes/Beneficiary_Data_All_schemes"
# PhoneNumbers = ['Mobile Number', 'Contact_Number', 'Contact Number', 'CONTACT_NO', 'Mobile NO',
#                 'Phone Number', 'MOBILE_NUMBER', 'MOBILE', 'Phone number', 'Mobile No.','Mobile']
#
# # List all folders in the directory
# all_folders = os.listdir(file_path)
#
#
# for folder in all_folders:
#     constituency_lengths_Mobile = {}
#
#     if folder != 'Ts':  # Change folder name based on your need
#         # constituency_name = folder
#         constituency_name = folder.split('_')[0]
#
#         all_files_in_folder = os.listdir(file_path + '/' + folder)
#
#         result_df = pd.DataFrame()
#
#         # Process each file in the folder
#         for file in all_files_in_folder:
#             print('Processing file:', file)
#             try:
#                 if file.endswith('.xlsx'):
#                     for i in range(0, 4):  # Try multiple headers
#                         df = pd.read_excel(file_path + '/' + folder + '/' + file, header=i)
#                         selected_columns = [col for col in df.columns if col in PhoneNumbers]
#                         filtered_df = df[selected_columns].copy()
#
#                         # Rename mobile columns for consistency
#                         column_mapping = {col: 'Mobile' for col in PhoneNumbers}
#                         filtered_df.rename(columns=column_mapping, inplace=True)
#
#                         if 'Mobile' in filtered_df.columns:
#                             result_df = pd.concat([result_df, filtered_df], axis=0, ignore_index=True)
#                         break  # If successful, exit the loop
#
#                 elif file.endswith('.csv'):
#                     df = pd.read_csv(file_path + '/' + folder + '/' + file)
#                     selected_columns = [col for col in df.columns if col in PhoneNumbers]
#                     filtered_df = df[selected_columns].copy()
#
#                     # Rename mobile columns for consistency
#                     column_mapping = {col: 'Mobile' for col in PhoneNumbers}
#                     filtered_df.rename(columns=column_mapping, inplace=True)
#
#                     if 'Mobile' in filtered_df.columns:
#                         result_df = pd.concat([result_df, filtered_df], axis=0, ignore_index=True)
#
#             except Exception as e:
#                 print(f"Exception while processing {file}: {e}")
#
#         # Function to clean and format mobile numbers
#         def clean_mobile_number(mobile):
#             try:
#                 mobile_float = float(mobile)
#                 mobile = "{:.0f}".format(mobile_float)  # Remove decimals
#             except ValueError:
#                 mobile = str(mobile)
#
#             if mobile.endswith(".0"):
#                 mobile = mobile[:-2]  # Remove trailing ".0"
#
#             return mobile
#
#         result_df['Mobile'] = result_df['Mobile'].apply(clean_mobile_number)
#
#         # Ensure mobile numbers are strings and filter valid ones
#         result_df['Mobile'] = result_df['Mobile'].astype(str)
#         result_df = result_df[result_df['Mobile'].str.isdigit()]  # Keep only numeric strings
#         result_df['Mobile'] = result_df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
#         result_df['Mobile'] = result_df['Mobile'].apply(lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
#
#         # Remove rows where mobile is None (invalid numbers)
#         result_df.dropna(subset=['Mobile'], inplace=True)
#
#         # Remove duplicate mobile numbers
#         result_df.drop_duplicates(subset=['Mobile'], inplace=True)
#
#         print("Total valid mobile numbers:", len(result_df))
#
#         # Save the resulting dataframe to an Excel file
#         result_df.to_excel(f"/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/Mobile/{constituency_name}.xlsx", index=False)
#         print("Mobile numbers extracted and saved successfully.")
#         constituency_lengths_Mobile[constituency_name] = len(result_df)
#
# constituency_Mobile = pd.DataFrame(list(constituency_lengths_Mobile.items()), columns=['Constituency', 'Length'])
# constituency_Mobile.to_excel(f"/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/constituency_lengths/Mobile/Telangana_Beneficiary_Mobile_constituency_lengths.xlsx",index = False)
#
# # List all processed folders
# for i in all_folders:
#     print(i)


