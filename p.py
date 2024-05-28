import os
# from indic_transliteration import sanscript
import pandas as pd
import re
# file_path = r"/home/rajashekar/Desktop/TS_CPU/BENEFICIARY_DATA_schemes/Malkajgiri"
# # possible_column_names = ['mobile','contact','phone']
# all_folders = os.listdir(file_path)
# beneficiary_names = ['Name of the Beneficiary', 'Beneficiary Name', 'PT_NAME', 'Name', 'BENEFICIARY_NAME','NAME_IN_AADHAR', 'Farmer Name',
#                      'Name of the Beneficiary(Nominee of Deceased Farmer)']
# PhoneNumbers = ['Mobile Number', 'Contact_Number', 'Contact Number', 'CONTACT_NO','Mobile NO',
#                    'Phone Number','MOBILE_NUMBER','MOBILE','Phone number','Mobile No.']

# beneficiary_names = ['Name of the Beneficiary', 'Beneficiary Name', 'PT_NAME', 'Name', 'BENEFICIARY_NAME', 'NAME_IN_AADHAR', 'Farmer Name', 'Name of the Beneficiary(Nominee of Deceased Farmer)']
# PhoneNumbers = ['Mobile  No.','Mobile Number', 'Contact_Number', 'Contact Number', 'CONTACT_NO', 'Mobile NO', 'Phone Number', 'MOBILE_NUMBER', 'MOBILE', 'Phone number', 'Mobile No.']
#
# # # constituency_name = 'Malkajgiri_44'
# for folder in all_folders:
#     # print('folder',folder)
#     if folder == 'Malkajgiri_44':
#         constituency_name = folder
#
#         all_files_in_folder = os.listdir(file_path+'/'+folder)
#         # print(len(all_files_phone_nums))
#         result_df = pd.DataFrame()
#         for file in all_files_in_folder:
#             print('file',file)
#             # print('file',file)
#             if file.endswith('.xlsx'):
#                 df = pd.read_excel(file_path+'/'+folder+'/'+file,header=1)
#                 print(file_path+'/'+folder+'/'+file)
#
#                 selected_columns = [col for col in df.columns if
#                                     col in PhoneNumbers or col in beneficiary_names]
#                 filtered_df = df[selected_columns].copy()  # Create a copy to avoid SettingWithCopyWarning
#                 column_mapping = {col: 'Mobile' for col in PhoneNumbers}
#                 column_mapping.update({col: 'Names' for col in beneficiary_names})
#                 filtered_df.rename(columns=column_mapping, inplace=True)
#                 print(file)
#                 print(filtered_df.columns)
#                 print(filtered_df)
#
#             if file.endswith('.csv'):
#
#                 df = pd.read_csv(file_path+'/'+folder+'/'+file)
#                 print(file_path+'/'+folder+'/'+file)
#
#                 selected_columns = [col for col in df.columns if
#                                     col in PhoneNumbers or col in beneficiary_names]
#                 filtered_df = df[selected_columns].copy()  # Create a copy to avoid SettingWithCopyWarning
#                 column_mapping = {col: 'Mobile' for col in PhoneNumbers}
#                 column_mapping.update({col: 'Names' for col in beneficiary_names})
#                 filtered_df.rename(columns=column_mapping, inplace=True)
#                 print(file)
#                 print(filtered_df.columns)
#                 print(filtered_df)


# import os
# import pandas as pd
#
# file_path = r"/home/rajashekar/Desktop/TS_CPU/BENEFICIARY_DATA_schemes/Malkajgiri"
#
# # Define column names
# beneficiary_names = ['Name of the Beneficiary', 'Beneficiary Name', 'PT_NAME', 'Name', 'BENEFICIARY_NAME', 'NAME_IN_AADHAR', 'Farmer Name', 'Name of the Beneficiary(Nominee of Deceased Farmer)']
# PhoneNumbers = ['Mobile Number', 'Contact_Number', 'Contact Number', 'CONTACT_NO', 'Mobile NO', 'Phone Number', 'MOBILE_NUMBER', 'MOBILE', 'Phone number', 'Mobile No.']
#
# # Specify the constituency name
# constituency_name = 'Malkajgiri_44'
#
# # Iterate through folders
# for folder in os.listdir(file_path):
#     if folder == constituency_name:
#         all_files_in_folder = os.listdir(os.path.join(file_path, folder))
#         for file in all_files_in_folder:
#             file_path_full = os.path.join(file_path, folder, file)
#             print('file', file)
#             try:
#                 if file.endswith('.xlsx') or file.endswith('.csv'):
#                     for i in range(0, 4):
#                         df = pd.read_excel(file_path_full, header=i) if file.endswith('.xlsx') else pd.read_csv(file_path_full, header=i)
#
#                         selected_columns = [col for col in df.columns if col in PhoneNumbers or col in beneficiary_names]
#                         filtered_df = df[selected_columns].copy()  # Create a copy to avoid SettingWithCopyWarning
#                         column_mapping = {col: 'Mobile' for col in PhoneNumbers}
#                         column_mapping.update({col: 'Names' for col in beneficiary_names})
#                         filtered_df.rename(columns=column_mapping, inplace=True)
#                         if len(filtered_df.columns) == 2:
#                             print(file)
#                             DF = df[["Names","Mobile"]]
#                             print(DF)
#             except Exception as e:
#                 print("Exception:", e)

# file_path = r"/home/rajashekar/Desktop/TS_CPU/BENEFICIARY_DATA_schemes/Adilabad"
# MP_Constituency = file_path.split('/')[-1]
# print(MP_Constituency)

# for i in range(0,10):
#     print(i)
#
# for i in range(1,10,3):
#     print(i)

# import os
#
# folder1_path = "/home/rajashekar/Desktop/Andhra_State_Daily_data/Machilipatnam/Machilipatnam_imported_Data/constituencies_To_be_cleaned/IMPORTED_DATA_2"
# folder2_path = "/home/rajashekar/Desktop/Andhra_State_Daily_data/Machilipatnam/Machilipatnam_imported_Data/constituencies_To_be_cleaned/Imported_Data_3"
#
# folder1_files = sorted(os.listdir(folder1_path))
# folder2_files = sorted(os.listdir(folder2_path))
#
# # Find common filenames
# common_files = set(folder1_files) & set(folder2_files)
#
# # Concatenate common files
# concatenated_files = {}
# for filename in common_files:
#     with open(os.path.join(folder1_path, filename), 'r') as f1, open(os.path.join(folder2_path, filename), 'r') as f2:
#         content1 = f1.read()
#         content2 = f2.read()
#         concatenated_files[filename] = content1 + content2
#
# # Concatenate files only present in folder1
# for filename in set(folder1_files) - common_files:
#     with open(os.path.join(folder1_path, filename), 'r') as f:
#         concatenated_files[filename] = f.read()
#
# # Concatenate files only present in folder2
# for filename in set(folder2_files) - common_files:
#     with open(os.path.join(folder2_path, filename), 'r') as f:
#         concatenated_files[filename] = f.read()
#
# # Output concatenated files
# for filename, content in concatenated_files.items():
#     print(f"Concatenated file {filename}:")
#     print(content)
#     print("-" * 20)


import pandas as pd

df = pd.read_excel(r"/home/rajashekar/Desktop/TS_CPU/TELANGANA_MP_EACH_CONSTITUENCY_VERIFIED_DATA/Medak/Medak_verified_Mp_Data1.xlsx")
df.dropna(inplace = True)
df.to_excel("Medak_verified_Data.xlsx",index = False)