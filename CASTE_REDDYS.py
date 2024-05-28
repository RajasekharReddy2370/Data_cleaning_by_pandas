import pandas as pd
import os

main_file_path = "/home/rajashekar/Desktop/MAHBUBNAGAR_CASTE_WISE_DATA/Mahbubnagar_Beneficiary_Constituencies"
files = os.listdir(main_file_path)

for file in files:
    print(main_file_path+'/'+file)
    constituency = file.split('-')[0]
    df = pd.read_excel(main_file_path+'/'+file)

    print("ORIGINAL LENGTH ...................................",len(df))

    df["Names"] = df["Names"].astype(str)

    def add_space_in_dot(name):
        if "." in name:
            name = name.replace(".", " ")
        return name.strip()

    df['Names'] = df['Names'].apply(add_space_in_dot)

    common_Reddy_names = ['Reddy', 'Redd', 'Reddi', 'Redde', 'Redi', 'Redy','Red']
    common_reddy_names_lower = [name.lower() for name in common_Reddy_names]


    # Function to check if any part of the name matches the common SC/ST names
    def check_common_REDDYS(name):
        name_parts = name.split()
        for part in name_parts:
            if part.lower() in common_reddy_names_lower:
                return True
        return False

    # Apply the function to the "Names" column to create a boolean mask
    mask = df['Names'].apply(check_common_REDDYS)

    # Filter the DataFrame using the mask
    Reddy_df = df[mask].copy()  # Make a copy to avoid SettingWithCopyWarning

    # Convert "Names" column to title case
    Reddy_df.loc[:, "Names"] = Reddy_df["Names"].astype(str)

    # Convert "Names" column to title case
    Reddy_df.loc[:, "Names"] = Reddy_df["Names"].str.title()

    print("Reddys_length.............................", len(Reddy_df))

    Reddy_df.to_excel(f"/home/rajashekar/Desktop/MAHBUBNAGAR_CASTE_WISE_DATA/Mahbubnagar_Beneficiary_Reddys/{constituency}_Reddy_Data.xlsx",index = False)

##################################### SINGLE CNSTITUENCY ###############################################################
# # constituency = "Devarkadra"
#
# # Load the Excel file into a DataFrame
# file_path = r"/home/rajashekar/Desktop/M/Shadnagar_unique.xlsx"
# df = pd.read_excel(file_path)
# print("ORIGINAL LENGTH ...................................",len(df))
#
# df["Names"] = df["Names"].astype(str)
#
# def add_space_in_dot(name):
#     if "." in name:
#         name = name.replace(".", " ")
#     return name.strip()
#
# df['Names'] = df['Names'].apply(add_space_in_dot)
#
# common_Reddy_names = ['Reddy', 'Redd', 'Reddi', 'Redde', 'Redi', 'Redy','Red']
# common_reddy_names_lower = [name.lower() for name in common_Reddy_names]
#
#
# # Function to check if any part of the name matches the common SC/ST names
# def check_common_REDDYS(name):
#     name_parts = name.split()
#     for part in name_parts:
#         if part.lower() in common_reddy_names_lower:
#             return True
#     return False
#
# # Apply the function to the "Names" column to create a boolean mask
# mask = df['Names'].apply(check_common_REDDYS)
#
# # Filter the DataFrame using the mask
# Reddy_df = df[mask].copy()  # Make a copy to avoid SettingWithCopyWarning
#
# # Convert "Names" column to title case
# Reddy_df.loc[:, "Names"] = Reddy_df["Names"].astype(str)
#
# # Convert "Names" column to title case
# Reddy_df.loc[:, "Names"] = Reddy_df["Names"].str.title()
#
# print("Reddys_length.............................", len(Reddy_df))

# sc_st_df.to_excel(f"/home/rajashekar/Desktop/Mahbubnagar_sc_st_data/{constituency}_Reddy_Data.xlsx",index = False)
# NON_Reddy_df = df[~mask]
#
# # # Convert "Names" column to string type
# NON_Reddy_df.loc[:, "Names"] = NON_Reddy_df["Names"].astype(str)
#
# # Convert "Names" column to title case
# NON_Reddy_df.loc[:, "Names"] = NON_Reddy_df["Names"].str.title()
#
# print("Non_sc_st_length...........................................", len(NON_Reddy_df))
# NON_Reddy_df.to_excel(f"/home/rajashekar/Desktop/Mahbubnagar_sc_st_data/{constituency}_Non_Reddy_Data.xlsx",index = False)