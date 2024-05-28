# import pandas as pd
# import os
#
# main_folder_path = r"/home/rajashekar/Desktop/AP_CPU/voter_MP_Data/Anakapalli"
# files = os.listdir(main_folder_path)
# n = "galla madhavi"
# for file in files:
#     c = 0
#
#     # if "Chodavaram" in file:
#     # df = pd.read_excel(main_folder_path+'/'+file,usecols=["Names"])
#     print(file)
#     df = pd.read_excel(main_folder_path+'/'+file)
#     # print(df.columns)
#     # df = df.loc[:,["First Name", 'Last Name', 'Voter ID','Mobile']]
#     # print(df)
#     df['Last Name'] = df['Last Name'].fillna('')
#     df['First Name'] = df['First Name'].astype(str)
#     df['Last Name'] = df['Last Name'].astype(str)
#     df['First Name'] = df['First Name'].str.strip()
#     df['Last Name'] = df['Last Name'].str.strip()
#     df['Names'] = df['First Name'] + ' ' + df['Last Name']
#     df["Names"] = df["Names"].str.lower()
#
#     for i in df["Names"]:
#         # print(i)
#         if i in n:
#             print(n,"in",file,"found")
#             c +=1
#     print(c)

# import pandas as pd
#
# # df = pd.read_excel(r"/home/rajashekar/Desktop/ANDHRA_PRADESH/IMPORTED_DATA/GUNTUR/94-Guntur West.xlsx",usecols = ['FM_NAME_EN','LASTNAME_EN'])
# df = pd.read_excel(r"/home/rajashekar/Desktop/ANDHRA_PRADESH/IMPORTED_DATA/GUNTUR/94-Guntur West.xlsx")
# print(df.columns)
#
# df['LASTNAME_EN'] = df['LASTNAME_EN'].fillna('')
# df['FM_NAME_EN'] = df['FM_NAME_EN'].astype(str)
# df['LASTNAME_EN'] = df['LASTNAME_EN'].astype(str)
# df['FM_NAME_EN'] = df['FM_NAME_EN'].str.strip()
# df['LASTNAME_EN'] = df['LASTNAME_EN'].str.strip()
# df['Names'] = df['FM_NAME_EN'] + ' ' + df['LASTNAME_EN']
#
# # df = df[['Names']]
#
# df['Names'] = df["Names"].astype(str)
# df['Names'] = df["Names"].str.strip()
# df['Names'] = df["Names"].str.title()
#
# # print(df)
# df.dropna(subset=["Names"],inplace = True)
#
# # filtered_df = df[df['Names'].str.contains('Nathani Sreeram',case = False,na = False)]
# filtered_df = df[df['Names'].str.contains('Gangisetti',case = False,na = False)]
#
# print(filtered_df)
# print(len(filtered_df))
# filtered_df.to_excel('Gangisetti.xlsx',index = False)
#
# n_df = df[df['Names'] == 'Gangisetti venugopal']
# print(n_df)
#
# n2_df = df[df['Names'] == 'venugopal Gangisetti']
# print(n2_df)



import pandas as pd

# Load the Excel file
df = pd.read_excel(r"/home/rajashekar/Desktop/ANDHRA_PRADESH/IMPORTED_DATA/GUNTUR/94-Guntur West.xlsx")

# Display the column names for verification
print(df.columns)

# Handle missing values in 'FM_NAME_EN' and 'LASTNAME_EN' columns
df['LASTNAME_EN'] = df['LASTNAME_EN'].fillna('')
df['FM_NAME_EN'] = df['FM_NAME_EN'].astype(str)
df['LASTNAME_EN'] = df['LASTNAME_EN'].astype(str)

# Strip leading and trailing spaces from 'FM_NAME_EN' and 'LASTNAME_EN' columns
df['FM_NAME_EN'] = df['FM_NAME_EN'].str.strip()
df['LASTNAME_EN'] = df['LASTNAME_EN'].str.strip()

# Combine 'FM_NAME_EN' and 'LASTNAME_EN' into a new 'Names' column
df['Names'] = df['FM_NAME_EN'] + ' ' + df['LASTNAME_EN']

# Strip leading and trailing spaces and convert to title case in 'Names' column
df['Names'] = df['Names'].astype(str).str.strip().str.title()

# Drop rows where 'Names' column is empty
df.dropna(subset=["Names"], inplace=True)

# Filter the DataFrame based on the 'Names' column
filtered_df = df[df['Names'].str.contains('Gangisetti', case=False, na=False)]

# Display the filtered DataFrame and its length
print(filtered_df)
print(len(filtered_df))
filtered_df.to_excel('Gangisetti.xlsx',index = False)





