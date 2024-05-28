
import pandas as pd
import re
#
# constituency = "Zahirabad"

# df1 = pd.read_excel(r"/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/Beneficiary_Voter_Mp_Constituency/Zahirabad/Zahirabad_MP_Mobile_Numbers_Part1.xlsx")
# df2 = pd.read_excel(r"/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/Beneficiary_Voter_Mp_Constituency/Zahirabad/Zahirabad_MP_Mobile_Numbers_Part2.xlsx")
# df = pd.concat([df1,df2],ignore_index=True)
df = pd.read_excel(r"/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Mahbubnagar/Mahbubnagar_from_Final_MBNR_PBC/Mahbubnagar_karyakarthalu.xlsx")
print(df.columns)
# df.rename(columns={"MOBILE":"Mobile"},inplace = True)
df.dropna(subset=["Mobile"],inplace=True)
print(len(df))

df["Names"] = df["Names"].str.lower()

def add_space_in_dot(names):
    name = str(names)
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
df['Mobile'] = df['Mobile'].apply(
    lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
df = df[df["Mobile"].notna()]  # Remove rows where Mobile is None

DFs = df[["Mobile"]].copy()
# DFs["Names"] = DFs["Names"].astype(str)
# DFs["Names"] = DFs["Names"].str.strip()
# DFs["Names"] = DFs["Names"].str.title()
# DFs.dropna(subset=["Names"], inplace=True)
DFs.dropna(subset=["Mobile"], inplace=True)
DFs.dropna(inplace=True)
# DFs.drop_duplicates(subset = ["Names","Mobile"],inplace = True)
DFs.drop_duplicates(subset = ["Mobile"],inplace = True)


# df["Mobile"] = df["Mobile"].astype(int)

# print(len(df))
# df.to_excel('ss2.xlsx',index=False)
# df.drop_duplicates(subset=["Mobile"],inplace=True)
# df.dropna(subset=["Mobile"],inplace = True)
# print(len(df))
# print(df)
DFs.to_excel("/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Mahbubnagar/Mahbubnagar_from_Final_MBNR_PBC/Mahbubnagar_karyakarthalu_cleaned.xlsx",index = False)

# df.to_excel("/home/rajashekar/Desktop/AP_CPU/MOBILE_NUMBERS/MP/Bapatla/Bapatla_voter_Mp_Mobile_Numbers.xlsx")
#
# l = len(df)
# # print("After droping of duplicate rows",l)
# if l > 1000000:
#     first_part = df.iloc[:1000000, :]
#     second_part = df.iloc[1000001:, :]
#
#     first_file_path = f"/home/rajashekar/Desktop/AP_CPU/MOBILE_NUMBERS/MP/Bapatla/Bapatla_voter_Mp_Mobile_Numbers.xlsx{constituency}_MP_Mobile_Numbers_Part1_cleaned.xlsx"
#     first_part.to_excel(first_file_path, index=False)
#
#     print("............................................first_part")
#
#     second_file_path = f"/home/rajashekar/Desktop/AP_CPU/MOBILE_NUMBERS/MP/Bapatla/Bapatla_voter_Mp_Mobile_Numbers.xlsx{constituency}_MP_Mobile_Numbers_Part2_cleaned.xlsx"
#     second_part.to_excel(second_file_path, index=False)
#     print("............................................second_part")
# else:
#     file_path = f"/home/rajashekar/Desktop/AP_CPU/MOBILE_NUMBERS/MP/Bapatla/Bapatla_voter_Mp_Mobile_Numbers.xlsx{constituency}_MP_Mobile_Numbers_cleaned.xlsx"
#     df.to_excel(file_path, index=False)
#     print("*******************************************original file stored successfully")

# df.to_excel('ssss.xlsx',index=False)
# df = df[df["Mobile"].str.strip() != ""]
# df.dropna(subset=['Mobile'], inplace=True)
# df['Mobile'] = df['Mobile'].astype(int)