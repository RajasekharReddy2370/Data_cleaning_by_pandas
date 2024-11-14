
import os
from indic_transliteration import sanscript
import pandas as pd
import re
file_path = r"/home/rajashekar/Desktop/RAJA_LAPTOP/Telangana/TELANGANA/TELANGANA_MOBILE_NUMBERS_from_Drive_data_and_schemes/Beneficiary_Data_All_schemes"
# possible_column_names = ['mobile','contact','phone']
all_folders = os.listdir(file_path)
beneficiary_names = ['Name of the Beneficiary', 'Beneficiary Name', 'PT_NAME', 'Name', 'BENEFICIARY_NAME','NAME_IN_AADHAR', 'Farmer Name',
                     'Name of the Beneficiary(Nominee of Deceased Farmer)','Names']
PhoneNumbers = ['Mobile Number', 'Contact_Number', 'Contact Number', 'CONTACT_NO','Mobile NO',
                   'Phone Number','MOBILE_NUMBER','MOBILE','Phone number','Mobile No.','Mobile']


# constituency_name = 'Malkajgiri_44'
c = 0
for folder in all_folders:
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",folder)
    constituency_lengths_Name_Mobile = {}

    # print('folder',folder)
    if folder != 'Ts':
        constituency_name = folder.split('_')[0]

        all_files_in_folder = os.listdir(file_path+'/'+folder)
        # print(len(all_files_phone_nums))
        result_df = pd.DataFrame()
        for file in all_files_in_folder:
            # print('file',file)
            # print('file',file)
            if file.endswith('.xlsx'):
                try:
                    for i in range(0,4):
                        df = pd.read_excel(file_path+'/'+folder+'/'+file,header=i)
                        print(file_path+'/'+folder+'/'+file)

                        selected_columns = [col for col in df.columns if
                                            col in PhoneNumbers or col in beneficiary_names]
                        filtered_df = df[selected_columns].copy()  # Create a copy to avoid SettingWithCopyWarning
                        column_mapping = {col: 'Mobile' for col in PhoneNumbers}
                        column_mapping.update({col: 'Names' for col in beneficiary_names})
                        filtered_df.rename(columns=column_mapping, inplace=True)
                        print(filtered_df.columns)
                        # print(filtered_df)
                        if len(filtered_df.columns) == 2:

                            def add_space_in_dot(name):
                                if "." in name:
                                    name = name.replace(".", " ")
                                    return name
                                else:
                                    return name
                            filtered_df['Names'] = filtered_df['Names'].apply(add_space_in_dot)
                            def is_telugu_word(word):
                                telugu_range = range(0x0C00, 0x0C7F)
                                for char in str(word):
                                    if ord(char) in telugu_range:
                                        mod = sanscript.transliterate(word, sanscript.TELUGU, sanscript.HK)
                                        if 'Ò' or 'È' in mod:
                                            mod = ''.join(['O' if letter == 'Ò' else letter for letter in mod])
                                            mod = ''.join(['E' if letter == 'È' else letter for letter in mod])
                                            mod = ''.join(['e' if letter == 'è' else letter for letter in mod])
                                            mod = ''.join(['o' if letter == 'ò' else letter for letter in mod])
                                            mod = ''.join(['S' if letter == 'Z' else letter for letter in mod])
                                            mod = ''.join(['s' if letter == 'z' else letter for letter in mod])
                                            mod = ''.join(['ch' if letter == 'c' else letter for letter in mod])
                                            def replace_m(word):
                                                def replace(match):
                                                    return re.sub(r'(?<!^)M(?!$)', 'n', match.group())

                                                return re.sub(r'\b\w+\b', replace, word)

                                            # Example usage:
                                            word = mod
                                            result = replace_m(word)
                                            return result
                                        else:
                                            return mod
                                return word
                            filtered_df['Names'] = filtered_df['Names'].apply(is_telugu_word)
                            def extract_alphabets_and_spaces(values):
                                value = str(values)
                                return re.sub(r'[^a-zA-Z\s]', '', value)
                            filtered_df['Names'] = filtered_df['Names'].apply(extract_alphabets_and_spaces)

                            filtered_df['Names'] = filtered_df['Names'].str.strip()
                            filtered_df = filtered_df[filtered_df["Names"].str.strip() != ""]
                            filtered_df["Names"] = filtered_df["Names"].str.title()
                            print(len(filtered_df))
                            result_df = pd.concat([result_df, filtered_df],axis=0, ignore_index=True)

                        else :
                            pass
                except Exception as E:
                    print('exception...', E)

            if file.endswith('.csv'):
                try:
                    df = pd.read_csv(file_path+'/'+folder+'/'+file,low_memory=False)
                    # print(file_path+'/'+folder+'/'+file)
                    selected_columns = [col for col in df.columns if
                                        col in PhoneNumbers or col in beneficiary_names]
                    filtered_df = df[selected_columns].copy()  # Create a copy to avoid SettingWithCopyWarning
                    column_mapping = {col: 'Mobile' for col in PhoneNumbers}
                    column_mapping.update({col: 'Names' for col in beneficiary_names})
                    filtered_df.rename(columns=column_mapping, inplace=True)
                    print(filtered_df.columns)
                    # print(filtered_df)
                    if len(filtered_df.columns) == 2:

                        def add_space_in_dot(name):
                            if "." in name:
                                name = name.replace(".", " ")
                                return name
                            else:
                                return name
                        filtered_df['Names'] = filtered_df['Names'].apply(add_space_in_dot)
                        def is_telugu_word(word):
                            telugu_range = range(0x0C00, 0x0C7F)
                            for char in str(word):
                                if ord(char) in telugu_range:
                                    mod = sanscript.transliterate(word, sanscript.TELUGU, sanscript.HK)
                                    if 'Ò' or 'È' in mod:
                                        mod = ''.join(['O' if letter == 'Ò' else letter for letter in mod])
                                        mod = ''.join(['E' if letter == 'È' else letter for letter in mod])
                                        mod = ''.join(['e' if letter == 'è' else letter for letter in mod])
                                        mod = ''.join(['o' if letter == 'ò' else letter for letter in mod])
                                        mod = ''.join(['S' if letter == 'Z' else letter for letter in mod])
                                        mod = ''.join(['s' if letter == 'z' else letter for letter in mod])
                                        mod = ''.join(['ch' if letter == 'c' else letter for letter in mod])
                                        def replace_m(word):
                                            def replace(match):
                                                return re.sub(r'(?<!^)M(?!$)', 'n', match.group())

                                            return re.sub(r'\b\w+\b', replace, word)
                                        # Example usage:
                                        word = mod
                                        result = replace_m(word)
                                        return result
                                    else:
                                        return mod
                            return word
                        filtered_df['Names'] = filtered_df['Names'].apply(is_telugu_word)
                        def extract_alphabets_and_spaces(values):
                            value = str(values)
                            return re.sub(r'[^a-zA-Z\s]', '', value)
                        filtered_df['Names'] = filtered_df['Names'].apply(extract_alphabets_and_spaces)

                        filtered_df['Names'] = filtered_df['Names'].str.strip()
                        filtered_df = filtered_df[filtered_df["Names"].str.strip() != ""]
                        filtered_df["Names"] = filtered_df["Names"].str.title()
                        # print(len(filtered_df))
                        result_df = pd.concat([result_df, filtered_df], axis=0,ignore_index=True)

                    else:
                        pass
                except Exception as E:
                    print('exception...',E)
        print("result_df",len(result_df))

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

        result_df['Mobile'] = result_df['Mobile'].apply(clean_mobile_number)

        result_df['Mobile'] = result_df['Mobile'].astype('str')
        result_df = result_df[result_df['Mobile'].str.isdigit()]
        result_df['Mobile'] = result_df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
        result_df['Mobile'] = result_df['Mobile'].apply(lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
        result_df.dropna(subset=['Names','Mobile'], inplace=True)
        result_df["Names"] = result_df["Names"].apply(lambda x:x if len(x)>0 else x)
        result_df = result_df[result_df["Names"].str.strip() != ""]
        result_df.drop_duplicates(subset=['Names','Mobile'], inplace=True)
        # print(result_df)
        print("*********************************************************After removal of duplicate rows",len(result_df))

        # result_df.to_excel(f"C:\\Users\\jaswa\\Desktop\\TS\\Beneficiary_original\\Chevella_53\\{constituency_name}_o_beneficiary_scheme.xlsx",index=False)
        # result_df.drop_duplicates(subset=['Mobile'], inplace=True)

        # print("*************************************************************After removal of duplicate mobiles",len(result_df))
        result_df.to_excel(f"/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/Names_Mobile/{constituency_name}_beneficiary_scheme.xlsx",index=False)
        c += 1
        print("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc",c)
        print("....................................................success..")
        constituency_lengths_Name_Mobile[constituency_name] = len(result_df)

constituency_df_n_m = pd.DataFrame(list(constituency_lengths_Name_Mobile.items()), columns=['Constituency', 'Length'])
constituency_df_n_m.to_excel(f"/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/constituency_lengths/Names_Mobile/Telangana_Beneficiary_Names_Mobile_constituency_lengths.xlsx",index = False)

for i in all_folders:
    print(i)



# import os
# from indic_transliteration import sanscript
# import pandas as pd
# import re
#
# file_path = r"/home/rajashekar/Desktop/RAJA_LAPTOP/Telangana/TELANGANA/TELANGANA_MOBILE_NUMBERS_from_Drive_data_and_schemes/Beneficiary_Data_All_schemes"
# all_folders = os.listdir(file_path)
#
# # Column name mappings
# beneficiary_names = ['Name of the Beneficiary', 'Beneficiary Name', 'PT_NAME', 'Name', 'BENEFICIARY_NAME', 'NAME_IN_AADHAR', 'Farmer Name', 'Name of the Beneficiary(Nominee of Deceased Farmer)', 'Names']
# phone_numbers = ['Mobile Number', 'Contact_Number', 'Contact Number', 'CONTACT_NO', 'Mobile NO', 'Phone Number', 'MOBILE_NUMBER', 'MOBILE', 'Phone number', 'Mobile No.', 'Mobile']
#
# for folder in all_folders:
#     constituency_lengths = {}
#
#     if folder != 'Ts':
#         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",folder)
#         constituency_name = folder.split('_')[0]
#         all_files_in_folder = os.listdir(os.path.join(file_path, folder))
#         result_df = pd.DataFrame()
#
#         for file in all_files_in_folder:
#             if file.endswith(('.xlsx', '.csv')):
#                 file_path_full = os.path.join(file_path, folder, file)
#                 # print('Processing file:', file)
#
#                 try:
#                     # Try reading the file based on its extension
#                     if file.endswith('.xlsx'):
#                         df = pd.read_excel(file_path_full, header=0)
#                     elif file.endswith('.csv'):
#                         df = pd.read_csv(file_path_full, low_memory=False)
#
#                     # Check if the necessary columns are already present
#                     if 'Names' in df.columns and 'Mobile' in df.columns:
#                         filtered_df = df[['Names', 'Mobile']].copy()
#                     else:
#                         # Select columns based on predefined lists
#                         selected_columns = [col for col in df.columns if col in phone_numbers or col in beneficiary_names]
#                         if not selected_columns:
#                             continue  # Skip if no relevant columns found
#
#                         filtered_df = df[selected_columns].copy()
#                         column_mapping = {col: 'Mobile' for col in phone_numbers}
#                         column_mapping.update({col: 'Names' for col in beneficiary_names})
#                         filtered_df.rename(columns=column_mapping, inplace=True)
#
#                     # Ensure only the required columns are present
#                     if 'Names' in filtered_df.columns and 'Mobile' in filtered_df.columns:
#                         filtered_df['Names'] = filtered_df['Names'].str.strip()
#                         filtered_df['Mobile'] = filtered_df['Mobile'].astype(str).str.strip()
#
#                         # Clean the mobile numbers
#                         def clean_mobile_number(mobile):
#                             try:
#                                 mobile_float = float(mobile)
#                                 mobile = "{:.0f}".format(mobile_float)
#                             except ValueError:
#                                 mobile = str(mobile)
#
#                             if mobile.endswith(".0"):
#                                 mobile = mobile[:-2]
#
#                             return mobile
#
#                         filtered_df['Mobile'] = filtered_df['Mobile'].apply(clean_mobile_number)
#                         filtered_df = filtered_df[filtered_df['Mobile'].str.isdigit()]
#                         filtered_df['Mobile'] = filtered_df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
#                         filtered_df['Mobile'] = filtered_df['Mobile'].apply(lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
#                         filtered_df.dropna(subset=['Names', 'Mobile'], inplace=True)
#
#                         # Remove duplicates and clean names
#                         filtered_df.drop_duplicates(subset=['Names', 'Mobile'], inplace=True)
#
#                         result_df = pd.concat([result_df, filtered_df], axis=0, ignore_index=True)
#
#                 except Exception as e:
#                     print('Exception while processing file:', file, e)
#
#         # Remove duplicates based on 'Mobile' and save the result
#         # result_df.drop_duplicates(subset=['Mobile'], inplace=True)
#         result_df.drop_duplicates(subset=['Names','Mobile'], inplace=True)
#         print(f"After removing duplicates, total rows for {constituency_name}: {len(result_df)}")
#
#         output_path = f"/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/Names_Mobile/{constituency_name}_beneficiary_scheme.xlsx"
#         result_df.to_excel(output_path, index=False)
#         print(f"Successfully saved: {output_path}")
#
#         constituency_lengths[constituency_name] = len(result_df)
#
#     # Save the constituency lengths summary
#     lengths_df = pd.DataFrame(list(constituency_lengths.items()), columns=['Constituency', 'Length'])
#     lengths_df.to_excel(f"/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/constituency_lengths/Names_Mobile/Telangana_Beneficiary_Names_Mobile_constituency_lengths.xlsx", index=False)
#
# print("Processing completed for all folders.")







