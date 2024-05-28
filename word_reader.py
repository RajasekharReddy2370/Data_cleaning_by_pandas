import pandas as pd

df1 = pd.read_excel(r"/home/rajashekar/Downloads/Guntur West-94-B_(1-282)-AGE_ABOVE_80 (A4).xlsx")
print(df1.columns)
df1.dropna(subset=["Voter_id"],inplace = True)
print(len(df1))
df1.drop_duplicates(subset=["Voter_id"],inplace = True)
print(len(df1))

df2 = pd.read_excel(r"/home/rajashekar/Downloads/94-Guntur West.xlsx", usecols = ["Address_eng","RLN_FM_NM_EN","RLN_TYPE","EPIC_NO"])
df2.rename(columns={"EPIC_NO":"Voter_id"},inplace=True)
print(df2.columns)

df = pd.merge(df1, df2, how='inner', on='Voter_id')
print(df.columns)

df['Last Name'] = df['Last Name'].fillna('')
df['First Name'] = df['First Name'].astype(str)
df['Last Name'] = df['Last Name'].astype(str)
df['First Name'] = df['First Name'].str.strip()
df['Last Name'] = df['Last Name'].str.strip()
df['Full Name'] = df['First Name'] + ' ' + df['Last Name']
print(df.columns)
selected_columns = ['B#', 'S', 'S#', 'House No', 'Full Name', 'Voter_id', 'G',
        'Age', 'Mobile', 'Address Area', 'Form 12D Status', 'RLN_TYPE',
        'RLN_FM_NM_EN', 'Address_eng']
#
result = df[selected_columns]

result = result.rename(columns={'Full Name': 'Names'})
print(result.columns)
print(len(result))
result.drop_duplicates(subset=['Voter_id'],inplace = True)
print(len(result))

result.to_excel("94_GTR.xlsx",index = False)