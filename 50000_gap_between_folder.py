import pandas as pd
import os

main_folder_path = "/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS_from_Drive_data_and_schemes/Beneficiary_Voter_Assembly_Constituency/Medak"
files = os.listdir(main_folder_path)
for file in files:
    fil = file.split('_')[0]
    df = pd.read_excel(main_folder_path+'/'+file)
    empty_row = pd.DataFrame({'Mobile': [None]})

    # Create a list to store the modified dataframes
    dfs = []

    # Split the original DataFrame into chunks of 50,000 rows
    for i in range(0, len(df), 50000):
        chunk = df.iloc[i:i + 50000].copy()  # Get a chunk of 50,000 rows
        dfs.append(chunk)  # Append the chunk to the list
        if i < len(df) - 50000:  # Ensure we don't add an empty row after the last chunk
            dfs.append(empty_row)  # Append an empty row after each chunk

    # Concatenate the list of dataframes into a single dataframe
    new_df = pd.concat(dfs, ignore_index=True)

    # Reset the index of the new DataFrame
    new_df.reset_index(drop=True, inplace=True)

    # new_df.to_excel('/home/rajashekar/Documents/Machilipatnam_18_35_women_35_70/Women/Machilipatnam_MP_Female_50000_Gap.xlsx',index = False)
    new_df.to_excel(
        f'/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Medak/Medak_mobile_numbers_50000_gap_constituecy_wise/{fil}_Mobile_Numbers_50000_gap.xlsx',
        index=False)


