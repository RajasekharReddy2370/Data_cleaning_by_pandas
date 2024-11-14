# import os
# from indic_transliteration import sanscript
# import pandas as pd
# import re
# import time
#
# start_time = time.time()
#
# file_path = r"/home/rajashekar/Desktop/RAJA_LAPTOP/Telangana/TELANGANA/TELANGANA_MOBILE_NUMBERS_from_Drive_data_and_schemes/Beneficiary_Data_All_schemes"
# all_folders = os.listdir(file_path)
# constituency_lengths_Name_Mobile = {}
# c = 0
# for folder in all_folders:
#     c += 1
#     print('folder...............................................................................',folder)
#     if folder == 'Achampet_82':
#         constituency = folder.split('_')[0]
#
#         all_files_in_folder = os.listdir(file_path+'/'+folder)
#         # print(len(all_files_phone_nums))
#         result_df = pd.DataFrame()
#         for file in all_files_in_folder:
#             fil = file.split('.xlsx')[0]
#             if file.endswith('.xlsx') :
#                 df = pd.read_excel(file_path + '/' + folder + '/' + file)
#
#                 df.dropna(subset=["Names"],inplace=True)
#                 df.dropna(subset=["Mobile"],inplace=True)
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
#
#                 def add_space_in_dot(names):
#                     name = str(names)
#                     if "." in name:
#                         name = name.replace(".", " ")
#                         return name
#                     else:
#                         return name
#
#                 df['Names'] = df['Names'].apply(add_space_in_dot)
#
#                 def is_telugu_word(word):
#                     telugu_range = range(0x0C00, 0x0C7F)
#                     for char in str(word):
#                         if ord(char) in telugu_range:
#                             mod = sanscript.transliterate(word, sanscript.TELUGU, sanscript.HK)
#                             if 'Ò' or 'È' in mod:
#                                 mod = ''.join(['O' if letter == 'Ò' else letter for letter in mod])
#                                 mod = ''.join(['E' if letter == 'È' else letter for letter in mod])
#                                 mod = ''.join(['e' if letter == 'è' else letter for letter in mod])
#                                 mod = ''.join(['o' if letter == 'ò' else letter for letter in mod])
#                                 mod = ''.join(['S' if letter == 'Z' else letter for letter in mod])
#                                 mod = ''.join(['s' if letter == 'z' else letter for letter in mod])
#                                 mod = ''.join(['ch' if letter == 'c' else letter for letter in mod])
#
#                                 def replace_m(word):
#                                     def replace(match):
#                                         return re.sub(r'(?<!^)M(?!$)', 'n', match.group())
#
#                                     return re.sub(r'\b\w+\b', replace, word)
#
#                                 # Example usage:
#                                 word = mod
#                                 result = replace_m(word)
#                                 return result
#                             else:
#                                 return mod
#                     return word
#
#                 df['Names'] = df['Names'].apply(is_telugu_word)
#                 #
#                 def extract_alphabets_and_spaces(values):
#                     value = str(values)
#                     return re.sub(r'[^a-zA-Z\s]', '', value)
#
#                 df['Names'] = df['Names'].apply(extract_alphabets_and_spaces)
#                 #
#                 df['Names'] = df['Names'].str.strip()
#                 df['Names'] = df['Names'].str.title()
#                 df = df[df["Names"].str.strip() != ""]
#                 df["Mobile"] = df["Mobile"].astype(int)
#                 df = df[["Names", 'Mobile']]
#                 df.drop_duplicates(subset=["Names","Mobile"],inplace=True)
#
#                 result_df = pd.concat([result_df, df], axis=0, ignore_index=True)
#
#             elif file.endswith('.csv'):
#
#                 print("fileeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",file)
#                 df = pd.read_csv(file_path + '/' + folder + '/' + file, low_memory=False)
#                 df.columns = df.columns.str.strip()
#
#                 if 'Mobile' in df.columns and 'Names' in df.columns:
#                     print(f"'Mobile' and 'Names' columns found in {file}")
#
#                 # Drop rows with missing 'Names' or 'Mobile'
#                     df.dropna(subset=['Names', 'Mobile'], inplace=True)
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
#                     def add_space_in_dot(names):
#                         name = str(names)
#                         if "." in name:
#                             name = name.replace(".", " ")
#                             return name
#                         else:
#                             return name
#                     df['Names'] = df['Names'].apply(add_space_in_dot)
#                     def is_telugu_word(word):
#                         telugu_range = range(0x0C00, 0x0C7F)
#                         for char in str(word):
#                             if ord(char) in telugu_range:
#                                 mod = sanscript.transliterate(word, sanscript.TELUGU, sanscript.HK)
#                                 if 'Ò' or 'È' in mod:
#                                     mod = ''.join(['O' if letter == 'Ò' else letter for letter in mod])
#                                     mod = ''.join(['E' if letter == 'È' else letter for letter in mod])
#                                     mod = ''.join(['e' if letter == 'è' else letter for letter in mod])
#                                     mod = ''.join(['o' if letter == 'ò' else letter for letter in mod])
#                                     mod = ''.join(['S' if letter == 'Z' else letter for letter in mod])
#                                     mod = ''.join(['s' if letter == 'z' else letter for letter in mod])
#                                     mod = ''.join(['ch' if letter == 'c' else letter for letter in mod])
#
#                                     def replace_m(word):
#                                         def replace(match):
#                                             return re.sub(r'(?<!^)M(?!$)', 'n', match.group())
#
#                                         return re.sub(r'\b\w+\b', replace, word)
#
#                                     # Example usage:
#                                     word = mod
#                                     result = replace_m(word)
#                                     return result
#                                 else:
#                                     return mod
#                         return word
#                     df['Names'] = df['Names'].apply(is_telugu_word)
#                     #
#                     def extract_alphabets_and_spaces(values):
#                         value = str(values)
#                         return re.sub(r'[^a-zA-Z\s]', '', value)
#
#                     df['Names'] = df['Names'].apply(extract_alphabets_and_spaces)
#                     #
#                     df['Names'] = df['Names'].str.strip()
#                     df['Names'] = df['Names'].str.title()
#                     df = df[df["Names"].str.strip() != ""]
#                     df["Mobile"] = df["Mobile"].astype(int)
#                     df = df[["Names",'Mobile']]
#                     df.drop_duplicates(subset=["Names","Mobile"], inplace=True)
#                     # df.drop_duplicates(subset=["Mobile"], inplace=True)
#                     result_df = pd.concat([result_df, df], axis=0, ignore_index=True)
#             else :
#                 pass
#
#         result_df.drop_duplicates(subset=['Names', 'Mobile'], inplace=True)
#         result_df.to_excel(f"/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/Names_Mobile/{constituency}.xlsx",index = False)
#         l = len(result_df)
#         print("*********************************************************After removal of duplicate rows",folder,len(result_df),c)
#         constituency_lengths_Name_Mobile[constituency] = l
# constituency_df_n_m = pd.DataFrame(list(constituency_lengths_Name_Mobile.items()),columns=['Constituency', 'Length'])
# constituency_df_n_m.to_excel(f"/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/constituency_lengths/Names_Mobile/Telangana_Beneficiary_Names_Mobile_constituency_lengths.xlsx",index = False)

