import pandas as pd
import re


df = pd.read_excel(r"/home/rajashekar/Downloads/96-Chilakaluripet.xlsx",usecols=["FM_NAME_EN","FM_NAME_V1","MOBILE_NO"])
print(df.columns)
print("TOTAL_LENGTH#####################################################",len(df))
df.rename(columns={"FM_NAME_EN":"Names","FM_NAME_V1":"Telugu_Names","MOBILE_NO":"Mobile"},inplace=True)
print(df.columns)

df.dropna(subset=["Names"],inplace=True)
df.dropna(subset=["Telugu_Names"],inplace=True)
df.dropna(subset=["Mobile"],inplace=True)

df["Names"] = df["Names"].astype(str)
df["Names"] = df["Names"].str.strip()

def add_space_in_dot(name):
    if "." in name:
        name = name.replace(".", " ")
        return name
    else:
        return name

df['Names'] = df['Names'].apply(add_space_in_dot)
def extract_alphabets_and_spaces(values):
    value = str(values)
    return re.sub(r'[^a-zA-Z\s]', '', value)
df['Names'] = df['Names'].apply(extract_alphabets_and_spaces)

df = df[df["Names"].str.strip() != ""]
df.dropna(subset=["Names"],inplace=True)

df.drop_duplicates(subset=["Mobile"],inplace = True)
def clean_mobile_number(mobile):
    # Convert scientific notation to normal form
    if 'e' in str(mobile):
        mobile = "{:.0f}".format(mobile)
    # Remove ".0" if it exists at the end
    mobile_str = str(mobile)
    if mobile_str.endswith('.0'):
        mobile = mobile_str[:-2]
    return mobile

df['Mobile'] = df['Mobile'].apply(clean_mobile_number)

print("After_mobile_validation...................................................",len(df))

df['Mobile'] = df['Mobile'].astype(str)
df = df[df['Mobile'].str.isdigit()]

df['Mobile'] = df['Mobile'].apply(lambda x: x[3:] if len(x) > 10 and x.startswith('+91') else x)
df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)

print(len(df))

df['Mobile'] = df['Mobile'].apply(lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)

print(len(df))

df = df[df["Mobile"].str.strip() != ""]
df.dropna(subset=['Mobile'], inplace=True)
df['Mobile'] = df['Mobile'].astype(int)
print(len(df))

df.to_excel("CHILAKALURIPETA_RAW_DATA.xlsx",index = False)