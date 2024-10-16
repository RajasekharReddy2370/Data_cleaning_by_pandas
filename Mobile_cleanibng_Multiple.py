import pandas as pd
import os
main_folder_path = "/home/rajashekar/Documents/Telangana_daily/karimnagar_15/to_be_cleaned"

files = os.listdir(main_folder_path)

cdf = pd.DataFrame()

c = 0
for file in files:

    df = pd.read_excel(main_folder_path+'/'+file,usecols=["Mobile"])
    df = pd.read_excel(main_folder_path+'/'+file)
    print(df.columns)
    fil = file.split('.xlsx')[0]


    df.dropna(subset = ["Mobile"],inplace = True)
    print("ooooooooooooooooooooooooooooooooooooooooooooo",len(df))

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

    # print(len(df))
    df['Mobile'] = df['Mobile'].astype(str)
    df = df[df['Mobile'].str.isdigit()]
    df['Mobile'] = df['Mobile'].apply(lambda x: x[3:] if len(x) > 10 and x.startswith('+91') else x)
    # print(len(df))
    df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
    # print(len(df))
    df['Mobile'] = df['Mobile'].apply(lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
    df = df[df["Mobile"].notna()]
    df.drop_duplicates(subset=["Mobile"],inplace=True)
    c = c+1
    print(c,file,len(df))
    df.to_excel(f'/home/rajashekar/Documents/Telangana_daily/karimnagar_15/{fil}_cleaned.xlsx',index = False)
    cdf = pd.concat([cdf,df],ignore_index=True)
print(len(cdf))

cdf.drop_duplicates(subset=["Mobile"],inplace=True)
print(cdf)
print(len(cdf))

cdf["Mobile"] = cdf["Mobile"].astype(int)

cdf.to_excel('/home/rajashekar/Documents/Telangana_daily/karimnagar_15/Sangareddy_siddipet_Medak_cleaned.xlsx',index = False)