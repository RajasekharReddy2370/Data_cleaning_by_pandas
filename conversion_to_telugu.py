import pandas as pd
from indic_transliteration import sanscript
import time
import re
start_time = time.time()

constituency = "output_telugu_conversion"
df = pd.read_excel(r"/home/rajashekar/Downloads/output (20).xlsx")
print(df.info())
df.dropna(subset = ['Names'],inplace=True)
df.dropna(subset = ['Mobile'],inplace=True)
# df.drop_duplicates(subset = ['Mobile'],ignore_index=True, inplace=True)
df.dropna(inplace=True)

def extract_alphabets_and_spaces(values):
    value = str(values)
    return re.sub(r'[^a-zA-Z\s]', '', value)
# Apply the function to the "name" column
df['Telugu_Names'] = df['Names'].apply(extract_alphabets_and_spaces)
df["Telugu_Names"]=df["Telugu_Names"].astype(str)
df["Telugu_Names"]=df["Telugu_Names"].str.lower()
def replace_z_with_s_q_with_k(input_string):
    # Replace both 'Z' and 'z' with 'S' and 's', respectively
    output_string = input_string.replace('z', 'j').replace('q', 'k')
    return output_string
df['Telugu_Names'] = df['Telugu_Names'].apply(replace_z_with_s_q_with_k)

def add_h_in_f(name):
    if "f" in name:
        name = name.replace("f","ph")
        return name
    else:
        return name
df['Telugu_Names'] = df['Telugu_Names'].apply(add_h_in_f)
df['Telugu_Names'] = df['Telugu_Names'].astype(str)
df['Telugu_Names'] = df['Telugu_Names'].str.lower()
# Function to transliterate English names to Telugu script
def transliterate_to_telugu(name):
    telugu_name = sanscript.transliterate(name, sanscript.ITRANS, sanscript.TELUGU)
    return telugu_name
# Apply the transliteration function to the 'Names' column and create a new 'Telugu_Names' column
df['Telugu_Names'] = df['Telugu_Names'].apply(transliterate_to_telugu)

df = df[['Names','Telugu_Names','Mobile']]

df = df[df["Names"].str.strip() != ""]

# df.drop_duplicates(subset=['Mobile'],inplace = True)

# df['Names']=df['Names'].astype(str)
# df['Names']=df['Names'].str.title()

df = df[['Names','Telugu_Names','Mobile']]
print(df)
print("final",df.info())
df.to_excel(f'{constituency}.xlsx',index = False)

# print("################################################CONSTITUENCY", constituency)

end_time  = time.time()
print(end_time-start_time)




