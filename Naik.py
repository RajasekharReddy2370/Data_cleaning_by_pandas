import pandas as pd

# Sample DataFrame
# data = {'Names': ['John Doe', 'Jane Nayak', 'Mark Naik', 'Alice', 'Bob'],
#         'Mobile': [1234567890, 2345678901, 3456789012, 4567890123, 5678901234]}
# df = pd.DataFrame(data)

df = pd.read_excel(r"/home/rajashekar/WORK/voters_prac/MHB_SCST_Data.xlsx")

df.dropna(inplace=True)
# Filter rows containing 'Nayak' or 'Naik'
nayak_df = df[df['Names'].str.contains('Nayak|Naik', case=False)]
# other_df = df[~df['Names'].str.contains('Nayak|Naik', case=False)]
print(nayak_df)
print(len(nayak_df))
# print(other_df)
# print(len(other_df))
# Save filtered DataFrames to separate Excel files
# nayak_df.to_excel('Mahbubnagar_only_Naik's_ST_data_with_Booth_and_Assembly_Constituency_Numbers.xlsx', index=False)
# other_df.to_excel('Mahbubnagar_SC_data.xlsx', index=False)
