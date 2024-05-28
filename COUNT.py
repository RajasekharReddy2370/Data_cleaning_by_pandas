import pandas as pd
import os

main_file_path = "/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Machilipatnam_imported_Data/constituencies_To_be_cleaned/imported_Data_concat"
files = os.listdir(main_file_path)
cdf = pd.DataFrame()
for file in files:
    f = file.split('_')[0]
    # print(file)
    # constituency = file.split('.')[0]
    # print(main_file_path+'/'+file)
    df = pd.read_excel(main_file_path+'/'+file)

    # def replace_dot_with_space(value):

    # df["Names"] = df["Names"].astype(str)
    # df["Names"] = df["Names"].str.strip()
    # df["Names"] = df["Names"].str.title()
    #
    #
    # df["Telugu_Names"] = df["Telugu_Names"].astype(str)
    # df["Telugu_Names"] = df["Telugu_Names"].str.strip()
    cdf = pd.concat([cdf,df],ignore_index=True)
    # df.to_excel(f"/home/rajashekar/Desktop/chevella/{constituency}.xlsx",index=False)

    print(f,"ORIGINAL LENGTH ...................................", len(df))
#
# print(len(cdf))
# cdf.drop_duplicates(subset=["Mobile"],inplace=True)
# print(len(cdf))


# import pandas as pd
#
# # Assuming df is your DataFrame with columns [slno, District, Mandal, Panchayat, name, FatherName, Mobile]
# df = pd.read_excel(r"/home/rajashekar/Downloads/SERP Employees all data MPC.xlsx")
# # Group the DataFrame by 'District', 'Mandal', and 'Panchayat', and count the rows in each group
# counts = df.groupby(['District', 'Mandal', 'Panchayat']).size().reset_index(name='Count')
#
# # Print the result
# print(counts)
#
# counts.to_excel("Count.xlsx",index = False)

# import pandas as pd
#
# # Assuming df is your DataFrame with columns [slno, District, Mandal, Panchayat, name, FatherName, Mobile]
# df = pd.read_excel(r"/home/rajashekar/Downloads/SERP Employees all data MPC.xlsx")
# print(df.columns)
# # Group the DataFrame by 'District', 'Mandal', and 'Panchayat', and count the rows in each group
# counts = df.groupby(['District', 'Mandal', 'Panchayat']).agg(
#     Count=('Sl. No.', 'count'),
#     slno=('Sl. No.', 'first'),
#     name=( 'Name', 'first'),
#     FatherName=('Father/Husband Name', 'first'),
#     Mobile=('Phone No', 'first')
# ).reset_index()
#
# # Print the result
# print(counts)
# counts.to_excel('M_c_a.xlsx',index = False)

# import pandas as pd
#
# # Assuming df is your DataFrame with columns [slno, District, Mandal, Panchayat, name, FatherName, Mobile]
# df = pd.read_excel(r"/home/rajashekar/Downloads/SERP Employees all data MPC.xlsx")
# print(df.columns)
#
# # Group the DataFrame by 'District', 'Mandal', and 'Panchayat', and count the rows in each group
# df['Count'] = df.groupby(['District', 'Mandal', 'Panchayat'])['Sl. No.'].transform('count')
#
# # Print the DataFrame with the count column
# print(df)
# df.to_excel("Me_Co_all.xlsx",index  =False)


