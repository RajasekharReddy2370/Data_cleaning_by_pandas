# import pandas as pd
#
# master  = pd.read_excel(r"/home/rajashekar/Downloads/HH_Data_Guntur_Schemes_in_one(2).xlsx")
# print(len(master))
# reports  = pd.read_excel(r"/home/rajashekar/Downloads/Overall Data.xlsx")
# print(len(reports))
# print(master.columns)
# print(reports.columns)
#
# df = pd.concat([master,reports],ignore_index=True)
# df.dropna(subset=['MOBILE'],inplace=True)
# print(df.info())
# print(len(df))
# # df.to_excel("ORIGINAL_REPORTS.xlsx",index=False)
# df.dropna(subset = ['Favour'],inplace=True)
#
# print("#############################################",len(df))
# df.drop_duplicates(subset=['MOBILE'],keep = 'last',inplace=True)
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",len(df))
# # df.to_excel("UNIQUE_REPORTS.xlsx",index=False)
# df.dropna(subset = ['Favour'],inplace=True)
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",len(df))


# import pandas as pd
#
# # Sample DataFrame with different columns including 'Favour'
# df = pd.read_excel(r"/home/rajashekar/WORK/voters_prac/UNIQUE_REPORTS.xlsx")
#
# # Group by 'Favour' column
# grouped = df.groupby('Favour')
#
# # Store each group in a separate Excel file
# for favour, group_df in grouped:
#     # Skip if 'Favour' is None
#     if favour is None:
#         continue
#
#     # Construct Excel file name based on 'Favour' value
#     excel_file_path = f"master_{favour}_group.xlsx"
#
#     # Store the group DataFrame in an Excel file
#     group_df.to_excel(excel_file_path, index=False)
#
#     print(f"Group '{favour}' saved to Excel file:", excel_file_path)


import pandas as pd

df = pd.read_excel(r"/home/rajashekar/Documents/ZHRB.xlsx")

df["Names"] = df["Names"].astype(str)
df["Names"] = df["Names"].str.strip()
df["Names"] = df["Names"].str.title()
df["Telugu_Names"] = df["Telugu_Names"].str.strip()

print(df)

df.to_excel("Zahirabad_Half_cleaned_Data.xlsx",index = False)

