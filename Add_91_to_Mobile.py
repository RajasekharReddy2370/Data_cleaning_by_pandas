# import pandas as pd
# import os
# main_folder_path = "/home/rajashekar/Desktop/ALL_MP_DATA_UNIQUE_MOBILE_NUMBERS_TS/UPDATED/Mahbubnagar_Total_Mp_Mobile_Numbers_Part1.xlsx"
# files = os.listdir(main_folder_path)
#
# for file in files:
#     fil = file.split('_')[0]
#     df = pd.read_excel(main_folder_path+'/'+file,usecols=["Mobile"])
#
#     df["Mobile"] = df["Mobile"].astype(str)
#     df["Mobile"] = '91'+df["Mobile"]
#
#     df["Mobile"] = df["Mobile"].astype(int)
#     print(df)
#     df.to_excel(f"/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Mahbubnagar/Mahbubnagar_Mp_Mobile_Numbers_part1_with_50000_gap/Mahbubnagar_MP_Mobile_Numbers_part1_50000_Gap_starting_with_91.xlsx",index = False)
    # break
import pandas as pd

df = pd.read_excel(r"/home/rajashekar/Desktop/ALL_MP_DATA_UNIQUE_MOBILE_NUMBERS_TS/UPDATED/Mahbubnagar_Total_Mp_Mobile_Numbers_Part2.xlsx",usecols=["Mobile"])

df["Mobile"] = df["Mobile"].astype(str)
df["Mobile"] = '91'+df["Mobile"]

df["Mobile"] = df["Mobile"].astype(int)
print(df)
df.to_excel("/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Mahbubnagar/Mahbubnagar_Mp_Mobile_Numbers_with_50000_gap/Mahbubnagar_MP_Mobile_Numbers_part1_50000_Gap_starting_with_91_Part2.xlsx",index = False)