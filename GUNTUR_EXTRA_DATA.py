import pandas as pd
import re
import os
from indic_transliteration import sanscript
#
# file_name = "RK_anna_Contacts_1"
#
# df = pd.read_excel("/home/rajashekar/Desktop/AP_CPU/GUNTUR_EXTRA_DATA/RK anna Contacts.xls",header = 0,usecols=["Display Name","Mobile Phone"])
#
# print(df.columns)
# df.rename(columns={"Display Name": "Names", "Mobile Phone": "Mobile"}, inplace=True)
# print(df)
#
# df.dropna(inplace=True)
# df["Names"] = df["Names"].astype(str)
# df["Names"] = df["Names"].str.strip()
# def replace_dot_withspace(name):
#     if "." in name:
#         name = name.replace(".", " ")
#     return name
#
# df["Names"] = df["Names"].apply(replace_dot_withspace)
#
# def extract_alphabets_and_spaces(values):
#     value = str(values)
#     return re.sub(r'[^a-zA-Z\s]', '', value)
#
# df['Names'] = df['Names'].apply(extract_alphabets_and_spaces)
#
# df['Names'] = df['Names'].str.strip()
# df = df[df["Names"].str.strip() != ""]
#
# def clean_mobile_number(mobile):
#     # Convert scientific notation to normal form
#     if 'e' in str(mobile):
#         mobile = "{:.0f}".format(mobile)
#     # Remove ".0" if it exists at the end
#     mobile_str = str(mobile)
#     if mobile_str.endswith('.0'):
#         mobile = mobile_str[:-2]
#     return mobile
#
# df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
# df['Mobile'] = df['Mobile'].astype(str)
# df = df[df['Mobile'].str.isdigit()]
# df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
# df['Mobile'] = df['Mobile'].apply(lambda x: x if x and x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
# df.dropna(inplace=True)
# df.drop_duplicates(subset=["Mobile"], inplace=True)
# df["Mobile"] = df["Mobile"].astype(int)
#
# df = df[["Names", "Mobile"]]
# print(df)
# df.to_excel(f"/home/rajashekar/Desktop/AP_CPU/GUNTUR_EXTRA_DATA_CLEANED/{file_name}_cleaned.xlsx", index=False)

################################### CONCAT OF ALL FILES ######################################################

#
# main_file_path = "/home/rajashekar/Desktop/AP_CPU/GUNTUR_EXTRA_DATA_CLEANED"
# file_name = "GUNTUR_EXTRA_DATA_ALL_FILES"
# files = os.listdir(main_file_path)
# result_df = pd.DataFrame()
# c = 0
# for file in files:
#     c = c+1
#     print(file,c)
#     df = pd.read_excel(main_file_path+'/'+file)
#
#     result_df = pd.concat([result_df,df],ignore_index=True)
# print(len(result_df))
#
# result_df.drop_duplicates(subset=["Mobile"],inplace=True)
# print(result_df)
# # result_df.to_excel("GUNTUR_EXTRA_DATA_ALL_FILES.xlsx",index=False)
# result_df.to_excel(f"/home/rajashekar/Desktop/AP_CPU/GUNTUR_EXTRA_DATA_CLEANED/{file_name}_CLEANED.xlsx", index=False)


#################################### CONCAT OF MAIN FILE AND EXTRA_DATA_FILE #######################################

# file_name = "Rk_ANNA_CONCATS"
# df1 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/STP_DATA/sattenapalli_Raw_data_Cleaned.xlsx")
# print(len(df1))
# df2 = pd.read_excel(r"SATTENAPALLI_VOTER_UPDATED_DATA1.xlsx")
# print(len(df2))
# df = pd.concat([df1,df2],ignore_index=True)
#
# # df = df[["Names","Mobile"]]
# df = df[["Names","Telugu_Names","Mobile"]]
# df.drop_duplicates(subset=["Mobile"],inplace = True)
# df.dropna(inplace=True)
# print(df)
# df.to_excel("SATP_DATA.xlsx",index=False)
# df.to_excel(f"/home/rajashekar/Desktop/AP_CPU/GUNTUR_EXTRA_DATA_CLEANED/{file_name}_CLEANED.xlsx", index=False)

########################################## LANGUAGE_CONVERSION #########################################################


# df = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/GUNTUR_EXTRA_DATA_CLEANED/GUNTUR_EXTRA_DATA_ALL_FILES_CLEANED.xlsx")
#
# def add_space_in_dot(name):
#     if "." in name:
#         name = name.replace("."," ")
#         return name
#     else:
#         return name
# df['Names'] = df['Names'].apply(add_space_in_dot)
#
# def extract_alphabets_and_spaces(values):
#     value = str(values)
#     return re.sub(r'[^a-zA-Z\s]', '', value)
# # Apply the function to the "name" column
# df['Telugu_Names'] = df['Names'].apply(extract_alphabets_and_spaces)
# df["Telugu_Names"]=df["Telugu_Names"].astype(str)
# df["Telugu_Names"]=df["Telugu_Names"].str.lower()
# def replace_z_with_s_q_with_k(input_string):
#     # Replace both 'Z' and 'z' with 'S' and 's', respectively
#     output_string = input_string.replace('z', 'j').replace('q', 'k')
#     return output_string
# df['Telugu_Names'] = df['Telugu_Names'].apply(replace_z_with_s_q_with_k)
#
# def add_ph_in_f(name):
#     if "f" in name:
#         name = name.replace("f","ph")
#         return name
#     else:
#         return name
# df['Telugu_Names'] = df['Telugu_Names'].apply(add_ph_in_f)
# df['Telugu_Names'] = df['Telugu_Names'].astype(str)
# df['Telugu_Names'] = df['Telugu_Names'].str.lower()
# # Function to transliterate English names to Telugu script
# def transliterate_to_telugu(name):
#     telugu_name = sanscript.transliterate(name, sanscript.ITRANS, sanscript.TELUGU)
#     return telugu_name
# # Apply the transliteration function to the 'Names' column and create a new 'Telugu_Names' column
# df['Telugu_Names'] = df['Telugu_Names'].apply(transliterate_to_telugu)
#
# df = df[["Names","Telugu_Names","Mobile"]]
# print(df)
#
# df.to_excel("GUNTUR_EXTRA_DATA_CONVERSION.xlsx",index = False)