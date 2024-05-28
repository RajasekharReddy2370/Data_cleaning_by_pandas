import pandas as pd
import os
import re
main_file_path = r"/home/rajashekar/Desktop/AP_CPU/voter_MP_Data/Kakinada"
files = os.listdir(main_file_path)

concat_df = pd.DataFrame()
for file in files:
    df = pd.read_excel(main_file_path+'/'+file, usecols=['Age',"Mobile"])
    # df = pd.read_excel(main_file_path+'/'+file, usecols=["Age", "Mobile"])
    print(file)
    constituency = file.split('-')[0]
    # age_filtered_df = df[(df['Age'] >= 18) & (df['Age'] <= 28) & (df['G'] == 'F')].copy()  # Make a copy to avoid SettingWithCopyWarning
    # age_filtered_df = df[(df['gender'] == '2')].copy()  # Make a copy to avoid SettingWithCopyWarning

    # age_filtered_df = df[(df['Age'] >= 18) & (df['Age'] <= 25)].copy()  # Make a copy to avoid SettingWithCopyWarning
    age_filtered_df = df[(df['Age'] >= 40)].copy()  # Make a copy to avoid SettingWithCopyWarning

    # Drop any NaN values in the 'Mobile' column
    age_filtered_df.dropna(subset=['Mobile'], inplace=True)

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

    # Apply the clean_mobile_number function to the 'Mobile' column
    age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(clean_mobile_number)

    # Convert the 'Mobile' column back to string type
    age_filtered_df['Mobile'] = age_filtered_df['Mobile'].astype(str)

    # Filter out non-digit mobile numbers and fix formatting
    age_filtered_df = age_filtered_df[age_filtered_df['Mobile'].str.isdigit()]  # Keep only digit mobile numbers
    age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(
        lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)  # Remove '91' prefix
    age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(
        lambda x: x if x.startswith(('6', '7', '8', '9')) and len(
            x) == 10 else None)  # Keep only 10-digit numbers starting with 6, 7, 8, or 9

    # Drop duplicate mobile numbers
    age_filtered_df.drop_duplicates(subset=["Mobile"], inplace=True)
    age_filtered_df.dropna(inplace=True)
    DF = age_filtered_df[["Mobile"]]
    concat_df = pd.concat([concat_df,DF],ignore_index=True)
    # print(age_filtered_df)
    print(file,len(DF))
    # print(age_filtered_df)
    DF.to_excel(f"/home/rajashekar/Desktop/Andhra_State_Daily_data/Kakinada/Kakinada_40_above_age/{constituency}_From_40_Age_group.xlsx",index=False)

# print(len(concat_df))
#
concat_df.drop_duplicates(subset=["Mobile"],inplace=True)
print(len(concat_df))
print(concat_df)

concat_df.to_excel('/home/rajashekar/Desktop/Andhra_State_Daily_data/Kakinada/Kakinada_40_above_age/Kakinada_MP_From_40_Age_Group.xlsx',index = False)
# df2 = pd.read_excel(r"/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Mahbubnagar/Mahbubnagar_Beneficiary_Schemes_Mobile_Numbers/Mahbubnagar_Mp_Beneficiary_Mobiles.xlsx",usecols=["Mobile"])
# print(len(df2))
# c_df = pd.concat([concat_df,df2],ignore_index=True)
# print(len(c_df))
# c_df.drop_duplicates(subset=["Mobile"],inplace=True)
# print(len(c_df))

# c_df.to_excel('/home/rajashekar/Desktop/ThursDay_Meh_Med/Medak/Total_Females_Beneficiary_Voter.xlsx')

