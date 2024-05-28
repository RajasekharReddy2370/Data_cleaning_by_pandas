import pandas as pd
from indic_transliteration import sanscript
import re
# Assuming you have a DataFrame named df
# and the Telugu_Names column is named 'Telugu_Names'
df = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/G_W_94_DATA/94_GUNTUR_WEST_AND_EXTRA_GUNTUR_DATA_GUNTUR_NEW_DATA.xlsx")
print(len(df))


df['Name'] = df['Names'].astype(str)
df['Name'] = df['Name'].str.strip()
def add_space_in_dot(name):
    if "." in name:
        name = name.replace("."," ")
        return name
    else:
        return name
df['Name'] = df['Name'].apply(add_space_in_dot)

def extract_alphabets_and_spaces(values):
    value = str(values)
    return re.sub(r'[^a-zA-Z\s]', '', value)
# Apply the function to the "name" column
df['Name'] = df['Name'].apply(extract_alphabets_and_spaces)
df["Name"]=df["Name"].astype(str)
df["Name"]=df["Name"].str.lower()
def replace_z_with_s_q_with_k(input_string):
    # Replace both 'Z' and 'z' with 'S' and 's', respectively
    output_string = input_string.replace('z', 'j').replace('q', 'k')
    return output_string
df['Name'] = df['Name'].apply(replace_z_with_s_q_with_k)

def add_ph_in_f(name):
    if "f" in name:
        name = name.replace("f","ph")
        return name
    else:
        return name
df['Name'] = df['Name'].apply(add_ph_in_f)
df['Name'] = df['Name'].astype(str)
df['Name'] = df['Name'].str.lower()

# Define a function to transliterate English names to Telugu
def transliterate_to_telugu(name):
    telugu_name = sanscript.transliterate(name, sanscript.ITRANS, sanscript.TELUGU)
    return telugu_name
# Apply the transliteration function to the 'Names' column and create a new 'Telugu_Names' column

# Apply the conversion where Telugu_Names is empty
# df['Telugu_Names'] = df.apply(lambda row: transliterate_to_telugu(row['Names']) if row['Telugu_Names'] == '' else row['Telugu_Names'], axis=1)
df['Telugu_Names'] = df.apply(lambda row: transliterate_to_telugu(row['Name']) if pd.isna(row['Telugu_Names']) else row['Telugu_Names'], axis=1)

print(df.columns)
df = df[["Names","Telugu_Names","Mobile"]]
df.to_excel("Telugu_conversion.xlsx",index = False)
