import pandas as pd
import re


df = pd.read_excel(r"/home/rajashekar/Downloads/Guntur_west_85_PWD_cleaned.xlsx")
print(df.columns)
print(df.info())

new_df = df.copy()
# new_df = df.loc[:,["First Name", 'Last Name', 'Voter ID','Mobile']]
print(new_df)
new_df['LASTNAME_EN'] = new_df['LASTNAME_EN'].fillna('')
new_df['FM_NAME_EN'] = new_df['FM_NAME_EN'].astype(str)
new_df['LASTNAME_EN'] = new_df['LASTNAME_EN'].astype(str)
new_df['FM_NAME_EN'] = new_df['FM_NAME_EN'].str.strip()
new_df['LASTNAME_EN'] = new_df['LASTNAME_EN'].str.strip()
new_df['Names'] = new_df['FM_NAME_EN'] + ' ' + new_df['LASTNAME_EN']

new_df["Names"] = new_df["Names"].str.lower()
#
# new_df['RLN_L_NM_EN'] = new_df['RLN_L_NM_EN'].fillna('')
# new_df['RLN_FM_NM_EN'] = new_df['RLN_FM_NM_EN'].astype(str)
# new_df['RLN_L_NM_EN'] = new_df['RLN_L_NM_EN'].astype(str)
# new_df['RLN_FM_NM_EN'] = new_df['RLN_FM_NM_EN'].str.strip()
# new_df['RLN_L_NM_EN'] = new_df['RLN_L_NM_EN'].str.strip()
# new_df['RLN_FM_NM_ENG'] = new_df['RLN_FM_NM_EN'] + ' ' + new_df['RLN_L_NM_EN']
#
# new_df["RLN_FM_NM_ENG"] = new_df["RLN_FM_NM_ENG"].str.title()

DF = new_df[["B#","S","S#","House No","Names","RLN_FM_NM_ENG","Voter_id","G","RLN_TYPE","Age","Mobile","Address_eng","PINCODE",]]

DF["Address_eng"] = DF["Address_eng"].fillna("...............")

print(DF.columns)
print(DF)

DF.to_excel("GUNTUR_WEST_85A_PWD_DATA.xlsx",index = False)


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


result_df['Mobile'] = result_df['Mobile'].apply(clean_mobile_number)


# selected_columns = ['Full Name', 'Mobile','Voter ID' ]
# df = new_df[selected_columns]
# df = df.rename(columns={'Full Name': 'Names'})
# df.dropna(subset = ['Names','Mobile'], inplace = True)
# df.dropna(subset = ['Names'], inplace = True)
# def clean_mobile_number(mobile):
#     # Convert scientific notation to normal form
#     if 'e' in str(mobile):
#         mobile = "{:.0f}".format(mobile)
#     # Remove ".0" if it exists at the end
#     mobile_str = str(mobile)
#     if mobile_str.endswith('.0'):
#         mobile = mobile_str[:-2]
#     return mobile
# df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
# df['mobile'] = df['Mobile'].astype(str)
# df = df[df['Mobile'].str.isdigit()]
# df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
# df['Mobile'] = df['Mobile'].apply(lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
# df = df[['Names','Mobile','Voter ID']]
# df.dropna(inplace = True)
# df.drop_duplicates(subset = ['Names','Mobile'], inplace =True)
# df.drop_duplicates(subset = ['Mobile'], inplace =True)
#
# print(df)
# print(len(df))
#
# df.to_excel('cpt.xlsx',index = False)
