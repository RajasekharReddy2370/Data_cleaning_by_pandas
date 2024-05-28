import pandas as pd

df1 = pd.read_excel(r"/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Medak_34/Medak_34_MP_first_part_unique.xlsx")
df2 = pd.read_excel(r"/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Medak_34/Medak_34_MP_second_part_unique.xlsx")
df = pd.concat([df1,df2],ignore_index=True)


df["Names"] = df["Names"].astype(str)
df["Names"] = df["Names"].str.lower()

# Splitting 'Names' column into separate parts
df['Split_Names'] = df['Names'].str.split()

# Filtering rows where 'modi' is present in split names
# result = df[df['Split_Names'].apply(lambda x: any('modi' in y.lower() for y in x if y is not None))]

# exact match
result = df[df['Split_Names'].apply(lambda x: any(y.lower() == 'modi' for y in x if y is not None))]

# Selecting only 'Names' and 'Mobile' columns
result = result[['Names', 'Mobile']]
print(result)
print(len(result))

# Exporting filtered DataFrame to Excel
output_file = 'MODI_exactmatch_data.xlsx'
result.to_excel(output_file, index=False)
#
# print("Filtered data with Modi present in split names has been exported to", output_file)

