import os
from indic_transliteration import sanscript
import pandas as pd
import re
file_path = r"/home/rajashekar/Desktop/TS_CPU/Schemes/BD"
# possible_column_names = ['mobile','contact','phone']
all_folders = os.listdir(file_path)
# beneficiary_names = ['Name of the Beneficiary', 'Beneficiary Name', 'PT_NAME', 'Name', 'BENEFICIARY_NAME','NAME_IN_AADHAR', 'Farmer Name',
#                      'Name of the Beneficiary(Nominee of Deceased Farmer)']
PhoneNumbers = ['Mobile Number', 'Contact_Number', 'Contact Number', 'CONTACT_NO','Mobile NO',
                   'Phone Number','MOBILE_NUMBER','MOBILE','Phone number','Mobile No.','Mobile  No.','Mobile  No.']
# constituency_name = 'Malkajgiri_44'
for folder in all_folders:
    # print('folder',folder)
    if folder == 'Dubbak_41':
        constituency_name = folder

        all_files_in_folder = os.listdir(file_path+'/'+folder)
        # print(len(all_files_phone_nums))
        result_df = pd.DataFrame()
        for file in all_files_in_folder:
            # print('file',file)
            # print('file',file)
            if file.endswith('.xlsx'):
                try:
                    for i in range(1,4):
                        df = pd.read_excel(file_path+'/'+folder+'/'+file,header=i)
                        # print(file_path+'/'+folder+'/'+file)

                        # selected_columns = [col for col in df.columns if col in PhoneNumbers or col in beneficiary_names]

                        selected_columns = [col for col in df.columns if
                                            col in PhoneNumbers]
                        filtered_df = df[selected_columns].copy()  # Create a copy to avoid SettingWithCopyWarning
                        column_mapping = {col: 'Mobile' for col in PhoneNumbers}
                        # column_mapping.update({col: 'Names' for col in beneficiary_names})
                        filtered_df.rename(columns=column_mapping, inplace=True)
                        # print(filtered_df.columns)
                        # print(filtered_df)
                        if len(filtered_df.columns) == 1:
                            def clean_mobile_number(mobile):
                                # Convert scientific notation to normal form
                                if 'e' in str(mobile):
                                    mobile = "{:.0f}".format(mobile)
                                # Remove ".0" if it exists at the end
                                mobile_str = str(mobile)
                                if mobile_str.endswith('.0'):
                                    mobile = mobile_str[:-2]
                                return mobile


                            filtered_df['Mobile'] = filtered_df['Mobile'].apply(clean_mobile_number)
                            filtered_df['Mobile'] = filtered_df['Mobile'].astype('str')
                            filtered_df = filtered_df[filtered_df['Mobile'].str.isdigit()]
                            filtered_df['Mobile'] = filtered_df['Mobile'].apply(
                                lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
                            filtered_df['Mobile'] = filtered_df['Mobile'].apply(
                                lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
            #
            #                 # def add_space_in_dot(name):
            #                 #     if "." in name:
            #                 #         name = name.replace(".", " ")
            #                 #         return name
            #                 #     else:
            #                 #         return name
            #                 # filtered_df['Names'] = filtered_df['Names'].apply(add_space_in_dot)
            #                 # def is_telugu_word(word):
            #                 #     telugu_range = range(0x0C00, 0x0C7F)
            #                 #     for char in str(word):
            #                 #         if ord(char) in telugu_range:
            #                 #             mod = sanscript.transliterate(word, sanscript.TELUGU, sanscript.HK)
            #                 #             if 'Ò' or 'È' in mod:
            #                 #                 mod = ''.join(['O' if letter == 'Ò' else letter for letter in mod])
            #                 #                 mod = ''.join(['E' if letter == 'È' else letter for letter in mod])
            #                 #                 mod = ''.join(['e' if letter == 'è' else letter for letter in mod])
            #                 #                 mod = ''.join(['o' if letter == 'ò' else letter for letter in mod])
            #                 #                 mod = ''.join(['S' if letter == 'Z' else letter for letter in mod])
            #                 #                 mod = ''.join(['s' if letter == 'z' else letter for letter in mod])
            #                 #                 mod = ''.join(['ch' if letter == 'c' else letter for letter in mod])
            #                 #                 def replace_m(word):
            #                 #                     def replace(match):
            #                 #                         return re.sub(r'(?<!^)M(?!$)', 'n', match.group())
            #                 #
            #                 #                     return re.sub(r'\b\w+\b', replace, word)
            #                 #
            #                 #                 # Example usage:
            #                 #                 word = mod
            #                 #                 result = replace_m(word)
            #                 #                 return result
            #                 #             else:
            #                 #                 return mod
            #                 #     return word
            #                 # filtered_df['Names'] = filtered_df['Names'].apply(is_telugu_word)
            #                 # def extract_alphabets_and_spaces(values):
            #                 #     value = str(values)
            #                 #     return re.sub(r'[^a-zA-Z\s]', '', value)
            #                 # filtered_df['Names'] = filtered_df['Names'].apply(extract_alphabets_and_spaces)
            #                 #
            #                 # filtered_df['Names'] = filtered_df['Names'].str.strip()
            #                 # filtered_df = filtered_df[filtered_df["Names"].str.strip() != ""]
                            filtered_df.drop_duplicates(subset=["Mobile"],inplace=True)
                            print(file,len(filtered_df))
                            result_df = pd.concat([result_df, filtered_df],axis=0, ignore_index=True)

                        else :
                            pass
                except Exception as E:
                    print('exception...', E)

            if file.endswith('.csv'):
            # if file.endswith('.csv') and ('Arogya Laxmi' in file):

                try:
                    df = pd.read_csv(file_path+'/'+folder+'/'+file)
                    # print(file_path+'/'+folder+'/'+file)
                    # selected_columns = [col for col in df.columns if  col in PhoneNumbers or col in beneficiary_names]
                    selected_columns = [col for col in df.columns if  col in PhoneNumbers]

                    filtered_df = df[selected_columns].copy()  # Create a copy to avoid SettingWithCopyWarning
                    column_mapping = {col: 'Mobile' for col in PhoneNumbers}
                    # column_mapping.update({col: 'Names' for col in beneficiary_names})
                    filtered_df.rename(columns=column_mapping, inplace=True)
                    # print(filtered_df.columns)
                    # print(filtered_df)
                    if len(filtered_df.columns) == 1:

                        def clean_mobile_number(mobile):
                            # Convert scientific notation to normal form
                            if 'e' in str(mobile):
                                mobile = "{:.0f}".format(mobile)
                            # Remove ".0" if it exists at the end
                            mobile_str = str(mobile)
                            if mobile_str.endswith('.0'):
                                mobile = mobile_str[:-2]
                            return mobile

                        filtered_df['Mobile'] = filtered_df['Mobile'].apply(clean_mobile_number)
                        filtered_df['Mobile'] = filtered_df['Mobile'].astype('str')
                        filtered_df = filtered_df[filtered_df['Mobile'].str.isdigit()]
                        filtered_df['Mobile'] = filtered_df['Mobile'].apply(
                            lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
                        filtered_df['Mobile'] = filtered_df['Mobile'].apply(
                            lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)

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
                        filtered_df.drop_duplicates(subset=["Mobile"], inplace=True)
                        print(file,len(filtered_df))
                        result_df = pd.concat([result_df, filtered_df], axis=0,ignore_index=True)

                    else:
                        pass
                except Exception as E:
                    print('exception...',E)
        print("result_df",len(result_df))
        #
        # result_df['Mobile'] = result_df['Mobile'].apply(lambda x:"{:.0f}".format(x) if 'e' in x else x)
        # result_df['Mobile'] = result_df['Mobile'].apply(lambda x: x[:-2 if x.endswith('.0') else x)
        # def clean_mobile_number(mobile):
        #     # Convert scientific notation to normal form
        #     if 'e' in str(mobile):
        #         mobile = "{:.0f}".format(mobile)
        #     # Remove ".0" if it exists at the end
        #     mobile_str = str(mobile)
        #     if mobile_str.endswith('.0'):
        #         mobile = mobile_str[:-2]
        #     return mobile


        def clean_mobile_number(mobile):
            if mobile is None:
                return None  # Return None if mobile is None

            # Convert to string
            mobile_str = str(mobile)

            # Convert scientific notation to normal form
            if 'e' in mobile_str:
                mobile_str = "{:.0f}".format(float(mobile_str))

            # Remove ".0" if it exists at the end
            if mobile_str.endswith('.0'):
                mobile_str = mobile_str[:-2]

            return mobile_str
        result_df['Mobile'] = result_df['Mobile'].apply(clean_mobile_number)
        result_df['Mobile'] = result_df['Mobile'].astype('str')
        result_df = result_df[result_df['Mobile'].str.isdigit()]
        result_df['Mobile'] = result_df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
        result_df['Mobile'] = result_df['Mobile'].apply(lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
        # result_df.dropna(subset=['Names','Mobile'], inplace=True)
        # result_df["Names"] = result_df["Names"].apply(lambda x:x if len(x)>0 else x)
        # result_df = result_df[result_df["Names"].str.strip() != ""]
        # result_df.drop_duplicates(subset=['Names','Mobile'], inplace=True)
        print(result_df)
        # print("*********************************************************After removal of duplicate rows",len(result_df))

        # result_df.to_excel(f"C:\\Users\\jaswa\\Desktop\\TS\\Beneficiary_original\\Chevella_53\\{constituency_name}_o_beneficiary_scheme.xlsx",index=False)
        result_df.drop_duplicates(subset=['Mobile'], inplace=True)

        print("*************************************************************After removal of duplicate mobiles",len(result_df))
        # result_df.to_excel(f"C:\\Users\\jaswa\\Desktop\\TS\\Beneficiary_unique\\Chevella_53\\{constituency_name}_u_beneficiary_scheme.xlsx",index=False)
        print("....................................................success..")

# for i in all_folders:
#     print(i)