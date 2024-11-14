import pandas as pd
import os

main_file_path = "/home/rajashekar/Desktop/All_states_data/Telangana/Beneficiary_Voter_Name_and_Mobile"
files = os.listdir(main_file_path)
cdf = pd.DataFrame()
constituency_lengths_Mobile = {}
numb = 0
for file in files:
    f = file.split('.')[0]
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
    C = len(df)
    # df.to_excel(f"/home/rajashekar/Desktop/chevella/{constituency}.xlsx",index=False)
    constituency_lengths_Mobile[f] = C
    numb += 1
    print(f,"ORIGINAL LENGTH ...................................", len(df),numb)

constituency_df_n_m = pd.DataFrame(list(constituency_lengths_Mobile.items()), columns=['Constituency', 'Length'])
constituency_df_n_m.to_excel('/home/rajashekar/Desktop/All_states_data/State_constituency_lengths/Name_and_Mobile/Telangana_constituency_lengths_Names_and_Mobile.xlsx', index=False)

cdf.drop_duplicates(subset = ["Names","Mobile"],inplace=True)
# cdf.drop_duplicates(subset = ["Mobile"],inplace=True)
print("CDF...........................................",len(cdf))

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


