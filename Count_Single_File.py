import pandas as pd

df1 = pd.read_excel(r"/home/rajashekar/Desktop/TS_CPU/TELANGANA_MP_EACH_CONSTITUENCY_VERIFIED_DATA/Zahirabad/Zahirabad_Mp_Data/Zahirabad_cleaned_Mp__Data.xlsx")
df2 = pd.read_excel(r"/home/rajashekar/Desktop/TS_CPU/TELANGANA_MP_EACH_CONSTITUENCY_VERIFIED_DATA/Zahirabad/Zahirabad_Transcripts_cleaned/zaharibad_remaining_data.xlsx")
df = pd.concat([df1,df2],ignore_index=True)
# df = pd.read_excel(r"/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/Beneficiary_Voter_Mp_Constituency/Secunderabad/Secunderabad_MP_Mobile_Numbers_cleaned.xlsx")

print(len(df))

df.drop_duplicates(subset=["Mobile"],inplace=True)
df.to_excel("Zahirabad_total_Mp_cleaned_Data.xlsx",index  =False)