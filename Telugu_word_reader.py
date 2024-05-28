import pandas as pd
import re

# Sample DataFrame
# data = {'Names': ['English త.ెలుగుSpecial', 'నామం.EnglishSpecial', 'తెలు గుOnly','తెలుగు.నామం']}
df = pd.read_excel(r"/home/rajashekar/Desktop/TS_CPU/TELANGANA_MP_EACH_CONSTITUENCY_VERIFIED_DATA/Medak/Medak_verified_Mp_Data.xlsx")

print(len(df))

df.dropna(subset=["Names"],inplace=True)
df.dropna(subset=["Telugu_Names"],inplace=True)
df.dropna(subset=["Mobile"],inplace=True)

# Function to extract Telugu characters
df["Names"] = df["Names"].astype(str)
df["Names"] = df["Names"].str.strip()
df["Names"] = df["Names"].str.title()

def replace_dot_with_space(words):
    word = str(words)
    word = word.replace(".",' ')
    return word

df["Telugu_Names"] = df["Telugu_Names"].apply(replace_dot_with_space)

def extract_telugu(text):
    telugu_chars = re.findall(r'[\u0C00-\u0C7F]+', text)
    return ''.join(telugu_chars)

# Apply the function to the 'Names' column
df['Telugu_Names'] = df['Telugu_Names'].apply(extract_telugu)

# Function to extract Telugu characters while preserving spaces
def extract_telugu_with_spaces(text):
    telugu_chars_with_spaces = re.findall(r'(?:[\u0C00-\u0C7F]+|\s)+', text)
    return ''.join(telugu_chars_with_spaces)

# Apply the function to the 'Names' column
df['Telugu_Names'] = df['Telugu_Names'].apply(extract_telugu_with_spaces)

df['Telugu_Names'] = df['Telugu_Names'].astype(str)
df['Telugu_Names'] = df['Telugu_Names'].str.strip()

df["Mobile"] = df["Mobile"].astype(str)

df = df[df['Mobile'].str.len() == 10]
df.dropna(subset=["Names"],inplace = True)
df.dropna(subset=["Telugu_Names"],inplace = True)
df.dropna(subset=["Mobile"],inplace = True)

print(df)

df.to_excel("/home/rajashekar/Desktop/TS_CPU/TELANGANA_MP_EACH_CONSTITUENCY_VERIFIED_DATA/Medak/Medak_verified_Mp_Data1.xlsx",index = False)