#############################################################################################################################################################3


import os
import pandas as pd
import re
import time
from indic_transliteration import sanscript

# Start time
start_time = time.time()

# File path
file_path = r"/home/rajashekar/Desktop/RAJA_LAPTOP/Telangana/TELANGANA/TELANGANA_MOBILE_NUMBERS_from_Drive_data_and_schemes/Beneficiary_Data_All_schemes"
all_folders = os.listdir(file_path)
constituency_lengths_Name_Mobile = {}
c = 0
cdff = pd.DataFrame()
# Helper functions
def clean_mobile_number(mobile):
    """Clean the mobile number by removing decimals and handling prefixes."""
    try:
        mobile_float = float(mobile)
        mobile = "{:.0f}".format(mobile_float)
    except ValueError:
        mobile = str(mobile)

    if mobile.endswith(".0"):
        mobile = mobile[:-2]
    return mobile

def is_telugu_word(word):
    """Check if the word contains Telugu characters and transliterate."""
    telugu_range = range(0x0C00, 0x0C7F)
    for char in str(word):
        if ord(char) in telugu_range:
            mod = sanscript.transliterate(word, sanscript.TELUGU, sanscript.HK)
            replacements = {'Ò': 'O', 'È': 'E', 'è': 'e', 'ò': 'o', 'Z': 'S', 'z': 's', 'c': 'ch'}
            for key, value in replacements.items():
                mod = mod.replace(key, value)

            # Replace internal 'M' with 'n'
            mod = re.sub(r'(?<!^)M(?!$)', 'n', mod)
            return mod
    return word

