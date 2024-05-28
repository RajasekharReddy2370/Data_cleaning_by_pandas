import pandas as pd
import re
df = pd.read_excel(r"/home/rajashekar/Documents/Shadnagar_Clean.xlsx")
print(len(df))

df["Names"] = df["Names"].astype(str)
df["Names"] = df["Names"].str.strip()
df["Names"] = df["Names"].str.title()
df.dropna(subset=["Mobile"],inplace=True)

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

# df["Mobile"] = df["Mobile"].astype(int)

df.dropna(subset=["Names"],inplace=True)
df.dropna(subset=["Mobile"],inplace=True)
df.dropna(inplace=True)

df.sort_values(by=["Names"],inplace=True)

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

df['Mobile'] = df['Mobile'].astype(str)
df = df[df['Mobile'].str.isdigit()]
print(len(df))
df['Mobile']=df['Mobile'].apply(lambda x : x[2:] if len(x)==12 and x.startswith('91') else x)
df['Mobile']=df['Mobile'].apply(lambda x : x[:] if x.startswith(('6','7','8','9')) and len(x)==10 else None)

print(len(df))

df.drop_duplicates(subset=["Mobile"],inplace=True)

print(len(df))
print(df)

df.to_excel("Shadnagar_Clean_file.xlsx",index = False)

# import pandas as pd
#
# df1 = pd.read_excel(r"/home/rajashekar/Documents/FESTIVALS_DATA/UGADI_CAMPAINING_DATA/SATTENAPALLI/SATTENAPALLI_CAMPAINING_DATA.xlsx",usecols = ["Names","Mobile"])
# df2 = pd.read_excel(r"/home/rajashekar/WORK/voters_prac/SATTENAPALLI_IMPORTANT_LEADERS_CLEANED_DATA.xlsx",usecols = ["Names","Mobile"])
# print(len(df1))
# print(len(df2))
# df = pd.concat([df1,df2],ignore_index=True)
# print(len(df))
#
# df["Names"] = df["Names"].astype(str)
# df["Names"] = df["Names"].str.strip()
# df["Names"] = df["Names"].str.title()
# df["Mobile"] = df["Mobile"].astype(int)
#
# df.drop_duplicates(subset=["Names","Mobile"],inplace=True)
# df.drop_duplicates(subset=["Mobile"],inplace=True)
# print(len(df))
# df.dropna(subset=["Names"],inplace=True)
# df.dropna(subset=["Mobile"],inplace=True)
# df.dropna(inplace=True)
#
# print("Final.................",len(df))
# df.to_excel("SATTENAPALLI_OVEALL_UPDATED_DATA.xlsx",index = False)