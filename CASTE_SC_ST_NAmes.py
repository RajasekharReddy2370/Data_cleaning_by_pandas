# import pandas as pd
# import os
#
# main_file_path = "/home/rajashekar/Documents/Mahbubnagar_Nayak_STs_Datawith_Booth_and_Assembly_Number/Mahbubnagr_concat_Data.xlsx"
# files = os.listdir(main_file_path)
#
# for file in files:
#     print(main_file_path+'/'+file)
#     constituency = file.split('-')[0]
#     df = pd.read_excel(main_file_path+'/'+file)
#     print("ORIGINAL LENGTH ...................................", len(df))
#
#     df["Names"] = df["Names"].astype(str)
#
#
#     def add_space_in_dot(name):
#         if "." in name:
#             name = name.replace(".", " ")
#         return name.strip()
#
#
#     df['Names'] = df['Names'].apply(add_space_in_dot)
#
#     common_sc_st_names = ['Paanaavath', 'Kadar', 'Kanikar', 'Rupavath', 'Damaria', 'Patelia', 'Chavan', 'Karamtoth',
#                           'Depaavath',
#                           'Sahariya', 'Sejaavath', 'Vankdoth', 'Poosnamal', 'Minas', 'Khond', 'Adiyan', 'Dhanka',
#                           'Korra',
#                           'Halaavath', 'Undaavath', 'Nunsavath', 'Injraavath', 'Sabavat', 'VaderJhaad',
#                           'KeluthLavidiya',
#                           'Pawar', 'Nenaavath', 'Ranasoth', 'Kotas', 'Lokaavath', 'Gangaavath', 'Banoth', 'Inloth',
#                           'Jayt',
#                           'Khethaavath', 'Dumaavath', 'Paathloth', 'Tejaavath', 'Dharmasoth', 'Meraavath', 'Sangaavath',
#                           'Aivath', 'Phulia', 'Chaivoth', 'Lavhadiya', 'Raajavath', 'Meenas', 'Kunsoth', 'Sabdasoth',
#                           'Teraavath', 'Matya', 'Jhandavath', 'Bhils', 'Lavori', 'Bhutia', 'Sotki', 'Mudavath',
#                           'Raamavath', 'Ranavath', 'Ade', 'Degaavath', 'Meraajoth', 'Tuvar', 'Santhals', 'Eravallan',
#                           'Lepchas', 'Aade', 'Ghara', 'Bhagvaandas', 'Lunsavath', 'Lonaavath', 'Vadithya', 'Aaloth',
#                           'Pithaavath',
#                           'Jharapla', 'Pipaavath', 'Baanni', 'Todas', 'Khaatroth', 'Oraons', 'Dungaroth', 'Devsoth',
#                           'Barmaavath',
#                           'Kharia', 'Baanoth', 'Bhilavath', 'Ajmera', 'Bhaanaavath', 'Chauradiya', 'Goraam', 'Jaadhav',
#                           'Chauhan',
#                           'Kuntaavath', 'Paalthyaa', 'Vislaavath', 'Baadaavath', 'Bodaa', 'Nayak', 'Dhaaraavath',
#                           'Karnaavath',
#                           'Kaanaavath', 'Meghaavath', 'Mood', 'Jaajigiri', 'Gugloth', 'Tepaavath', 'Aamgoth',
#                           'Aranadan',
#                           'Loolaavath', 'Kagla', 'Mohandas', 'Rajuar', 'Kurra', 'Jadhav', 'Dheeravath', 'Kodaavath',
#                           'Salaavath',
#                           'Gadaba', 'Naik', 'Khilaavath', 'Pammar', 'Dungaavath', 'Bhojaavath', 'Raathla', 'Tarabaanni',
#                           'Maaloth',
#                           'Kumaavath', 'Irular', 'Pamaadiyaa', 'Jaatroth', 'Daanaavath', 'Aadoth', 'Kholavath',
#                           'Bharoth', 'Jaloth']
#
#     common_sc_st_names_lower = [name.lower() for name in common_sc_st_names]
#
#
#     # Function to check if any part of the name matches the common SC/ST names
#     def check_common_sc_st(name):
#         name_parts = name.split()
#         for part in name_parts:
#             if part.lower() in common_sc_st_names_lower:
#                 return True
#         return False
#
#     # Apply the function to the "Names" column to create a boolean mask
#     mask = df['Names'].apply(check_common_sc_st)
#
#     # Filter the DataFrame using the mask
#     sc_st_df = df[mask].copy()  # Make a copy to avoid SettingWithCopyWarning
#
#     # Convert "Names" column to title case
#     sc_st_df.loc[:, "Names"] = sc_st_df["Names"].astype(str)
#
#     # Convert "Names" column to title case
#     sc_st_df.loc[:, "Names"] = sc_st_df["Names"].str.title()
#
#     print("sc_st_length.............................", len(sc_st_df))
#     # sc_st_df.to_excel(f"/home/rajashekar/Desktop/MAHBUBNAGAR_CASTE_WISE_DATA/Mahbubnagar_Beneficiary_SC_ST/{constituency}_sc_st_Data.xlsx",index = False)
#     sc_st_df.to_excel("MHB_SCST_Data.xlsx",index = False)
#
############################################### FOR single constituency ###################################
import pandas as pd

