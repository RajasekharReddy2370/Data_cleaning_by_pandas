import pandas as pd
import os
import re

main_file_path = "/home/rajashekar/Desktop/MALKAJGIRI_IMPORTED_DATA"
files = os.listdir(main_file_path)

MAHBUBNAGAR_DATA = pd.DataFrame()

c = 0
for file in files:
    print(file)
    constituency = file.split('.')[0]
    # print(main_file_path+'/'+file)
    c = c+1
    df = pd.read_excel(main_file_path+'/'+file,usecols=["Names","Mobile"])
    print("ORIGINAl_LENGTH",len(df))
    df.dropna(inplace = True)

    def add_space_in_dot(name):
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

    df['Names'] = df['Names'].str.strip()
    df = df[df["Names"].str.strip() != ""]

    def clean_mobile_number(mobile):
        # Convert scientific notation to normal form
        if 'e' in str(mobile):
            mobile = "{:.0f}".format(mobile)
        # Remove ".0" if it exists at the end
        mobile_str = str(mobile)
        if mobile_str.endswith('.0'):
            mobile = mobile_str[:-2]
        return mobile

    df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
    df['Mobile'] = df['Mobile'].astype('str')
    df['Mobile'] = df['Mobile'].str.strip()
    df = df[df['Mobile'].str.isdigit()]
    df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
    df['Mobile'] = df['Mobile'].apply(lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
    print("After_cleaning",len(df))

    df["Names"] = df["Names"].astype(str)
    df["Names"] = df["Names"].str.title()

    df = df[df["Names"].str.strip() != ""]
    df = df[df["Mobile"].str.strip() != ""]

    # df["Mobile"] = df["Mobile"].astype(int)

    print(df)
    df.to_excel(f"/home/rajashekar/Desktop/MALKAJGIRI_IMPORTED_DATA_CLEANED_FILES/MALKAJGIRI_IMPORTED_DATA_CLEANED_FILES_original/{constituency}.xlsx",index = False)

    df.drop_duplicates(subset=["Mobile"],inplace = True)

    df.to_excel(f"/home/rajashekar/Desktop/MALKAJGIRI_IMPORTED_DATA_CLEANED_FILES/MALKAJGIRI_IMPORTED_DATA_CLEANED_FILES_unique/{constituency}.xlsx",index = False)

    MAHBUBNAGAR_DATA = pd.concat([MAHBUBNAGAR_DATA,df],ignore_index=True)

    # break
print(c)
MAHBUBNAGAR_DATA.drop_duplicates(subset=["Names","Mobile"],inplace = True)

MAHBUBNAGAR_DATA.to_excel(f"/home/rajashekar/Desktop/MALKAJGIRI_IMPORTED_DATA_CLEANED_FILES/MAHBUBNAGAR_MERGED_DATA_ORIGINAL.xlsx",index = False)

MAHBUBNAGAR_DATA.drop_duplicates(subset=["Mobile"],inplace = True)

MAHBUBNAGAR_DATA.to_excel(f"/home/rajashekar/Desktop/MALKAJGIRI_IMPORTED_DATA_CLEANED_FILES/MAHBUBNAGAR_MERGED_DATA_UNIQUE.xlsx",index = False)

