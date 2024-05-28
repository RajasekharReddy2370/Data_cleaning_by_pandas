import os
from indic_transliteration import sanscript
import pandas as pd
import re
file_path = r'/home/rajashekar/Desktop/TS_CPU/BENEFICIARY_DATA_schemes/Mahbubnagar'
# possible_column_names = ['mobile','contact','phone']
all_folders = os.listdir(file_path)
# print(all_folders)
# beneficiary_names = ['Names','Name of the Beneficiary', 'Beneficiary Name', 'PT_NAME', 'Name', 'BENEFICIARY_NAME','NAME_IN_AADHAR', 'Farmer Name',
#                      'Name of the Beneficiary(Nominee of Deceased Farmer)']
PhoneNumbers = ['Mobile','Mobile Number', 'Contact_Number', 'Contact Number', 'CONTACT_NO','Mobile NO','Mobile_No',
                   'Phone Number','MOBILE_NUMBER','MOBILE','Phone number','Mobile No.']
gender = ['Gender']
# constituency_name = 'Malkajgiri_44'
for folder in all_folders:
    print('folder',folder)
    if folder == 'Makthal_77':
        print(folder)
        constituency_name = folder

        all_files_in_folder = os.listdir(file_path+'/'+folder)
        # print(len(all_files_phone_nums))
        result_df = pd.DataFrame()
        for file in all_files_in_folder:
            # print('file',file)
            print('file',file)
            # if file.endswith('.xlsx'):
            #     try:
            #         for i in range(1,4):
            #             df = pd.read_excel(file_path+'/'+folder+'/'+file,header=i)
            #             # print(file_path+'/'+folder+'/'+file)
            # #
            #             selected_columns = [col for col in df.columns if
            #                                 col in PhoneNumbers or col in gender]
            #             filtered_df = df[selected_columns].copy()  # Create a copy to avoid SettingWithCopyWarning
            #             column_mapping = {col: 'Mobile' for col in PhoneNumbers}
            #             # column_mapping.update({col: 'Names' for col in beneficiary_names})
            #             column_mapping.update(
            #                 {col: 'Gender' for col in gender})  # Update the mapping for the 'Gender' column
            #             filtered_df.rename(columns=column_mapping, inplace=True)
            # #
            # #             # print(filtered_df.columns)
            # #             # print(filtered_df)
            #             if len(filtered_df.columns) == 2:
            #                 print(file)
            #                 filtered_df_female = filtered_df[filtered_df['Gender'] == 'Male']
            #                 print(filtered_df)
            # #
            # #                 def add_space_in_dot(name):
            # #                     if "." in name:
            # #                         name = name.replace(".", " ")
            # #                         return name
            # #                     else:
            # #                         return name
            # #                 filtered_df['Names'] = filtered_df['Names'].apply(add_space_in_dot)
            # #                 def is_telugu_word(word):
            # #                     telugu_range = range(0x0C00, 0x0C7F)
            # #                     for char in str(word):
            # #                         if ord(char) in telugu_range:
            # #                             mod = sanscript.transliterate(word, sanscript.TELUGU, sanscript.HK)
            # #                             if 'Ò' or 'È' in mod:
            # #                                 mod = ''.join(['O' if letter == 'Ò' else letter for letter in mod])
            # #                                 mod = ''.join(['E' if letter == 'È' else letter for letter in mod])
            # #                                 mod = ''.join(['e' if letter == 'è' else letter for letter in mod])
            # #                                 mod = ''.join(['o' if letter == 'ò' else letter for letter in mod])
            # #                                 mod = ''.join(['S' if letter == 'Z' else letter for letter in mod])
            # #                                 mod = ''.join(['s' if letter == 'z' else letter for letter in mod])
            # #                                 mod = ''.join(['ch' if letter == 'c' else letter for letter in mod])
            # #                                 def replace_m(word):
            # #                                     def replace(match):
            # #                                         return re.sub(r'(?<!^)M(?!$)', 'n', match.group())
            # #
            # #                                     return re.sub(r'\b\w+\b', replace, word)
            # #
            # #                                 # Example usage:
            # #                                 word = mod
            # #                                 result = replace_m(word)
            # #                                 return result
            # #                             else:
            # #                                 return mod
            # #                     return word
            # #                 filtered_df['Names'] = filtered_df['Names'].apply(is_telugu_word)
            # #                 def extract_alphabets_and_spaces(values):
            # #                     value = str(values)
            # #                     return re.sub(r'[^a-zA-Z\s]', '', value)
            # #                 filtered_df['Names'] = filtered_df['Names'].apply(extract_alphabets_and_spaces)
            # #
            # #                 filtered_df['Names'] = filtered_df['Names'].str.strip()
            # #                 filtered_df = filtered_df[filtered_df["Names"].str.strip() != ""]
            # #                 print(len(filtered_df))
            #                 result_df = pd.concat([result_df, filtered_df],axis=0, ignore_index=True)
            # #
            #             else :
            #                 pass
            #     except Exception as E:
            #         print('exception...', E)

            # if file.endswith('.csv') and ('Laxmi' in file or 'Shadi' in file or 'KCR' in file or 'Arogyasri' in file):
            if file.endswith('.csv') and ('Bed' in file):
            # if file.endswith('.csv')  ('Arogya Laxmi' in file):

                try:
                    # for i in range(1,4):
                    #     df = pd.read_excel(file_path+'/'+folder+'/'+file,header=i)
                    df = pd.read_csv(file_path + '/' + folder + '/' + file,low_memory=False)
                    # print(file_path + '/' + folder + '/' + file)
                    selected_columns = [col for col in df.columns if
                                        col in PhoneNumbers]
                    filtered_df = df[selected_columns].copy()  # Create a copy to avoid SettingWithCopyWarning
                    column_mapping = {col: 'Mobile' for col in PhoneNumbers}
                    # column_mapping.update({col: 'Names' for col in beneficiary_names})
                    # column_mapping.update(
                    #     {col: 'Gender' for col in gender})  # Update the mapping for the 'Gender' column
                    filtered_df.rename(columns=column_mapping, inplace=True)

                    print(filtered_df.columns)
                    if len(filtered_df.columns) in [1,2]:
                        # Filter the DataFrame to contain only rows where the "Gender" column contains the value 'Female'
                        # filtered_df_female = filtered_df[filtered_df['Gender'] == 'Female']
                        print(filtered_df)
                        # def add_space_in_dot(name):
                        #     if "." in name:
                        #         name = name.replace(".", " ")
                        #         return name
                        #     else:
                        #         return name
                        # filtered_df['Names'] = filtered_df['Names'].apply(add_space_in_dot)
                        # def is_telugu_word(word):
                        #     telugu_range = range(0x0C00, 0x0C7F)
                        #     for char in str(word):
                        #         if ord(char) in telugu_range:
                        #             mod = sanscript.transliterate(word, sanscript.TELUGU, sanscript.HK)
                        #             if 'Ò' or 'È' in mod:
                        #                 mod = ''.join(['O' if letter == 'Ò' else letter for letter in mod])
                        #                 mod = ''.join(['E' if letter == 'È' else letter for letter in mod])
                        #                 mod = ''.join(['e' if letter == 'è' else letter for letter in mod])
                        #                 mod = ''.join(['o' if letter == 'ò' else letter for letter in mod])
                        #                 mod = ''.join(['S' if letter == 'Z' else letter for letter in mod])
                        #                 mod = ''.join(['s' if letter == 'z' else letter for letter in mod])
                        #                 mod = ''.join(['ch' if letter == 'c' else letter for letter in mod])
                        #                 def replace_m(word):
                        #                     def replace(match):
                        #                         return re.sub(r'(?<!^)M(?!$)', 'n', match.group())
                        #
                        #                     return re.sub(r'\b\w+\b', replace, word)
                        #                 # Example usage:
                        #                 word = mod
                        #                 result = replace_m(word)
                        #                 return result
                        #             else:
                        #                 return mod
                        #     return word
                        # filtered_df['Names'] = filtered_df['Names'].apply(is_telugu_word)
                        # def extract_alphabets_and_spaces(values):
                        #     value = str(values)
                        #     return re.sub(r'[^a-zA-Z\s]', '', value)
                        # filtered_df['Names'] = filtered_df['Names'].apply(extract_alphabets_and_spaces)
                        #
                        # filtered_df['Names'] = filtered_df['Names'].str.strip()
                        # filtered_df = filtered_df[filtered_df["Names"].str.strip() != ""]
                        print(len(filtered_df))
                        result_df = pd.concat([result_df, filtered_df], axis=0,ignore_index=True)

                    else:
                        pass
                except Exception as E:
                    print('exception...',E)

        print("result_df",len(result_df))
        print(result_df.columns,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        # print(result_df)
        # result_df = result_df[(result_df['Gender'] == 'Female') | (result_df['Gender'].isna())]
        # result_df = result_df[(result_df['Gender'] == 'Male')]
        # result_df = result_df[(result_df['Gender'] == 'Female')]
        # print(len(result_df))
        # print(result_df)

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
        # result_df.dropna(subset=['Names','Mobile'], inplace=True)
        # result_df["Names"] = result_df["Names"].apply(lambda x:x if len(x)>0 else x)
        # result_df = result_df[result_df["Names"].str.strip() != ""]
        # result_df.drop_duplicates(subset=['Names','Mobile'], inplace=True)
        # result_df.drop_duplicates(subset=['Names','Mobile'], inplace=True)
        # result_df = result_df[result_df["Gender"]=='Female']
        # print("*********************************************************After removal of duplicate rows",len(result_df))

        # result_df.to_excel(f"C:\\Users\\jaswa\\Desktop\\TS\\Beneficiary_original\\Chevella_53\\{constituency_name}_o_beneficiary_scheme.xlsx",index=False)
        result_df.drop_duplicates(subset=['Mobile'], inplace=True)
        # result_df = result_df[["Names","Mobile"]]
        result_df = result_df[["Mobile"]]
        print(result_df)
        # result_df.to_excel(f'/home/rajashekar/Desktop/ThursDay_Meh_Med/Medak/Medak_Double_Bedroom/{constituency_name}_Double_bed_room_Data.xlsx',index=False)
        # result_df.to_excel(f'/home/rajashekar/Desktop/ThursDay_Meh_Med/Mahbubnagar/Mahbubnagar_Beneficiary_Females/{constituency_name}_Female_Data.xlsx',index=False)

        print("*************************************************************After removal of duplicate mobiles",len(result_df))
        # result_df.to_excel(f"/home/rajashekar/Desktop/M_Fe_Ma_Data/B_Females/{constituency_name}_u_beneficiary_Female.xlsx",index=False)
        print("....................................................success..",folder)


# for i in all_folders:
#     print(i)