# #     break
# import pandas as pd
# # Read the Excel file
# # df = pd.read_excel("/home/rajashekar/Desktop/AP_CPU/voter_MP_Data/Guntur/Guntur West-94-AC- iToC Voter Data.xlsx",usecols = ["First Name","Last Name","Mobile","Voter ID"])
# df = pd.read_excel("/home/rajashekar/Desktop/AP_CPU/voter_MP_Data/Guntur/Guntur West-94-AC- iToC Voter Data.xlsx",usecols = ["First Name","Last Name","Mobile","Voter ID","Age"])
# print(df.columns)
# print(len(df))
# df.dropna(subset = ["Age"],inplace=True
#           )
#
# new_df = df[(df['Age'] >= 18) & (df['Age'] <= 25)].copy()  # Make a copy to avoid SettingWithCopyWarning
# #
# print(len(new_df))
# # new_df = df.loc[:, ['B#',"First Name", "Last Name", 'Mobile']]
# # print(new_df)
# #
# new_df["Last Name"] = new_df["Last Name"].fillna('')
# new_df["First Name"] = new_df["First Name"].astype(str)
# new_df["Last Name"] = new_df["Last Name"].astype(str)
# new_df["First Name"] = new_df["First Name"].str.strip()
# new_df["Last Name"] = new_df["Last Name"].str.strip()
# new_df['Names'] = new_df["First Name"] + ' ' + new_df["Last Name"]
#
# new_df["Names"] = new_df["Names"].str.lower()
#
# def add_space_in_dot(name):
#     if "." in name:
#         name = name.replace(".", " ")
#         return name
#     else:
#         return name
#
# new_df['Names'] = new_df['Names'].apply(add_space_in_dot)
# #
# def extract_alphabets_and_spaces(values):
#     value = str(values)
#     return re.sub(r'[^a-zA-Z\s]', '', value)
# new_df['Names'] = new_df['Names'].apply(extract_alphabets_and_spaces)
#
# new_df["Names"] = new_df["Names"].astype(str)
# new_df["Names"] = new_df["Names"].str.strip()
# new_df["Names"] = new_df["Names"].str.title()
#
# # print(new_df)
# ag = new_df[["Names","Mobile","Voter ID","Age"]]
# print(ag.columns)
#
# print(ag)
#
# #
# # # Filter the DataFrame to include only rows where the age is between 18 and 25
# # age_filtered_df = df[(df['Age'] >= 18) & (df['Age'] <= 28) & (df['G'] == 'F')].copy()  # Make a copy to avoid SettingWithCopyWarning
# # # age_filtered_df = df[(df['Age'] >= 18) & (df['Age'] <= 28)].copy()  # Make a copy to avoid SettingWithCopyWarning
# # # age_filtered_df = df[(df['Age'] >= 18) & (df['Age'] <= 28)].copy()  # Make a copy to avoid SettingWithCopyWarning
# # age_filtered_df = ag[(ag['Age'] >= 18) & (ag['Age'] <= 24)].copy()  # Make a copy to avoid SettingWithCopyWarning
# #
# # # # Drop any NaN values in the 'Mobile' column
# #
# ag.dropna(subset=['Mobile'], inplace=True)
# ag['Mobile'] = ag['Mobile'].astype(str)
#
# def clean_mobile_number(mobil):
#     mobile = str(mobil)
#     # Try to convert mobile to float to handle scientific notation and remove decimals
#     try:
#         mobile_float = float(mobile)
#         # Convert scientific notation to normal form and remove ".0" if it exists
#         mobile = "{:.0f}".format(mobile_float)
#     except ValueError:
#         # If conversion fails, it's likely already a string that doesn't need conversion
#         mobile = str(mobile)
#
#     # Remove any trailing ".0"
#     if mobile.endswith(".0"):
#         mobile = mobile[:-2]
#
#     return mobile
#
# # Apply the clean_mobile_number function to the 'Mobile' column
# # ag['Mobile'] = ag['Mobile'].apply(clean_mobile_number)
# #
# ag.loc[:, 'Mobile'] = ag['Mobile'].apply(clean_mobile_number)
#
# # # Convert the 'Mobile' column back to string type
# # ag['Mobile'] = ag['Mobile'].astype(str)
# #
# # # Filter out non-digit mobile numbers and fix formatting
# ag = ag[ag['Mobile'].str.isdigit()]  # Keep only digit mobile numbers
# ag['Mobile'] = ag['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)  # Remove '91' prefix
# ag['Mobile'] = ag['Mobile'].apply(lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)  # Keep only 10-digit numbers starting with 6, 7, 8, or 9
#
# # # Drop duplicate mobile numbers
# # age_filtered_df.drop_duplicates(subset=["Mobile"], inplace=True)
# ag.dropna(inplace=True)
# #
# print(ag)
# # ag.to_excel("Guntur_West_18_25_age_group_Data.xlsx",index = False)


