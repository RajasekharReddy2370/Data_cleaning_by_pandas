import pandas as pd
import os
import re

main_file_path = "/home/rajashekar/Desktop/sec"
files = os.listdir(main_file_path)

c = 0

concat_df = pd.DataFrame()

for file in files:
    # print(file)
    constituency = file.split(".")[0]
    c = c+1
    print(c,file)
    df = pd.read_excel(main_file_path+'/'+file,usecols=["Names","Mobile"])
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
    df = df[df['Mobile'].str.isdigit()]
    df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
    df['Mobile'] = df['Mobile'].apply(lambda x: x[:] if x.startswith(('2','4','6', '7', '8', '9')) and len(x) == 10 else None)

    df = df[["Names","Mobile"]]
    # df["Mobile"] = df["Mobile"].astype(int)
    df["Names"] = df["Names"].astype(str)
    df["Names"] = df["Names"].str.strip()
    df["Names"] = df["Names"].str.title()

    concat_df = pd.concat([concat_df,df],ignore_index=True)
    df.dropna(inplace=True)

    df["Mobile"] = df["Mobile"].astype(int)

    df.to_excel(f"/home/rajashekar/Desktop/SECUNDERABAD_IMPORTED_CLEANED_DATA/SECUNDERABAD_IMPORTED_CLEANED_DATA_original/{constituency}_original.xlsx",index = False)

    print("origggggggggggggggggggggggggggggggggggggggggggggginal",len(df))

    print("\U0001F600")

    df.drop_duplicates(subset=["Mobile"],inplace = True)

    df.to_excel(f"/home/rajashekar/Desktop/SECUNDERABAD_IMPORTED_CLEANED_DATA/SECUNDERABAD_IMPORTED_CLEANED_DATA_unique/{constituency}_original.xlsx",index = False)

    print("UNIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIQ",len(df))
    print(df)
    # break

print(len(concat_df))

# concat_df["Mobile"] = concat_df["Mobile"].astype(int)
concat_df["Names"] = concat_df["Names"].astype(str)
concat_df["Names"] = concat_df["Names"].str.strip()
concat_df["Names"] = concat_df["Names"].str.title()

concat_df.dropna(inplace = True)

concat_df["Mobile"] = concat_df["Mobile"].astype(int)

concat_df.drop_duplicates(subset=["Names","Mobile"],inplace=True)

concat_df.to_excel("/home/rajashekar/Desktop/SECUNDERABAD_IMPORTED_CLEANED_DATA/SECUNDERABAD_IMPORTED_CLEANED_DATA_MERGED_ORIGINAL.xlsx",index = False)

concat_df.drop_duplicates(subset=["Mobile"],inplace=True)

concat_df.to_excel("/home/rajashekar/Desktop/SECUNDERABAD_IMPORTED_CLEANED_DATA/SECUNDERABAD_IMPORTED_CLEANED_DATA_MERGED_unique.xlsx",index = False)





