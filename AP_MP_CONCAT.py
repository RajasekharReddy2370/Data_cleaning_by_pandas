import pandas as pd
import os

main_file_path = "/home/rajashekar/Desktop/AP_CPU/CONSTITUENCY_ORIGINAL"
folders = os.listdir(main_file_path)
for folder in folders:
    print(folder)
    if folder == "Ongole":
        constituency = folder
        files_in_folder =os.listdir(main_file_path+'/'+folder)

        final_df = pd.DataFrame()
        for file in files_in_folder:
            print(main_file_path+'/'+folder+'/'+file)
            df = pd.read_excel(main_file_path+'/'+folder+'/'+file)

            final_df = pd.concat([final_df,df],ignore_index=True)

        print(final_df)
        print("ALL_CONCAT_DATA#######################################################",len(final_df))
        final_df["Names"] = final_df["Names"].astype(str)
        final_df["Names"] = final_df["Names"].str.lower()
        final_df.drop_duplicates(subset = ["Names","Mobile"],inplace=True)
        print("After dropping of duplicate rows ###########################################################",len(final_df))
        final_df.to_excel(f"/home/rajashekar/Desktop/AP_CPU/MP_ORIGINAL/Ongole/{constituency}_MP_ORIGINAL_DATA.xlsx",index=False)
        final_df.drop_duplicates(subset = ["Mobile"],inplace=True)
        final_df["Names"] = final_df["Names"].str.title()
        print("After dropping of duplicates################################################",len(final_df))
        final_df.to_excel(f"/home/rajashekar/Desktop/AP_CPU/MP_UNIQUE/Ongole/{constituency}_MP_UNIQUE_DATA.xlsx",index=False)











