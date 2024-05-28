import pandas as pd
df = pd.read_excel(r"/home/rajashekar/Documents/FESTIVALS_DATA/UGADI_CAMPAINING_DATA/MAHBUBNAGAR/Mahbubnagar_Campaining_Data/MAHBUBNAGAR_MP_DATA.xlsx")
print(len(df))
print(df.columns)
df.dropna(inplace=True)
print(len(df))
df.drop_duplicates(subset=["Mobile"],inplace=True)
print(len(df))

