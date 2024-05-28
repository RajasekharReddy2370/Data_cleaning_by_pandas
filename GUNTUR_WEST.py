# import pandas as pd
#
# df1 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/G_W_94_DATA/94_GUNTUR_WEST_AND_EXTRA_GUNTUR_DATA_GUNTUR_NEW_DATA.xlsx")
# print(len(df1))
# df2 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/GUNTUR_IMPORTED_DATA/Guntur_Rice_Card.xlsx",usecols=["Names","Telugu_Names","Mobile"])
# print(len(df2))
#
# df = pd.concat([df1,df2],ignore_index=True)
# print(len(df))
# print(df)
#
# df["Names"] = df["Names"].astype(str)
# df["Names"] = df["Names"].str.strip()
# df["Names"] = df["Names"].str.title()
#
# df.drop_duplicates(subset = ["Mobile"],inplace= True)
#
#
# print(len(df))
# df.to_excel("GUNTUR_WEST_CAMPAINING_DATA1.xlsx",index = False)


import pandas as pd

df = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/G_W_94_DATA/GUNTUR_WEST_CAMPAINING_DATA1.xlsx")
print(len(df))
df.to_excel("GUNTUR_WEST_OMLY_MOBILE_NUMBERS.xlsx",index=False)