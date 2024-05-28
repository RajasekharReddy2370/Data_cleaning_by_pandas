import os
from indic_transliteration import sanscript
import pandas as pd
import re
import time

start_time = time.time()

file_path = r"/home/rajashekar/Desktop/TS_CPU/BENEFICIARY_DATA_schemes/Mahbubnagar"
# possible_column_names = ['mobile','contact','phone']
all_folders = os.listdir(file_path)
# beneficiary_names = ['Names','Name of the Beneficiary', 'Beneficiary Name', 'PT_NAME', 'Name', 'BENEFICIARY_NAME','NAME_IN_AADHAR', 'Farmer Name',
#                      'Name of the Beneficiary(Nominee of Deceased Farmer)']
# PhoneNumbers = ['Mobile','Mobile Number', 'Contact_Number', 'Contact Number', 'CONTACT_NO','Mobile NO',
#                    'Phone Number','MOBILE_NUMBER','MOBILE','Phone number','Mobile No.']
# constituency_name = 'Malkajgiri_44'
for folder in all_folders:
    # print('folder',folder)
    if folder == 'Shadnagar_84':
        fol = folder.split('_')[0]

        all_files_in_folder = os.listdir(file_path+'/'+folder)
        # print(len(all_files_phone_nums))
        cdf = pd.DataFrame()
        c = 0
        for file in all_files_in_folder:
            fil = file.split('.xlsx')[0]
            c+=1
            # print('file','-----------------------',file)
            # print('file',file)
            if file.endswith('.xlsx') and ('Bandhu' in file):
                # print('file','ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff',file)
                df = pd.read_excel(file_path + '/' + folder + '/' + file,usecols=["Mobile"])
                # print(df.columns)
                # print("ooooooooooooooooooooooooooollllllllllllllllllllllllllllllllllllllllllllllllllll",len(df))
                #
                # df.dropna(subset=["Names"],inplace=True)
                # df.dropna(subset=["Mobile"],inplace=True)
                # print("A_F_Nullllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll",len(df))

                def clean_mobile_number(mobile):
                    try:
                        mobile_float = float(mobile)
                        mobile = "{:.0f}".format(mobile_float)
                    except ValueError:
                        mobile = str(mobile)

                    if mobile.endswith(".0"):
                        mobile = mobile[:-2]

                    return mobile

                # Assuming df is your DataFrame
                df['Mobile'] = df['Mobile'].apply(clean_mobile_number)

                df['Mobile'] = df['Mobile'].astype('str')
                df = df[df['Mobile'].str.isdigit()]
                df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
                df['Mobile'] = df['Mobile'].apply(
                    lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
                df = df[df["Mobile"].notna()]  # Remove rows where Mobile is None
                print("A_M_Vnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn",len(df))

                # def add_space_in_dot(names):
                #     name = str(names)
                #     if "." in name:
                #         name = name.replace(".", " ")
                #         return name
                #     else:
                #         return name
                #
                # df['Names'] = df['Names'].apply(add_space_in_dot)
                #
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
                #
                #                 def replace_m(word):
                #                     def replace(match):
                #                         return re.sub(r'(?<!^)M(?!$)', 'n', match.group())
                #
                #                     return re.sub(r'\b\w+\b', replace, word)
                #
                #                 # Example usage:
                #                 word = mod
                #                 result = replace_m(word)
                #                 return result
                #             else:
                #                 return mod
                #     return word
                #
                # df['Names'] = df['Names'].apply(is_telugu_word)
                # #
                # def extract_alphabets_and_spaces(values):
                #     value = str(values)
                #     return re.sub(r'[^a-zA-Z\s]', '', value)
                #
                # df['Names'] = df['Names'].apply(extract_alphabets_and_spaces)
                # #
                # df['Names'] = df['Names'].str.strip()
                # df['Names'] = df['Names'].str.title()
                # df = df[df["Names"].str.strip() != ""]
                df["Mobile"] = df["Mobile"].astype(int)
                df.drop_duplicates(subset=["Mobile"],inplace=True)
                df = df[["Mobile"]]
                cdf = pd.concat([cdf,df],ignore_index=True)
                print("Tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt",len(df))

                # df.to_excel(f'/home/rajashekar/Desktop/M_B_S_C/Siddipet_Schemes/With_Mobile_Numbers/{fil}_cleaned.xlsx',index = False)
                # df.to_excel(f'/home/rajashekar/Desktop/M_B_S_C/Siddipet_Schemes/{fil}_cleaned.xlsx',index = False)

                    # df = pd.concat([df, df], axis=0, ignore_index=True)
            else:
                pass
            if file.endswith('.csv'):
                print("fileeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",file)
                df = pd.read_csv(file_path + '/' + folder + '/' + file, low_memory=False)
                print(df.columns)

                if 'Mobile' in df.columns:
                    print(df)
                    print("OLllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll",len(df))

                    df.dropna(subset=["Names"], inplace=True)
                    df.dropna(subset=["Mobile"], inplace=True)
                    print("A_D_Nllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll",len(df))

                    def clean_mobile_number(mobile):
                        try:
                            mobile_float = float(mobile)
                            mobile = "{:.0f}".format(mobile_float)
                        except ValueError:
                            mobile = str(mobile)

                        if mobile.endswith(".0"):
                            mobile = mobile[:-2]

                        return mobile

                    # Assuming df is your DataFrame
                    df['Mobile'] = df['Mobile'].apply(clean_mobile_number)

                    df['Mobile'] = df['Mobile'].astype('str')
                    df = df[df['Mobile'].str.isdigit()]
                    df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
                    df['Mobile'] = df['Mobile'].apply(
                        lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
                    df = df[df["Mobile"].notna()]  # Remove rows where Mobile is None
                    # print("A_M_Vnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn",len(df))
                    # def add_space_in_dot(names):
                    #     name = str(names)
                    #     if "." in name:
                    #         name = name.replace(".", " ")
                    #         return name
                    #     else:
                    #         return name
                    # df['Names'] = df['Names'].apply(add_space_in_dot)
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
                    #
                    #                 def replace_m(word):
                    #                     def replace(match):
                    #                         return re.sub(r'(?<!^)M(?!$)', 'n', match.group())
                    #
                    #                     return re.sub(r'\b\w+\b', replace, word)
                    #
                    #                 # Example usage:
                    #                 word = mod
                    #                 result = replace_m(word)
                    #                 return result
                    #             else:
                    #                 return mod
                    #     return word
                    # df['Names'] = df['Names'].apply(is_telugu_word)
                    # #
                    # def extract_alphabets_and_spaces(values):
                    #     value = str(values)
                    #     return re.sub(r'[^a-zA-Z\s]', '', value)
                    #
                    # df['Names'] = df['Names'].apply(extract_alphabets_and_spaces)
                    # #
                    # df['Names'] = df['Names'].str.strip()
                    # df['Names'] = df['Names'].str.title()
                    # df = df[df["Names"].str.strip() != ""]
                    df["Mobile"] = df["Mobile"].astype(int)
                    df.drop_duplicates(subset=["Mobile"], inplace=True)
                    df = df[["Mobile"]]
                    cdf = pd.concat([cdf,df],ignore_index=True)
                    print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",len(df))
                    print(df)

                    # df.to_excel(f'/home/rajashekar/Desktop/M_B_S_C/Siddipet_Schemes/With_Mobile_Numbers/{fil}_cleaned.xlsx', index=False)
                    # df.to_excel(f'/home/rajashekar/Desktop/M_B_S_C/Siddipet_Schemes/{fil}_cleaned.xlsx', index=False)
                else :
                    pass
        cdf.drop_duplicates(subset=["Mobile"],inplace = True)
        cdf.to_excel(f'/home/rajashekar/Desktop/MHB_Be_Sc_Mbs/{fol}.xlsx',index=False)


                    # def add_space_in_dot(names):
                    #     name = str(names)
                    #     if "." in name:
                    #         name = name.replace(".", " ")
                    #         return name
                    #     else:
                    #         return name
                    #
                    # df['Names'] = df['Names'].apply(add_space_in_dot)
                    #
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
                    #
                    #                 def replace_m(word):
                    #                     def replace(match):
                    #                         return re.sub(r'(?<!^)M(?!$)', 'n', match.group())
                    #
                    #                     return re.sub(r'\b\w+\b', replace, word)
                    #
                    #                 # Example usage:
                    #                 word = mod
                    #                 result = replace_m(word)
                    #                 return result
                    #             else:
                    #                 return mod
                    #     return word
                    #
                    #
                    # df['Names'] = df['Names'].apply(is_telugu_word)
                    #
                    # #
                    # def extract_alphabets_and_spaces(values):
                    #     value = str(values)
                    #     return re.sub(r'[^a-zA-Z\s]', '', value)
                    #
                    # df['Names'] = df['Names'].apply(extract_alphabets_and_spaces)
                    # df.dropna(subset=["Names"],inplace=True)
                    # #
                    # df['Names'] = df['Names'].str.strip()
                    # df['Names'] = df['Names'].str.title()
                    # df = df[df["Names"].str.strip() != ""]
                    # print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",len(df))
                    # df.to_excel(f'/home/rajashekar/Desktop/M_B_S_C/Siddipet_Schemes/Without_Mobile_Numbers/{fil}_cleaned.xlsx', index=False)
                    # df.to_excel(f'/home/rajashekar/Desktop/M_B_S_C/Siddipet_Schemes/{fil}_cleaned.xlsx', index=False)
#
# end_time = time.time()
# print(end_time-start_time)

for i in all_folders:
    print(i)