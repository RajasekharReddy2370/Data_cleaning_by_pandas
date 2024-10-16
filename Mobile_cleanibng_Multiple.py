import pandas as pd
import os
main_folder_path = "/home/rajasekharreddy/Documents/Telangana_daily/Gadwal_04/gadwal_database_numbers"

files = os.listdir(main_folder_path)

cdf = pd.DataFrame()

c = 0
for file in files:

    # df = pd.read_excel(main_folder_path+'/'+file,usecols=["Mobile","Age"])
    df = pd.read_csv(main_folder_path+'/'+file,usecols=["Phone_No"])
    fil = file.split('.xlsx')[0]

    df.dropna(subset = ["Phone_No"],inplace = True)
    # print("ooooooooooooooooooooooooooooooooooooooooooooo",len(df))

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

    df['Phone_No'] = df['Phone_No'].apply(clean_mobile_number)
    # print(len(df))
    df['Phone_No'] = df['Phone_No'].astype(str)
    df = df[df['Phone_No'].str.isdigit()]
    df['Phone_No'] = df['Phone_No'].apply(lambda x: x[3:] if len(x) > 10 and x.startswith('+91') else x)
    # print(len(df))
    df['Phone_No'] = df['Phone_No'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
    # print(len(df))
    df['Phone_No'] = df['Phone_No'].apply(lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
    # df = df[df["Mobile"].notna()]
    df.dropna(subset=["Phone_No"],inplace = True)
    df.drop_duplicates(subset=["Phone_No"],inplace=True)
    c = c+1
    df_mobile_only = df[['Phone_No']]
    df_mobile_only.to_excel(f'/home/rajasekharreddy/Documents/Telangana_daily/Gadwal_04/{fil}_cleaned_database.xlsx',index = False)
    # print(c,file,len(df_mobile_only))
    #
    # df_with_age = df.dropna(subset=["Age"])
    # df_with_age.to_excel(f'/home/rajasekharreddy/Documents/Andhra_Mobile_Numbers_with_Age/{fil}_cleaned.xlsx',index = False)
    # print(c,file,len(df_with_age))
    # if c == 1:
    #     break


#     cdf = pd.concat([cdf,df],ignore_index=True)
# print(len(cdf))
#
# cdf.drop_duplicates(subset=["Mobile"],inplace=True)
# print(cdf)
# print(len(cdf))
#
# cdf["Mobile"] = cdf["Mobile"].astype(int)
# cdf.to_excel('/home/rajashekar/Desktop/AP_CPU/zz_imported_data/Machilipatnam/concat_Data/All_files_concat_data.xlsx',index = False)