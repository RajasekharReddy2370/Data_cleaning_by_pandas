import pandas as pd
import os

main_file_path = "/home/rajashekar/Desktop/AP_CPU/voter_MP_Data/Kakinada"
files = os.listdir(main_file_path)

concat_df = pd.DataFrame()
for file in files:
    df = pd.read_excel(main_file_path+'/'+file,usecols=["Mobile"])
    df.dropna(subset=["Mobile"],inplace=True)
    print(file,"oooooooooooooooooooooooooooooooooooooo",len(df))

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
    # print(len(df))
    df.dropna(inplace = True)
    df.drop_duplicates(subset=["Mobile"],inplace = True)
    print(df)
    print(file,"fffffffffffffffffffffffffffffF",len(df))
    concat_df = pd.concat([concat_df,df],ignore_index=True)

print(concat_df)
concat_df.drop_duplicates(subset=["Mobile"],inplace=True)
concat_df.to_excel('m_n.xlsx',index=False)
print(len(concat_df))






