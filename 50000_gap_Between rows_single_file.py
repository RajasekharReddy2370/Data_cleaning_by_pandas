
import pandas as pd

# df1 = pd.read_excel(r"")
# df2 = pd.read_excel(r"")
# df = pd.concat([df1,df2],ignore_index=True)


# Assuming your original DataFrame is named 'df'
df = pd.read_excel(r"/home/rajashekar/Desktop/Andhra_State_Daily_data/Kakinada/Kakinada_40_above_age/Kakinada_MP_From_40_Age_Group.xlsx")

# Create a DataFrame with one empty row
empty_row = pd.DataFrame({'Mobile': [None]})

# Create a list to store the modified dataframes
dfs = []

# Split the original DataFrame into chunks of 50,000 rows
for i in range(0, len(df), 50000):
    chunk = df.iloc[i:i+50000].copy()  # Get a chunk of 50,000 rows
    dfs.append(chunk)  # Append the chunk to the list
    if i < len(df) - 50000:  # Ensure we don't add an empty row after the last chunk
        dfs.append(empty_row)  # Append an empty row after each chunk

# Concatenate the list of dataframes into a single dataframe
new_df = pd.concat(dfs, ignore_index=True)

# Reset the index of the new DataFrame
new_df.reset_index(drop=True, inplace=True)

# new_df.to_excel('/home/rajashekar/Documents/Machilipatnam_18_35_women_35_70/Women/Machilipatnam_MP_Female_50000_Gap.xlsx',index = False)
# new_df.to_excel('/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Mahbubnagar/Mahbubnagar_Mp_Mobile_Numbers_with_50000_gap/Mahbubnagar_MP_Mobile_Numbers_50000_gap_starting_with_91_part2.xlsx',index = False)
new_df.to_excel("Kakinada_MP_From_40_Age_Group_50000_Gap.xlsx",index=False)




