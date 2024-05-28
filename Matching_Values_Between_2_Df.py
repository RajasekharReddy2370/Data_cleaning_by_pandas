import pandas as pd
#
# # Sample dataframes
# df1 = pd.DataFrame({
#     'Names': ['Alice', 'Bob', 'Charlie'],
#     'Telugu_Names': ['అలిస్', 'బాబు', 'చార్లీ'],
#     'Mobile': ['1234567890', '2345678901', '3456789012']
# })
#
# df2 = pd.DataFrame({
#     'Names': ['Bob', 'David', 'Emma'],
#     'Telugu_Names': ['బాబు', 'డేవిడ్', 'ఎమ్మా'],
#     'Mobile': ['2345678901', '4567890123', '5678901234']
# })
file = "Penamaluru"
# df1 = pd.read_excel(r"/home/rajashekar/Desktop/Andhra_State_Daily_data/Machilipatnam/Machalipatnam_imported_data_Names_Mobile_which_are_equal_to_5_lakhs/Avanigadda_Names_Mobile_Numbers_unique.xlsx")
# df2 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/CONSTITUENCY_UNIQUE/Machilipatnam_updated_constituency_wise/Avanigadda_Constituency_Names_Mobile_Numbers.xlsx")
df1 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/CONSTITUENCY_UNIQUE/Machilipatnam_updated_constituency_wise/Penamaluru_Constituency_Names_Mobile_Numbers.xlsx")
df2 = pd.read_excel(r"/home/rajashekar/Desktop/Andhra_State_Daily_data/Machilipatnam/Machalipatnam_imported_data_Names_Mobile_which_are_equal_to_5_lakhs/penamaluru_Names_Mobile_Numbers_unique.xlsx")
print(len(df1))
print(len(df2))
# df1.dropna(subset=["Mobile"],inplace=True)
# print(len(df1))
# df2.dropna(subset=["Mobile"],inplace=True)
# print(len(df2))

# Find matched mobile numbers
# matched_mobiles = df1[df1['Mobile'].isin(df2['Mobile'])]['Mobile'].tolist()
# unmatched_mobiles = df1[~df1['Mobile'].isin(df2['Mobile'])]['Mobile'].tolist()
# unmatched_mobiles = df1[~df1['Mobile'].isin(df2['Mobile'])][['Names', 'Mobile']]
unmatched_mobiles = df1[~df1['Mobile'].isin(df2['Mobile'])][['Mobile']]

# print("Matched Mobile Numbers:")
# print("UNMatched Mobile Numbers:")
# print(matched_mobiles)
# print(len(matched_mobiles))
print(len(unmatched_mobiles))
print(unmatched_mobiles)
# unmatched_mobiles.to_excel("Machilipatnam_remaining_numbers_other_than_5_lakhs.xlsx",index=False)
unmatched_mobiles.to_excel(f"/home/rajashekar/Desktop/Andhra_State_Daily_data/Machilipatnam/Machalipatnam_imported_data_Names_Mobile_which_are_equal_to_5_lakhs/otherthan_5_lakhs/{file}_remaining_mobile_numbers_which_are_not_in_5_lakhs.xlsx",index = False)

#9951634052


# import pandas as pd
#
# # Read the dataframes
# df1 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/G_W_94_DATA/GUNTUR_WEST_FINAL_DATA_UNIQUE/GUNTUR_WEST_94_FINAL_DATA.xlsx")
# df2 = pd.read_excel(r"/home/rajashekar/Desktop/Concatenated_Data/Concatenated_Data.xlsx")
#
# # Merge the dataframes on the "Mobile" column, keeping all rows from both dataframes
# merged_df = pd.merge(df1, df2, on='Mobile', how='outer', suffixes=('_df1', '_df2'))
#
# # Extract matched and unmatched mobile numbers
# matched_mobiles = merged_df['Mobile'][(~merged_df['Mobile'].isnull()) & (~merged_df['Names_df1'].isnull()) & (~merged_df['Names_df2'].isnull())].tolist()
# unmatched_mobiles_df1 = merged_df['Mobile'][(~merged_df['Mobile'].isnull()) & (~merged_df['Names_df1'].isnull()) & (merged_df['Names_df2'].isnull())].tolist()
# unmatched_mobiles_df2 = merged_df['Mobile'][(~merged_df['Mobile'].isnull()) & (merged_df['Names_df1'].isnull()) & (~merged_df['Names_df2'].isnull())].tolist()
#
# print("Matched Mobile Numbers:")
# print(matched_mobiles)
#
# print("Unmatched Mobile Numbers in DataFrame 1:")
# print(unmatched_mobiles_df1)
#
# print("Unmatched Mobile Numbers in DataFrame 2:")
# print(unmatched_mobiles_df2)
