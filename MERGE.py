# import pandas as pd
#
# df1 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/voter_MP_Data/Vizainagaram/Cheepurupalli-15-AC- iToC Voter Data.xlsx")
# df2 = pd.read_excel(r"/home/rajashekar/Downloads/CHEEPURUPALLI.xlsx",usecols=["Mobile"])
#
# print(df1.columns)
# print(len(df1))
# print(df2.columns)
# print(len(df2))
# # df = pd.concat([df1["Epic No"],[df2["Voter_id"]]],ignore_index=True)
# df_concatenated = pd.concat([df1["Epic No"], df2["Voter_id"]], axis=0,ignore_index=True)
#
# print(df_concatenated)
# print(len(df_concatenated))

# df1 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/voter_MP_Data/Guntur/Guntur West-94-AC- iToC Voter Data.xlsx")
# df2 = pd.read_excel(r"")

import pandas as pd

# Load DataFrames from Excel files
df1 = pd.read_excel("/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Mahbubnagar_74/Mahbubnagar_74_MP_unique.xlsx", usecols=["Names", "Mobile"])
df2 = pd.read_excel("/home/rajashekar/Desktop/TS_CPU/Mahbubnagar_Hindi_names_converted_cleaned.xlsx", usecols=["Hindi_Names", "Mobile"])

# Merge the two DataFrames on the "Mobile" column
merged_df = pd.merge(df1, df2, on="Mobile", how="left")

# Display the merged DataFrame
print(merged_df)
print(len(merged_df))
