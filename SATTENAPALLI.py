import pandas as pd

df1 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/STP_DATA/Sattenapalli_raw_data_and_leela_parsed_data.xlsx")
print(len(df1))
df2 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/STP_DATA/SATTENAPALLI_SCHEMES_CONCAT_DATA_FROM_CLEANED_SCHEMES.xlsx")
print(len(df2))

df = pd.concat([df1,df2],ignore_index=True)
print(len(df))

df.drop_duplicates(subset=["Mobile"],inplace = True)
df.to_excel("SATTENAPALLI_CAMPAINING_DATA.xlsx",index = False)

print(len(df))



