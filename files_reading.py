import pandas as pd
import os

main_folder_path = "/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/Beneficiary_Voter_Assembly_Constituency"

folders = os.listdir(main_folder_path)
c = 0
concat_df = pd.DataFrame()

for folder in folders:

    # cdf = pd.DataFrame()

    # if folder != "raj":
    if folder == "Bhongir":
        print(folder)

        all_files_in_folder =  os.listdir(main_folder_path+'/'+folder)

        for file in all_files_in_folder:

            fil = file.split('_')[0]

            df = pd.read_excel(main_folder_path+'/'+folder+'/'+ file,usecols = ["Mobile"])
            df["Mobile"] = df["Mobile"].astype(str)
            filtered_df = df[df['Mobile'].str.len() == 10]
            print(fil,len(filtered_df))
            filtered_df.to_excel(f"/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/B_V_Assembly_Constituency/Bhongir/{fil}_Constituency_Mobile_Numbers.xlsx",index = False)

            # cdf = pd.concat([cdf,df],ignore_index=True)
            # print(len(df))
    # print(folder,len(cdf))

    # df = pd.read_excel(main_file_path+'/'+file,usecols=["Names","Telugu_Names","Mobile"])
    # print(df.columns)
    # concat_df = pd.concat([concat_df,df],ignore_index=True)
    # c+=1

# print(c)
# print(concat_df)
# concat_df.dropna(subset=["Names"],inplace = True)
# concat_df.dropna(subset=["Telugu_Names"],inplace = True)
# concat_df.dropna(subset=["Mobile"],inplace = True)
#
# concat_df["Names"] = concat_df["Names"].astype(str)
# concat_df["Names"] = concat_df["Names"].str.strip()
# concat_df["Names"] = concat_df["Names"].str.title()
#
# concat_df = concat_df[concat_df["Names"].str.strip() != ""]
# concat_df = concat_df[concat_df["Mobile"].str.strip() != ""]
#
# concat_df.drop_duplicates(subset=["Mobile"],inplace = True)
# concat_df.to_excel("MAHBUBNAGAR_CLEANED_CONSTITUENCIES_MP_DATA.xlsx",index = False)
