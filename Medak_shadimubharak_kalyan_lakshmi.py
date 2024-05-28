import pandas as pd

constituency = 'Siddipet'

df1 = pd.read_csv(r"/home/rajashekar/WORK/TS_DATA/Schemes/BD/Siddipet_33/SIDDIPET_Kalyan Laxmi.csv")
df2 = pd.read_csv(r"/home/rajashekar/WORK/TS_DATA/Schemes/BD/Siddipet_33/SIDDIPET_Shadi Mubarak.csv")
print(df1.columns)
print(df2.columns)

print(len(df1))
print(len(df2))
df = pd.concat([df1[['Name of the Beneficiary', 'Phone Number']], df2[['Name of the Beneficiary', 'Phone Number']]], ignore_index=True)
df.rename(columns={'Phone Number': 'Mobile'}, inplace=True)
print(df)
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
df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
df['Mobile'] = df['Mobile'].apply( lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)

df.dropna(subset=['Mobile'],inplace=True)
df.drop_duplicates(subset=['Mobile'], ignore_index=True, inplace=True)
df = df[['Mobile']]
df.to_excel(f'/home/rajashekar/Desktop/Medak_shadimubarak_kalyanalakshmi/{constituency}.xlsx',index = False)
print("***********************************************************88",len(df))