import pandas as pd
import re
import os
from indic_transliteration import sanscript

main_folder_path = "/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Machilipatnam_imported_Data/constituencies_To_be_cleaned/new_data_1"
# MP_Constituency = main_folder_path.split('/')[-1]

files = os.listdir(main_folder_path)

cdf = pd.DataFrame()
for file in files:
    fil = file.split('.xlsx')[0]
    df = pd.read_excel(main_folder_path+'/'+file,usecols=["Mobile"])

    print(df.columns)
    # print(df.info())
    df.dropna(subset = ["Mobile"],inplace = True)
    dfm = df[['Mobile']].copy()

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

    dfm['Mobile'] = dfm['Mobile'].apply(clean_mobile_number)

    dfm['Mobile'] = dfm['Mobile'].astype(str)
    dfm = dfm[dfm['Mobile'].str.isdigit()]
    dfm['Mobile'] = dfm['Mobile'].apply(lambda x: x[3:] if len(x) > 10 and x.startswith('+91') else x)
    # print(len(df))
    dfm['Mobile'] = dfm['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
    # print(len(df))
    dfm['Mobile'] = dfm['Mobile'].apply(lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
    dfm = dfm[dfm["Mobile"].notna()]

    # df = df[["Names", "Mobile"]]
    # dfm["Mobile"] = dfm["Mobile"].astype(int)
    dfm.dropna(subset=["Mobile"], inplace=True)
    dfm.to_excel(f"/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Machilipatnam_imported_Data/constituencies_To_be_cleaned/new_data1_with_duplicates/{fil}_Mobile_Numbers_cleaned.xlsx", index=False)


    dfm.drop_duplicates(subset = ["Mobile"],inplace = True)
    dfms = dfm[["Mobile"]].copy()

    print(len(dfms))
    print(fil,"CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC",len(dfms))
    dfms.to_excel(f"/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Machilipatnam_imported_Data/constituencies_To_be_cleaned/new_data1_without_duplicates/{fil}_Mobile_Numbers_cleaned.xlsx", index=False)

    cdf = pd.concat([cdf,dfms],ignore_index=True)
#
cdf.dropna(inplace=True)
cdf.to_excel(f"/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Machilipatnam_imported_Data/constituencies_To_be_cleaned/newdata1_concat/with_duplicates/new_data_concat_with_duplicates.xlsx",index=False)


cdf.drop_duplicates(subset = ["Mobile"],inplace=True)
cdf.dropna(subset=["Mobile"],inplace=True)
print("MP_MOBILE_NUMBERSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",len(cdf))
cdf.to_excel(f"/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Machilipatnam_imported_Data/constituencies_To_be_cleaned/newdata1_concat/without_duplicates/new_data_concat_without_duplicates.xlsx",index=False)


# l = len(cdf)
# if l > 1000000:
#     first_part = cdf.iloc[:1000000, :]
#     second_part = cdf.iloc[1000001:, :]
#
#     first_file_path = f"/home/rajashekar/Desktop/AP_CPU/MOBILE_NUMBERS/MP/Anantapur/{MP_Constituency}_voter_Mp_Mobile_Numbers_part1_cleaned.xlsx"
#     first_part.to_excel(first_file_path, index=False)
#
#     print("............................................first_part")
#
#     second_file_path = f"/home/rajashekar/Desktop/AP_CPU/MOBILE_NUMBERS/MP/Anantapur/{MP_Constituency}_voter_Mp_Mobile_Numbers_part2_cleaned.xlsx"
#     second_part.to_excel(second_file_path, index=False)
#     print("............................................second_part")
# else:
#     file_path = f"/home/rajashekar/Desktop/AP_CPU/MOBILE_NUMBERS/MP/Anantapur/{MP_Constituency}_voter_Mp_Mobile_Numbers_cleaned.xlsx"
#     cdf.to_excel(file_path, index=False)

# cdf.to_excel(f"/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/VOTER/Medak_Mp_Voter_Mobile_Numbers.xlsx",index = False)

################################### FOR SINGLE FILE ####################################################################

#
# df = pd.read_excel(r"/home/rajashekar/Downloads/Guntur_west_85_PWD_cleaned.xlsx")
# print(df.columns)
# print(df.info())
#
# new_df = df.copy()
#
# new_df = df.loc[:,["First Name", "Last Name", 'Voter ID','Mobile']]
#
# print(new_df)
# new_df["Last Name"] = new_df["Last Name"].fillna('')
# new_df["First Name"] = new_df["First Name"].astype(str)
# new_df["Last Name"] = new_df["Last Name"].astype(str)
# new_df["First Name"] = new_df["First Name"].str.strip()
# new_df["Last Name"] = new_df["Last Name"].str.strip()
# new_df['Names'] = new_df["First Name"] + ' ' + new_df["Last Name"]
#
# new_df["Names"] = new_df["Names"].str.lower()
#
# def add_space_in_dot(name):
#     if "." in name:
#         name = name.replace(".", " ")
#         return name
#     else:
#         return name
#
# new_df['Names'] = new_df['Names'].apply(add_space_in_dot)
#
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
# new_df['Names'] = new_df['Names'].apply(is_telugu_word)
#
#
# def extract_alphabets_and_spaces(values):
#     value = str(values)
#     return re.sub(r'[^a-zA-Z\s]', '', value)
#
# new_df['Names'] = new_df['Names'].apply(extract_alphabets_and_spaces)
#
#
# def clean_mobile_number(mobile):
#     # Try to convert mobile to float to handle scientific notation and remove decimals
#     try:
#         mobile_float = float(mobile)
#         # Convert scientific notation to normal form and remove ".0" if it exists
#         mobile = "{:.0f}".format(mobile_float)
#     except ValueError:
#         # If conversion fails, it's likely already a string that doesn't need conversion
#         mobile = str(mobile)
#
#     # Remove any trailing ".0"
#     if mobile.endswith(".0"):
#         mobile = mobile[:-2]
#
#     return mobile
#
# new_df['Mobile'] = new_df['Mobile'].apply(clean_mobile_number)
#
# df = new_df[["Names","Mobile"]]
# df["Names"] = df["Names"].astype(str)
# df["Names"] = df["Names"].str.strip()
# df["Names"] = df["Names"].str.title()
# df["Mobile"] = df["Mobile"].astype(int)
# df.dropna(subset = ["Names"],inplace = True)
# df.dropna(subset = ["Mobile"],inplace = True)
# df.dropna(inplace = True)
#
# df.to_excel(f"",index = False)

