import os

# main_folder_path = r"/home/rajashekar/WORK/TS_DATA/Voter_MP_Data"
# folders = os.listdir(main_folder_path)
# print(folders)
# for folder in folders:
#     folderpath = os.path.join(main_folder_path+'/'+folder)
#     files = os.listdir(folderpath)
#     for file in files:
#         file_path = os.path.join(main_folder_path+'/'+folderpath+'/'+file)
#         print(file_path)

import pandas as pd

df = pd.read_excel(r'/home/rajashekar/Downloads/Kuttu Machine, NRPT, Tele Conference 06.03.2024 (2).xlsx')
print(df.columns)

df = df.iloc[:,['Name of the Candidate','Mobile No']]
print(df)
