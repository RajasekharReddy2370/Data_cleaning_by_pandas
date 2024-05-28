import pandas as pd
import re
df = pd.read_excel(r"/home/rajashekar/Documents/Guntur_West_Tuesday_imported_Data/Concatenatd_Data.xlsx")

print(len(df))

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

df["Names"] = df["Names"].astype(str)
df["Names"] = df["Names"].str.strip()
df["Names"] = df["Names"].str.title()

# df["Telugu_Names"] = df["Telugu_Names"].astype(str)
# df["Telugu_Names"] = df["Telugu_Names"].str.strip()

def clean_mobile_number(mobile):
    try:
        mobile_float = float(mobile)
        mobile = "{:.0f}".format(mobile_float)
    except ValueError:
        mobile = str(mobile)

    if mobile.endswith(".0"):
        mobile = mobile[:-2]

    return mobile

# Assuming df is your DataFrame
df['Mobile'] = df['Mobile'].apply(clean_mobile_number)

df['Mobile'] = df['Mobile'].astype('str')
df = df[df['Mobile'].str.isdigit()]
df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
df['Mobile'] = df['Mobile'].apply(lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)

df = df[df["Mobile"].notna()]  # Remove rows where Mobile is None

df["Mobile"] = df["Mobile"].astype(int)

df.drop_duplicates(subset = ["Mobile"],inplace = True)

print(df)
print(len(df))

df.to_excel("Guntur_imported_cleaned_Data2.xlsx",index = False)
# df.to_excel("Zahirabad_cleaned_Mp__Data.xlsx",index = False)