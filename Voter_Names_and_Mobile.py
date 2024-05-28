import pandas as pd
import re
import os
from indic_transliteration import sanscript

main_folder_path = "/home/rajashekar/Desktop/TS_CPU/Voter_MP_Data/Mahbubnagar_74"
files = os.listdir(main_folder_path)

cdf = pd.DataFrame()
for file in files:
    print(file)
    fil = file.split('-')[0]
    acno = file.split('-')[1]
    df = pd.read_excel(main_folder_path+'/'+file)
    print(df.columns)

    new_df = df.copy()

    new_df = df.loc[:, ['B#',"First Name", "Last Name", 'Mobile']]
    print(new_df)

    new_df["Last Name"] = new_df["Last Name"].fillna('')
    new_df["First Name"] = new_df["First Name"].astype(str)
    new_df["Last Name"] = new_df["Last Name"].astype(str)
    new_df["First Name"] = new_df["First Name"].str.strip()
    new_df["Last Name"] = new_df["Last Name"].str.strip()
    new_df['Names'] = new_df["First Name"] + ' ' + new_df["Last Name"]

    new_df["Names"] = new_df["Names"].str.lower()

    def add_space_in_dot(name):
        if "." in name:
            name = name.replace(".", " ")
            return name
        else:
            return name

    new_df['Names'] = new_df['Names'].apply(add_space_in_dot)

    def extract_alphabets_and_spaces(values):
        value = str(values)
        return re.sub(r'[^a-zA-Z\s]', '', value)
    new_df['Names'] = new_df['Names'].apply(extract_alphabets_and_spaces)

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

    new_df['Mobile'] = new_df['Mobile'].apply(clean_mobile_number)

    new_df['Mobile'] = new_df['Mobile'].astype('str')
    new_df = new_df[new_df['Mobile'].str.isdigit()]
    new_df['Mobile'] = new_df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
    new_df['Mobile'] = new_df['Mobile'].apply(
        lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
    new_df = new_df[new_df["Mobile"].notna()]  # Remove rows where Mobile is None

    DFs = new_df[['B#',"Names", "Mobile"]]
    DFs["Names"] = DFs["Names"].astype(str)
    DFs["Names"] = DFs["Names"].str.strip()
    DFs["Names"] = DFs["Names"].str.title()
    DFs.dropna(subset=["Names"], inplace=True)
    DFs.dropna(subset=["Mobile"], inplace=True)
    DFs.dropna(inplace=True)
    DFs.drop_duplicates(subset = ["Names","Mobile"],inplace = True)
    DFs.drop_duplicates(subset = ["Mobile"],inplace = True)
    # DF["Mobile"] = DF["Mobile"].astype(int)

    DFs['AC_No'] = acno
    DFs = DFs[['AC_No','B#','Names','Mobile']]
    print(DFs)
    # break
    cdf = pd.concat([cdf,DFs],ignore_index=True)
    DFs.to_excel(f"/home/rajashekar/Documents/Mahbubnagar_Nayak_STs_Datawith_Booth_and_Assembly_Number/{fil}.xlsx",index = False)
    print("Success")

    # DF.to_excel(f"", index=False)
cdf.dropna(inplace=True)
cdf.drop_duplicates(subset = ["Names","Mobile"],inplace=True)
cdf.drop_duplicates(subset = ["Mobile"],inplace=True)
cdf = cdf[['AC_No', 'B#', 'Names', 'Mobile']]
print(cdf)
#
cdf.dropna(inplace=True)
cdf.to_excel(f"/home/rajashekar/Documents/Mahbubnagar_Nayak_STs_Datawith_Booth_and_Assembly_Number/Mahbubnagr_concat_Data.xlsx",index = False)
print('completed')




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
# DF = new_df[["Names","Mobile"]]
# DF["Names"] = DF["Names"].astype(str)
# DF["Names"] = DF["Names"].str.strip()
# DF["Names"] = DF["Names"].str.title()
# DF["Mobile"] = DF["Mobile"].astype(int)
# DF.dropna(subset = ["Names"],inplace = True)
# DF.dropna(subset = ["Mobile"],inplace = True)
# DF.dropna(inplace = True)
#
# DF.to_excel(f"",index = False)

