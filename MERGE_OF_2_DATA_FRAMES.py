import pandas as pd
import time
import os
start_time = time.time()

# main_file_path = "/home/rajashekar/Desktop/UGADI_CAMPAINING_DATA/Mahubnagar_CONSTITUENCY_DATA"
# files = os.listdir(main_file_path)
#
# for file in files:
#     constituency = file.split('_')[0]
#     df1 = pd.read_excel(main_file_path+'/'+file)
#     df2 = pd.read_excel(r"/home/rajashekar/Downloads/Mahbubnagar  Hindi names converted.xlsx",usecols=["Hindi_Names","Mobile"])
#
#     merged_df = pd.merge(df1, df2, on='Mobile', how='left')
#     print(len(merged_df))
#
#     # Rename Hindi_Names column to match the desired output
#     merged_df.rename(columns={'Hindi_Names': 'Hindi_Names'}, inplace=True)
#
#     print(merged_df.columns)
#
#     merged_df["Names"] = merged_df["Names"].astype(str)
#     merged_df["Names"] = merged_df["Names"].str.strip()
#     merged_df["Names"] = merged_df["Names"].str.title()
#
#     merged_df["Telugu_Names"] = merged_df["Telugu_Names"].astype(str)
#     merged_df["Telugu_Names"] = merged_df["Telugu_Names"].str.strip()
#     merged_df["Telugu_Names"] = merged_df["Telugu_Names"].str.title()
#
#     merged_df["Hindi_Names"] = merged_df["Hindi_Names"].astype(str)
#     merged_df["Hindi_Names"] = merged_df["Hindi_Names"].str.strip()
#     merged_df["Hindi_Names"] = merged_df["Hindi_Names"].str.title()
#
#     # Reorder columns to match the desired output
#     merged_df = merged_df[['Names', 'Telugu_Names', 'Hindi_Names', 'Mobile']]
#
#     print(merged_df)
#     #
#     merged_df.to_excel(f'/home/rajashekar/Desktop/M_H/{constituency}.xlsx', index=False)




df1 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/voter_MP_Data/Vizainagaram/Cheepurupalli-15-AC- iToC Voter Data.xlsx")
print(len(df1))

df2 = pd.read_excel(r"/home/rajashekar/Downloads/CHEEPURUPALLI.xlsx",usecols=["Mobile"])
print(len(df2))

# Merge dataframes based on Mobile column
merged_df = pd.merge(df1, df2, on='Mobile', how='inner')
print(len(merged_df))

print(merged_df.columns)

# merged_df.to_excel("CHEEPURUPALLI_DATA.xlsx",index = False)

# # Rename Hindi_Names column to match the desired output
# merged_df.rename(columns={'Hindi_Names': 'Hindi_Names'}, inplace=True)
#
# print(merged_df.columns)
#
# merged_df["Names"] = merged_df["Names"].astype(str)
# merged_df["Names"] = merged_df["Names"].str.strip()
# merged_df["Names"] = merged_df["Names"].str.title()
#
# # Reorder columns to match the desired output
# merged_df = merged_df[['Names', 'Telugu_Names', 'Hindi_Names', 'Mobile']]
#
# print(merged_df)
# #
# merged_df.to_excel('Merge.xlsx',index = False)
#
# #
# end_time = time.time()
# print("overall_time",end_time-start_time)





