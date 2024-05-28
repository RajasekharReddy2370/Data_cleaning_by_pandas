import pandas as pd
import os
import re

main_file_path = "/home/rajashekar/Desktop/Andhra_State_Daily_data/Machilipatnam/Machilipatnam_18_25/import_data2"
files = os.listdir(main_file_path)


result_df = pd.DataFrame()
# constituency = main_file_path.split('/')[-1]
# constituency = "Medak"

c = 0
for file in files:
    # if "Arogya" in file and 'Sri' not in file:
    # if "lock" in file:
    #     continue
    # else:
    #     print(file)
#     fil = file.split('_')[0]
#     # f = file.split('-')[0]
#     # print(main_file_path+'/'+file)
#     c = c+1
#     # print(c)
    df = pd.read_excel(main_file_path+'/'+file,usecols=["Mobile"])
    df.drop_duplicates(subset=["Mobile"],inplace=True)
#     print(len(df))
    result_df = pd.concat([result_df,df],ignore_index=True)
#
#     # Filter rows where the length of 'Mobile' column is 10
#     # filtered_df = df[df['Mobile'].str.len() == 10]
#
#     # Print or further process the filtered DataFrame
#     # print(filtered_df)
#     # filtered_df.to_excel(f"")
#
# print(len(result_df))
#
result_df.drop_duplicates(subset=["Mobile"],inplace = True)
print(len(result_df))
result_df.to_excel("/home/rajashekar/Desktop/Andhra_State_Daily_data/Machilipatnam/Machilipatnam_18_25/import_data2/Z_Concat.xlsx",index = False)

#
#     df.dropna(subset = ["Names"],inplace = True)
#     df.dropna(subset = ["Telugu_Names"],inplace = True)
#     df.dropna(subset = ["Mobile"],inplace = True)
#
#     def add_space_in_dot(name):
#         if "." in name:
#             name = name.replace(".", " ")
#             return name
#         else:
#             return name
#
#     df['Names'] = df['Names'].apply(add_space_in_dot)
#
#     def extract_alphabets_and_spaces(values):
#         value = str(values)
#         return re.sub(r'[^a-zA-Z\s]', '', value)
#
#     df['Names'] = df['Names'].apply(extract_alphabets_and_spaces)
#
#
#     def clean_mobile_number(mobile):
#         try:
#             mobile_float = float(mobile)
#             mobile = "{:.0f}".format(mobile_float)
#         except ValueError:
#             mobile = str(mobile)
#
#         if mobile.endswith(".0"):
#             mobile = mobile[:-2]
#
#         return mobile
#
#
#     # Assuming df is your DataFrame
#     df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
#
#     df['Mobile'] = df['Mobile'].astype('str')
#     df = df[df['Mobile'].str.isdigit()]
#     df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
#     df['Mobile'] = df['Mobile'].apply(
#         lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
#
#     # df = df[df["Mobile"].notna()]  # Remove rows where Mobile is None
#
#     print(c,len(df))
#     df.drop_duplicates(subset=["Mobile"],inplace = True)
#     df.to_excel(f"/home/rajashekar/Desktop/TS_CPU/TELANGANA_MP_EACH_CONSTITUENCY_VERIFIED_DATA/Medak/Medak_verified/{fil}_mobile_numbers_verified.xlsx",index = False)
#
#     result_df = pd.concat([result_df, df], axis=0, ignore_index=True)
#
# print("Concat_length..................",len(result_df))
#
# def clean_mobile_number(mobile):
#     try:
#         mobile_float = float(mobile)
#         mobile = "{:.0f}".format(mobile_float)
#     except ValueError:
#         mobile = str(mobile)
#
#     if mobile.endswith(".0"):
#         mobile = mobile[:-2]
#
#     return mobile
#
# # Assuming df is your DataFrame
# result_df['Mobile'] = result_df['Mobile'].apply(clean_mobile_number)
#
# result_df['Mobile'] = result_df['Mobile'].astype('str')
# result_df = result_df[result_df['Mobile'].str.isdigit()]
# result_df['Mobile'] = result_df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
# result_df['Mobile'] = result_df['Mobile'].apply(lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
#
# result_df = result_df[result_df["Mobile"].notna()]  # Remove rows where Mobile is None
#
# result_df["Mobile"] = result_df["Mobile"].astype(int)
#
# result_df.drop_duplicates(subset = ["Mobile"],inplace = True)
# # result_df.drop_duplicates(subset=["Names","Mobile"],inplace=True)
# result_df.drop_duplicates(subset=["Mobile"],inplace=True)
# # result_df.dropna(subset=["Mobile"],inplace=True)
#
# result_df["Names"] = result_df["Names"].astype(str)
# result_df["Names"] = result_df["Names"].str.strip()
# result_df["Names"] = result_df["Names"].str.title()
# result_df["Telugu_Names"] = result_df["Telugu_Names"].astype(str)
# result_df["Telugu_Names"] = result_df["Telugu_Names"].str.strip()
# result_df["Mobile"] = result_df["Mobile"].astype(int)
#
#
# print(result_df)
# print(len(result_df))
#
# l = len(result_df)
# # print("After droping of duplicate rows",l)
# if l > 1000000:
#     first_part = result_df.iloc[:1000000, :]
#     second_part = result_df.iloc[1000001:, :]
#
#     first_file_path = f"/home/rajashekar/Desktop/TS_CPU/TELANGANA_MP_EACH_CONSTITUENCY_VERIFIED_DATA/Medak/Medak_Mp_Concat/{constituency}_MP_Mobile_Numbers_part1_cleaned.xlsx"
#     first_part.to_excel(first_file_path, index=False)
#
#     print("............................................first_part")
#
#     second_file_path = f"/home/rajashekar/Desktop/TS_CPU/TELANGANA_MP_EACH_CONSTITUENCY_VERIFIED_DATA/Medak/Medak_Mp_Concat/{constituency}_MP_Mobile_Numbers_part2_cleaned.xlsx"
#     second_part.to_excel(second_file_path, index=False)
#     print("............................................second_part")
# else:
#     file_path = f"/home/rajashekar/Desktop/TS_CPU/TELANGANA_MP_EACH_CONSTITUENCY_VERIFIED_DATA/Medak/Medak_Mp_Concat/{constituency}_MP_Mobile_Numbers_cleaned.xlsx"
#     result_df.to_excel(file_path, index=False)
#     print("*******************************************file stored successfully")