# constituency = "Devarkadra"

# Load the Excel file into a DataFrame
file_path = r"/home/rajashekar/Documents/Mahbubnagar_Nayak_STs_Datawith_Booth_and_Assembly_Number/Mahbubnagr_concat_Data.xlsx"
df = pd.read_excel(file_path)
print("ORIGINAL LENGTH ...................................",len(df))

df["Names"] = df["Names"].astype(str)

def add_space_in_dot(name):
    if "." in name:
        name = name.replace(".", " ")
    return name.strip()

df['Names'] = df['Names'].apply(add_space_in_dot)

common_sc_st_names = ['Paanaavath', 'Kadar', 'Kanikar', 'Rupavath', 'Damaria', 'Patelia', 'Chavan', 'Karamtoth','Depaavath',
                     'Sahariya', 'Sejaavath', 'Vankdoth', 'Poosnamal', 'Minas', 'Khond', 'Adiyan', 'Dhanka', 'Korra',
                     'Halaavath', 'Undaavath', 'Nunsavath', 'Injraavath', 'Sabavat', 'VaderJhaad', 'KeluthLavidiya',
                     'Pawar', 'Nenaavath', 'Ranasoth', 'Kotas', 'Lokaavath', 'Gangaavath', 'Banoth', 'Inloth', 'Jayt',
                     'Khethaavath', 'Dumaavath', 'Paathloth', 'Tejaavath', 'Dharmasoth', 'Meraavath', 'Sangaavath',
                     'Aivath', 'Phulia', 'Chaivoth', 'Lavhadiya', 'Raajavath', 'Meenas', 'Kunsoth', 'Sabdasoth',
                     'Teraavath', 'Matya', 'Jhandavath', 'Bhils', 'Lavori', 'Bhutia', 'Sotki', 'Mudavath',
                     'Raamavath', 'Ranavath', 'Ade', 'Degaavath', 'Meraajoth', 'Tuvar', 'Santhals', 'Eravallan',
                     'Lepchas', 'Aade', 'Ghara', 'Bhagvaandas', 'Lunsavath', 'Lonaavath', 'Vadithya', 'Aaloth', 'Pithaavath',
                     'Jharapla', 'Pipaavath', 'Baanni', 'Todas', 'Khaatroth', 'Oraons', 'Dungaroth', 'Devsoth', 'Barmaavath',
                     'Kharia', 'Baanoth', 'Bhilavath', 'Ajmera', 'Bhaanaavath', 'Chauradiya', 'Goraam', 'Jaadhav', 'Chauhan',
                     'Kuntaavath', 'Paalthyaa', 'Vislaavath', 'Baadaavath', 'Bodaa', 'Nayak', 'Dhaaraavath', 'Karnaavath',
                     'Kaanaavath', 'Meghaavath', 'Mood', 'Jaajigiri', 'Gugloth', 'Tepaavath', 'Aamgoth', 'Aranadan',
                     'Loolaavath', 'Kagla', 'Mohandas', 'Rajuar', 'Kurra', 'Jadhav', 'Dheeravath', 'Kodaavath', 'Salaavath',
                     'Gadaba', 'Naik', 'Khilaavath', 'Pammar', 'Dungaavath', 'Bhojaavath', 'Raathla', 'Tarabaanni', 'Maaloth',
                     'Kumaavath', 'Irular', 'Pamaadiyaa', 'Jaatroth', 'Daanaavath', 'Aadoth', 'Kholavath', 'Bharoth', 'Jaloth']



common_sc_st_names_lower = [name.lower() for name in common_sc_st_names]

# Function to check if any part of the name matches the common SC/ST names
def check_common_sc_st(name):
    name_parts = name.split()
    for part in name_parts:
        if part.lower() in common_sc_st_names_lower:
            return True
    return False

# Apply the function to the "Names" column to create a boolean mask
mask = df['Names'].apply(check_common_sc_st)

# Filter the DataFrame using the mask
sc_st_df = df[mask].copy()  # Make a copy to avoid SettingWithCopyWarning

# Convert "Names" column to title case
sc_st_df.loc[:, "Names"] = sc_st_df["Names"].astype(str)

# Convert "Names" column to title case
sc_st_df.loc[:, "Names"] = sc_st_df["Names"].str.title()

print("sc_st_length.............................", len(sc_st_df))
sc_st_df.to_excel("MHB_SCST_Data.xlsx",index = False)


# sc_st_df.to_excel(f"/home/rajashekar/Desktop/Mahbubnagar_sc_st_data/{constituency}_sc_st_Data.xlsx",index = False)
# non_sc_st_df = df[~mask]
#
# # # Convert "Names" column to string type
# non_sc_st_df.loc[:, "Names"] = non_sc_st_df["Names"].astype(str)
#
# # Convert "Names" column to title case
# non_sc_st_df.loc[:, "Names"] = non_sc_st_df["Names"].str.title()
#
# print("Non_sc_st_length...........................................", len(non_sc_st_df))
# non_sc_st_df.to_excel(f"/home/rajashekar/Desktop/Mahbubnagar_sc_st_data/{constituency}_Non_sc_st_Data.xlsx",index = False)
