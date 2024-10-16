import pandas as pd
import os

main_folder_path = r"/home/rajashekar/Desktop/Data/hyd_sec"
files = os.listdir(main_folder_path)

concat_df = pd.DataFrame()
# constituency_lengths = {}
name = "Hyd_Sec_18_40_Age_group"
for file in files:
    df = pd.read_excel(main_folder_path + '/' + file, usecols=['Age', "Mobile"])
    # print(file)
    constituency = file.split('-')[0]

    age_filtered_df = df[(df['Age'] >= 18) & (df['Age'] <= 40)].copy()
    age_filtered_df.dropna(subset=['Age'], inplace=True)
    age_filtered_df.dropna(subset=['Mobile'], inplace=True)


    def clean_mobile_number(mobile):
        try:
            mobile_float = float(mobile)
            mobile = "{:.0f}".format(mobile_float)
        except ValueError:
            mobile = str(mobile)

        if mobile.endswith(".0"):
            mobile = mobile[:-2]

        return mobile


    age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(clean_mobile_number)
    age_filtered_df['Mobile'] = age_filtered_df['Mobile'].astype(str)
    age_filtered_df = age_filtered_df[age_filtered_df['Mobile'].str.isdigit()]
    age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(
        lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
    age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(
        lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)

    age_filtered_df.drop_duplicates(subset=["Mobile"], inplace=True)
    age_filtered_df.dropna(inplace=True)

    DF = age_filtered_df[["Mobile"]]
    concat_df = pd.concat([concat_df, DF], ignore_index=True)
    print(file, "-------------------------------------------------------", len(DF))

    # constituency_lengths[constituency] = len(DF)

# constituency_df = pd.DataFrame(list(constituency_lengths.items()), columns=['Constituency', 'Length'])
# constituency_df.to_excel('constituency_lengths.xlsx', index=False)

print("Overall State WITH DUPLICATES-----------------------------------------------",len(concat_df))
#
concat_df.drop_duplicates(subset=["Mobile"],inplace=True)
print("Overall State WITH out DUPLICATES-----------------------------------------------",len(concat_df))
print(concat_df)

l = len(concat_df)
if l > 1000000:
    first_part = concat_df.iloc[:1000000, :]
    second_part = concat_df.iloc[1000000:2000000, :]
    third_part = concat_df.iloc[2000000:3000000, :]
    fourth_part = concat_df.iloc[3000000:, :]

    first_file_path = f"{name}_1st_part.xlsx"
    first_part.to_excel(first_file_path, index=False)

    print("............................................first_part")

    second_file_path = f"{name}_2nd_part.xlsx"
    second_part.to_excel(second_file_path, index=False)
    print("............................................second_part")

    third_file_path = f"{name}_3rd_part.xlsx"
    third_part.to_excel(third_file_path, index=False)

    print("............................................third_part")

    fourth_file_path = f"{name}_4th_part.xlsx"
    fourth_part.to_excel(fourth_file_path, index=False)

    print("............................................four_part")
else:
    file_path = f"{name}.xlsx"
    concat_df.to_excel(file_path, index=False)
    print("*******************************************original file stored successfully")
# concat_df.to_excel('Telangana_18_30_Age_group_Mobile_Numbers.xlsx',index = False)