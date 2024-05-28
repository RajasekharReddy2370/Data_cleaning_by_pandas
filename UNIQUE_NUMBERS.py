import pandas as pd

df1 = pd.read_excel(r"/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Secunderabad_70/Secunderabad_70_MP_unique.xlsx")
df2 = pd.read_excel(r"/home/rajashekar/Desktop/SECUNDERABAD_IMPORTED_CLEANED_DATA/SECUNDERABAD_IMPORTED_CLEANED_DATA_MERGED_unique.xlsx")

print(len(df1))
print(len(df2))

df = pd.concat([df1,df2],ignore_index=True)

print(len(df))

df.drop_duplicates(subset=["Names","Mobile"],inplace = True)

print(len(df))

df.drop_duplicates(subset=["Mobile"],inplace = True)

print(len(df))

df.to_excel("SECUNDERABAD_UPDATED_DATA_UNIQUE.xlsx",index = False)