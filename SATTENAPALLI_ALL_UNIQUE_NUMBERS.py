import pandas as pd

df1 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/STP_DATA/Sattenapalli_Beneficiary_Data_CLEANED.xlsx",usecols=["Mobile"])
df2 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/STP_DATA/Sattenapalli_raw_data_and_leela_parsed_data.xlsx",usecols=["Mobile"])

df = pd.concat([df1,df2],ignore_index=True)

df.drop_duplicates(subset=["Mobile"],inplace=True)
print(len(df))
# df.to_excel("SATTENAPALLI_MOBILE_NUMBERS.xlsx",index = False)