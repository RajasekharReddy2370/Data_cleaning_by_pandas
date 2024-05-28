# import pandas as pd
# import os
#
# main_file_path = "/home/rajashekar/Desktop/TS_CPU/Voter_MP_Data/Mahbubnagar_74"
# files = os.listdir(main_file_path)
# for file in files:
#     print(file)
#     constituency = file.split('.')[0]
#     print(main_file_path+'/'+file)
#     df = pd.read_excel(main_file_path+'/'+file,usecols = ['B#', 'S', 'S#', 'House No', 'First Name', 'Last Name', 'Voter ID', 'G','Age', 'Mobile', 'Address Area'])
#     df.rename(columns={'First Name':"FM_NAME_EN",'Last Name':"LASTNAME_EN"},inplace = True)
#     print(df.columns)
#     new_df = df.copy()
#     # new_df = df.loc[:,["First Name", 'Last Name', 'Voter ID','Mobile']]
#     new_df['LASTNAME_EN'] = new_df['LASTNAME_EN'].fillna('')
#     new_df['FM_NAME_EN'] = new_df['FM_NAME_EN'].astype(str)
#     new_df['LASTNAME_EN'] = new_df['LASTNAME_EN'].astype(str)
#     new_df['FM_NAME_EN'] = new_df['FM_NAME_EN'].str.strip()
#     new_df['LASTNAME_EN'] = new_df['LASTNAME_EN'].str.strip()
#     new_df['Names'] = new_df['FM_NAME_EN'] + ' ' + new_df['LASTNAME_EN']
#
#     new_df["Names"] = new_df["Names"].str.title()
#     DF = new_df[['B#', 'S', 'S#', 'House No', 'Names','Voter ID',
#        'G', 'Age', 'Mobile', 'Address Area']]
#
#
#     def add_space_in_dot(name):
#         if "." in name:
#             name = name.replace(".", " ")
#             return name
#         else:
#             return name
#
#
#     DF.loc[:, 'Names'] = DF['Names'].apply(add_space_in_dot)
#     DF.loc[:, 'Names'] = DF['Names'].str.strip()
#     DF.drop_duplicates(subset = ["Voter ID"],inplace = True)
#     DF.dropna(subset = ["Names"],inplace = True)
#     print(DF)
#     # DF.to_excel(f"/home/rajashekar/Desktop/MAHBUBNAGAR_CASTE_WISE_DATA/MAHBUBNAGAR_VOTER_DATA_CONSTITUENCIES/{constituency}_cleaned_Data.xlsx",index = False)
#     # print(f"{constituency} stored successfully")
#     break

import pandas as pd
import os

main_file_path = "/home/rajashekar/Desktop/TS_CPU/Voter_MP_Data/Mahbubnagar_74"
files = os.listdir(main_file_path)
for file in files:
    print(file)
    constituency = file.split('.')[0]
    print(main_file_path+'/'+file)
    df = pd.read_excel(main_file_path+'/'+file, usecols=['B#', 'S', 'S#', 'House No', 'First Name', 'Last Name', 'Voter ID', 'G','Age', 'Mobile', 'Address Area'])
    df.rename(columns={'B#':'BOOTH_NO','S#':'SERIAL_NO','First Name': "FM_NAME_EN", 'Last Name': "LASTNAME_EN"}, inplace=True)
    print(df.columns)
    new_df = df.copy()
    new_df['LASTNAME_EN'] = new_df['LASTNAME_EN'].fillna('')
    new_df['FM_NAME_EN'] = new_df['FM_NAME_EN'].astype(str)
    new_df['LASTNAME_EN'] = new_df['LASTNAME_EN'].astype(str)
    new_df['FM_NAME_EN'] = new_df['FM_NAME_EN'].str.strip()
    new_df['LASTNAME_EN'] = new_df['LASTNAME_EN'].str.strip()
    new_df['Names'] = new_df['FM_NAME_EN'] + ' ' + new_df['LASTNAME_EN']
    new_df["Names"] = new_df["Names"].str.title()
    DF = new_df[['BOOTH_NO', 'S', 'SERIAL_NO', 'House No', 'Names','Voter ID', 'G', 'Age', 'Mobile', 'Address Area']]

    def add_space_in_dot(name):
        if "." in name:
            name = name.replace(".", " ")
            return name
        else:
            return name
    # Use .loc to avoid SettingWithCopyWarning
    DF.loc[:, 'Names'] = DF['Names'].apply(add_space_in_dot)
    DF.loc[:, 'Names'] = DF['Names'].str.strip()
    # Use .loc to avoid SettingWithCopyWarning
    DF.drop_duplicates(subset=["Voter ID"], inplace=True)
    # Use .loc to avoid SettingWithCopyWarning
    DF.dropna(subset=["Names"], inplace=True)
    print(DF)
    DF.to_excel(f"/home/rajashekar/Desktop/MAHBUBNAGAR_CASTE_WISE_DATA/MAHBUBNAGAR_VOTER_DATA_CONSTITUENCIES/{constituency}_cleaned_Data.xlsx", index=False)
    print(f"{constituency} stored successfully")
      # If you want to process only one file, remove this break statement


