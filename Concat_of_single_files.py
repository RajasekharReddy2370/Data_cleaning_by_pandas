import pandas as pd
import re
# Constituency = "Penamaluru"

df1 = pd.read_excel(r"/home/rajashekar/Desktop/Andhra_State_Daily_data/Machilipatnam/Machilipatnam_18_25/voter_18_25/Z_concat_18_25_Age_group.xlsx",usecols=["Mobile"])
df2 = pd.read_excel(r"/home/rajashekar/Desktop/Andhra_State_Daily_data/Machilipatnam/Machilipatnam_18_25/import_data3/Z_concat_18_25_Age_group.xlsx",usecols=["Mobile"])
df3 = pd.read_excel(r"/home/rajashekar/Desktop/Andhra_State_Daily_data/Machilipatnam/Machilipatnam_18_25/import_data2/Z_Concat.xlsx",usecols=["Mobile"])
# df4 = pd.read_excel(r"/home/rajashekar/Documents/FESTIVALS_DATA/UGADI_CAMPAINING_DATA/MALKAJGIRI/MALKAJGIRI_MOBILE_NUMBERS/MALKAJGIRI_UGADI_MOBILE_NUMBERS_part_2.xlsx",usecols=["Mobile"])
# df5 = pd.read_excel(r"/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Medak/SERP_Employees_all_data_MPC_cleaned.xlsx",usecols=["Mobile"])

# df = pd.concat([df1,df2,df3,df4,df5],ignore_index=True)
# df = pd.concat([df1,df2],ignore_index=True)
df = pd.concat([df1,df2,df3],ignore_index=True)
# df = pd.concat([df1,df2,df3,df4],ignore_index=True)
print(len(df1))
print(len(df2))
print(len(df3))
# print(len(df4))
# print(len(df5))
df.drop_duplicates(subset=["Mobile"],inplace=True)

print(len(df))

df.to_excel("Machilipatnam_18_25_Age_Group.xlsx",index = False)


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
# def extract_alphabets_and_spaces(values):
#     value = str(values)
#     return re.sub(r'[^a-zA-Z\s]', '', value)
#
# df['Names'] = df['Names'].apply(extract_alphabets_and_spaces)


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
# df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
#
# df['Mobile'] = df['Mobile'].astype('str')
# df = df[df['Mobile'].str.isdigit()]
# df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
# df['Mobile'] = df['Mobile'].apply(
#     lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
df = df[df["Mobile"].notna()]  # Remove rows where Mobile is None
# df = df[df["Names"].notna()]  # Remove rows where Mobile is None

# df.dropna(subset=["Names"],inplace=True)
# df.dropna(subset=["Mobile"],inplace=True)

# df["Names"] = df["Names"].astype(str)
# df["Names"] = df["Names"].str.strip()
# df["Names"] = df["Names"].str.title()
# df = df[df["Mobile"].str.strip() != ""]

print(df)
print(len(df))
# df.to_excel("Avanigadda_Names_Mobile_Numbers.xlsx",index = False)

# df.drop_duplicates(subset=["Mobile"],inplace=True)

print(len(df))

# df.to_excel(f"/home/rajashekar/Desktop/MACHILIPATNAM/Machilipatnam_Total_Mp_35_70_Age_Group.xlsx",index = False)




# df["Names"] = df["Names"].astype(str)
# df["Names"] = df["Names"].str.strip()
# df["Names"] = df["Names"].str.title()
# df["Telugu_Names"] = df["Telugu_Names"].astype(str)
# df["Telugu_Names"] = df["Telugu_Names"].str.strip()
# df["Mobile"] = df["Mobile"].astype(int)

# df.dropna(subset=["Mobile"],inplace=True)
# # df.drop_duplicates(subset=["Names","Mobile"],inplace=True)
# df.drop_duplicates(subset=["Mobile"],inplace=True)
# df.dropna(subset=["Mobile"],inplace=True)
#
# print(len(df))
# print(df)
# df.to_excel("/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Machilipatnam_imported_Data/Machilipatnam_each_constituency_unique/Penamaluru_unique_Mobile_Numbers.xlsx",index = False)
# df.to_excel(f"/home/rajashekar/Desktop/ALL_MP_DATA_UNIQUE_MOBILE_NUMBERS_TS/UPDATED/{constituency}_Total_Mp_Mobile_Numbers.xlsx",index = False)
# df.to_excel("/home/rajashekar/Documents/Guntur_West_Tuesday_imported_Data/Concatenated_Data/unmatched_Mobiles/concat_unmatched.xlsx",index = False)
# l = len(df)
# # print("After droping of duplicate rows",l)
# if l > 1000000:
#     first_part = df.iloc[:1000000, :]
#     second_part = df.iloc[1000001:, :]
#
#     first_file_path = f"/home/rajashekar/Desktop/TS_CPU/Total_State_Mobile_Numbers/Malkajgiri/{constituency}_Total_Mp_Mobile_Numbers_Part1_updated.xlsx"
#     first_part.to_excel(first_file_path, index=False)
#
#     print("............................................first_part")
#
#     second_file_path = f"/home/rajashekar/Desktop/TS_CPU/Total_State_Mobile_Numbers/Malkajgiri/{constituency}_Total_Mp_Mobile_Numbers_Part2_updated.xlsx"
#     second_part.to_excel(second_file_path, index=False)
#     print("............................................second_part")
# else:
#     file_path = f"/home/rajashekar/Desktop/TS_CPU/Total_State_Mobile_Numbers/Malkajgiri/{constituency}_Total_Mp_Mobile_Numbers_updated.xlsx"
#     df.to_excel(file_path, index=False)
#     print("*******************************************original file stored successfully")