def extract_alphabets_and_spaces(value):
    """Extract only alphabets and spaces from the given value."""
    return re.sub(r'[^a-zA-Z\s]', '', str(value))

def clean_name(name):
    """Clean the name by removing dots, transliterating, and formatting."""
    if "." in str(name):
        name = name.replace(".", " ")
    name = is_telugu_word(name)
    name = extract_alphabets_and_spaces(name).strip().title()
    return name if name else None

# Process folders
for folder in all_folders:
    c += 1
    print(f"Processing folder: {folder} ({c}/{len(all_folders)})")
    if folder != 'ts':
        constituency = folder.split('_')[0]
        all_files_in_folder = os.listdir(os.path.join(file_path, folder))
        result_df = pd.DataFrame()

        for file in all_files_in_folder:
            file_path_full = os.path.join(file_path, folder, file)
            if file.endswith('.xlsx') or file.endswith('.csv'):
                try:
                    if file.endswith('.xlsx'):
                        df = pd.read_excel(file_path_full)
                    elif file.endswith('.csv'):
                        df = pd.read_csv(file_path_full, low_memory=False)

                    # Standardize column names
                    df.columns = df.columns.str.strip()

                    # Check for required columns
                    if 'Mobile' not in df.columns or 'Names' not in df.columns:
                        # print(f"Skipping file {file} due to missing 'Mobile' or 'Names' columns.")
                        continue

                    # Clean data
                    df.dropna(subset=['Names', 'Mobile'], inplace=True)

                    # Clean Mobile column
                    df['Mobile'] = df['Mobile'].astype(str).str.strip()
                    df = df[df['Mobile'].notna() & (df['Mobile'] != '')]
                    df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
                    df = df[df['Mobile'].str.isdigit()]
                    df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
                    df['Mobile'] = df['Mobile'].apply(lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
                    df.dropna(subset=['Mobile'], inplace=True)

                    # Clean Names column
                    df['Names'] = df['Names'].apply(clean_name)
                    df.dropna(subset=['Names'], inplace=True)

                    # Final data selection
                    df['Mobile'] = df['Mobile'].astype(int)
                    df = df[['Names', 'Mobile']]
                    df.drop_duplicates(subset=['Names', 'Mobile'], inplace=True)

                    # Append to result DataFrame
                    result_df = pd.concat([result_df, df], ignore_index=True)

                except Exception as e:
                    print(f"Error processing file {file}: {e}")
                    continue

        # Save results for the constituency
        result_df.drop_duplicates(subset=['Names', 'Mobile'], inplace=True)
        cdff = pd.concat([cdff,result_df],ignore_index=True)

        output_path = f"/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/Names_Mobile/{constituency}.xlsx"
        result_df.to_excel(output_path, index=False)
        l = len(result_df)
        print(f"After duplicate removal: {folder}, Rows: {l}")
        constituency_lengths_Name_Mobile[constituency] = l

# Save constituency lengths
constituency_df_n_m = pd.DataFrame(list(constituency_lengths_Name_Mobile.items()), columns=['Constituency', 'Length'])
lengths_output_path = f"/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary/constituency_lengths/Names_Mobile/Telangana_Beneficiary_Names_Mobile_constituency_lengths.xlsx"
constituency_df_n_m.to_excel(lengths_output_path, index=False)

cdff.drop_duplicates(subset=["Mobile"],inplace = True)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@cdff",len(cdff))

# Print total time taken
end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")































