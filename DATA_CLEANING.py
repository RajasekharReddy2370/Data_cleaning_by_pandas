import pandas as pd
import re

# df = pd.read_excel(r"/home/rajashekar/Documents/Final_Cleaned.xlsx",usecols=['FM_NAME_EN','MOBILE_NO'])
df = pd.read_excel(r"/home/rajashekar/Documents/Kodangal_data_from_final_data_sheet.xlsx")
# df = pd.read_excel(r"/home/rajashekar/Desktop/TS_CPU/ZZ_IMPORTED_DATA/MEHBUBNAGAR/Voters Age 85 +PC-11.xlsx")
print(df)

# df.rename(columns={'FM_NAME_EN':"Names",'MOBILE_NO':"Mobile"},inplace=True)

def add_space_in_dot(name):
    if "." in name:
        name = name.replace(".", " ")
        return name
    else:
        return name

df['Names'] = df['Names'].apply(add_space_in_dot)

def add_space_in_dot(name):
    if "," in name:
        name = name.replace(",", " ")
        return name
    else:
        return name

df['Names'] = df['Names'].apply(add_space_in_dot)

def extract_alphabets_and_spaces(values):
    value = str(values)
    return re.sub(r'[^a-zA-Z\s]', '', value)

df['Names'] = df['Names'].apply(extract_alphabets_and_spaces)

df['Names'] = df['Names'].str.strip()
df = df[df["Names"].str.strip() != ""]

df.dropna(inplace=True)


# def clean_mobile_number(mobile):
#     # Convert scientific notation to normal form
#     if 'e' in str(mobile):
#         mobile = "{:.0f}".format(mobile)
#     # Remove ".0" if it exists at the end
#     mobile_str = str(mobile)
#     if mobile_str.endswith('.0'):
#         mobile = mobile_str[:-2]
#     return mobile
#
# df['Mobile'] = df['Mobile'].apply(clean_mobile_number)

def clean_mobile_number(mobile):
    # Try to convert mobile to float to handle scientific notation and remove decimals
    try:
        mobile_float = float(mobile)
        # Convert scientific notation to normal form and remove ".0" if it exists
        mobile = "{:.0f}".format(mobile_float)
    except ValueError:
        # If conversion fails, it's likely already a string that doesn't need conversion
        mobile = str(mobile)

    # Remove any trailing ".0"
    if mobile.endswith(".0"):
        mobile = mobile[:-2]

    return mobile

df['Mobile'] = df['Mobile'].apply(clean_mobile_number)

df['Mobile'] = df['Mobile'].astype('str')
df = df[df['Mobile'].str.isdigit()]
df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
df['Mobile'] = df['Mobile'].apply(lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
df.dropna(subset=['Names', 'Mobile'], inplace=True)
df["Names"] = df["Names"].apply(lambda x: x if len(x) > 0 else x)
df = df[df["Names"].str.strip() != ""]
df.drop_duplicates(subset=['Names', 'Mobile'], inplace=True)
df.drop_duplicates(subset=['Mobile'], inplace=True)

df = df[['Names','Mobile']]
print(df)
df.to_excel("Kodangal_updated_Final_Cleaned.xlsx",index = False)
# df.to_excel('/home/rajashekar/Desktop/TS_CPU/ZZ_IMPORTED_DATA/IMPORTED_DATA_CLEANED/Mehbubnagar/Voters_Age_85.xlsx',index=False)