# result_df.to_excel(f'/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/Voter_Mp/Zahirabad/{constituency}_Mp_Mobile_Numbers_Cleaned.xlsx',index = False)
# result_df.to_excel('/home/rajashekar/Desktop/MHB_Be_Sc_Mbs/Mahbubnagar_Mp_Beneficiary_Mobiles.xlsx',index=False)
#
# print(result_df)
# result_df.rename(columns={"First Name":"Names"},inplace=True)

# result_df.drop_duplicates(subset = ["Names","Mobile"],inplace=True)
# print(len(result_df))
# result_df.drop_duplicates(subset = ["Mobile"],inplace=True)
# result_df["Names"] = result_df["Names"].astype(str)
# result_df["Names"] = result_df["Names"].str.strip()
# result_df["Names"] = result_df["Names"].str.title()
# result_df.dropna(inplace=True)
# print(len(result_df))
# result_df.to_excel("/home/rajashekar/Desktop/M_Fe_Ma_Data/Beneficiary_Mahbubnagar_Mp_Males_Data.xlsx",index = False)

# result_df = result_df.head(10000)
# print(len(result_df))
# result_df.to_excel('SIDDIPET_15_FILES_DATA.xlsx',index=False)

# import pandas as pd
# #
# df1 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/G_W_94_DATA/GUNTUR_WEST_FINAL_DATA_UNIQUE/GUNTUR_WEST_94_FINAL_DATA.xlsx",usecols=["Mobile"])
# df2 = pd.read_excel(r"/home/rajashekar/Downloads/GUNTUR_WEST_AFTER_REMOVE_DUPLICATES_cleaned.xlsx",usecols=["Mobile"])
# df3= pd.read_excel(r"/home/rajashekar/Downloads/vishwa_brahman_cleaned.xlsx",usecols = ["Mobile"])
# #
#
# print(len(df1))
# print(len(df2))
# print(len(df3))
# df = pd.concat([df1,df2,df3],ignore_index=True)
#
# print(len(df))
#
# # df.drop_duplicates(subset=["Names","Mobile"],ignore_index=True)
# df.drop_duplicates(subset=["Mobile"],inplace=True)
# df.dropna(inplace=True)
#
# print(len(df))
#
# df.to_excel("GUNTUR_WEST_FINAL_UPDATED_UNIQUE_MOBILE_NUMBERS.xlsx",index = False)
#
# l = len(df)
# print("After droping of duplicate rows",l)
# if l > 1000000:
#     first_part = df.iloc[:1000000, :]
#     second_part = df.iloc[1000000:, :]
#
#     first_file_path = "MALKAJGIRI_UGADI_NAMES_AND_MOBILE_Part_1.xlsx"
#     first_part.to_excel(first_file_path, index=False)
#
#     print("............................................first_part")
#
#     second_file_path = "MALKAJGIRI_UGADI_NAMES_AND_MOBILE_part_2.xlsx"
#     second_part.to_excel(second_file_path, index=False)
#     print("............................................second_part")
# else:
#     file_path = "MALKAJGIRI_UGADI_MOBILE_NUMBERS.xlsx"
#     df.to_excel(file_path, index=False)
#     print("*******************************************original file stored successfully")

