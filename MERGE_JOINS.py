# import pandas as pd
#
# # Load DataFrames from Excel files
# df1 = pd.read_excel("/home/rajashekar/WORK/voters_prac/Kodangal_updated_Final_Cleaned.xlsx",usecols=["Names","Mobile"])
# df2 = pd.read_excel("/home/rajashekar/WORK/voters_prac/Kodangal_Final_Cleaned.xlsx",usecols=["Names","Mobile"])
#
# # Merge the two DataFrames on common columns
# merged = df2.merge(df1, how='left', indicator=True)
# print(merged)
#
# # Filter out rows present only in the second DataFrame (df2)
# result = merged[merged['_merge'] == 'left_only']
#
# # Drop the _merge column if not needed
# result = result.drop(columns=['_merge'])
# #
# print(result)

# result.to_excel("CHEEPURUPALLI_NOT_PRESENT_DATA.xlsx",index = False)

# m_df = pd.merge(df1,df2, on  = "First Name", how="Right" )

import pandas as pd

# Load DataFrames from Excel files
df1 = pd.read_excel("/home/rajashekar/WORK/voters_prac/Kodangal_updated_Final_Cleaned.xlsx", usecols=["Names", "Mobile"])
df2 = pd.read_excel("/home/rajashekar/WORK/voters_prac/Kodangal_Final_Cleaned.xlsx", usecols=["Names", "Mobile"])

# Extract mobile values from df1 that are not present in df2
result = df1[~df1['Mobile'].isin(df2['Mobile'])]

print(result)
print(len(result))