# df1 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/MP_UNIQUE/Guntur/Guntur_MP_UNIQUE_DATA.xlsx")
# print(len(df1))
# df2 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/CONSTITUENCY_UNIQUE/Guntur/Guntur_West_Campaign_Final_data_Cleaned.xlsx")
# print(len(df2))
#
# df = pd.concat([df1,df2],ignore_index=True)
# print(len(df))
# df.dropna(subset = ["Names","Mobile"],inplace = True)
# print(len(df))

# import pandas as pd
#
# df1 = pd.read_excel(r"/home/rajashekar/Desktop/M_Fe_Ma_Data/Beneficiary_Mahbubnagar_Mp_Females_Data.xlsx",usecols=["Names","Mobile"])
# df2 = pd.read_excel(r"/home/rajashekar/Desktop/M_Fe_Ma_Data/Mehbubnagar_Females_Mp_Data_from_Voters_Data.xlsx",usecols=["Names","Mobile"])
# # df3 = pd.read_excel(r"/home/rajashekar/Documents/FESTIVALS_DATA/Guntur_Nominations/Narasaraopet_Mp_Data/Narasaraopet_Mp_constituency_UNIQUE.xlsx",usecols=["Mobile"])
# # df4 = pd.read_excel(r"/home/rajashekar/Documents/FESTIVALS_DATA/Guntur_Nominations/Vijayawada_Mp_Data/Vijayawada_MP_UNIQUE_DATA.xlsx",usecols=["Mobile"])
#
# df = pd.concat([df1,df2],ignore_index=True)
# print(len(df1))
# print(len(df2))
# # print(len(df3))
# # print(len(df4))
# print(len(df))
#
# df["Names"] = df["Names"].astype(str)
# df["Names"] = df["Names"].str.strip()
# df["Names"] = df["Names"].str.title()
#
# df.drop_duplicates(subset=["Names","Mobile"],inplace=True)
# df.drop_duplicates(subset=["Mobile"],inplace=True)
# print(len(df))
#
# df.to_excel('/home/rajashekar/Desktop/M_Fe_Ma_Data/Mahbubnagar_Total_Females.xlsx',index=False)
#
# df = df[["Mobile"]]
#
# l = len(result_df)
# print("After droping of duplicate rows",l)
# if l > 1000000:
#     first_part = result_df.iloc[:1000000, :]
#     second_part = result_df.iloc[1000001:, :]
#
#     first_file_path = "/home/rajashekar/Desktop/TS_CPU/TELANGANA_MP_EACH_CONSTITUENCY_VERIFIED_DATA/Medak/Medak_Mp_Concat/Medak_Mp_Concat_verified_Part1.xlsx"
#     first_part.to_excel(first_file_path, index=False)
#
#     print("............................................first_part")
#
#     second_file_path = "/home/rajashekar/Desktop/TS_CPU/TELANGANA_MP_EACH_CONSTITUENCY_VERIFIED_DATA/Medak/Medak_Mp_Concat/Medak_Mp_Concat_verified_part2.xlsx"
#     second_part.to_excel(second_file_path, index=False)
#     print("............................................second_part")
# else:
#     file_path = "/home/rajashekar/Desktop/TS_CPU/TELANGANA_MP_EACH_CONSTITUENCY_VERIFIED_DATA/Medak/Medak_Mp_Concat/Medak_Mp_Concat.xlsx"
#     result_df.to_excel(file_path, index=False)
#     print("*******************************************original file stored successfully")

# MedakCleaned_mobile_numbers_verified.xlsx
# 140250
# Dubbak_mobile_numbers_verified.xlsx
# 175692
# Sangareddy_Mobile_Numbers_Veriied.xlsx
# 131960
# Gajwel_mobile_numbers_verified.xlsx
# 206948
# Narsapur_Mobile_Numbers_Veriied.xlsx
# 158170
# Siddipet_mobile_numbers_verified.xlsx
# 186866
# Pantancheruvu_Mobile_Numbers_Veriied.xlsx
# 237223
# 1237109
# 952972
# After droping of duplicate rows 952972

