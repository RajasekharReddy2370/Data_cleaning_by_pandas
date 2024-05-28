# import pandas as pd
# import os
# import re
#
# df = pd.read_excel("/home/rajashekar/Desktop/G_W_18_34_Data/GUNTUR_IMPORTED_DATA/Guntur West-94-AC- iToC Voter Data.xlsx",usecols=["Age","Mobile"])
#
# print(df.columns)
# age_filtered_df = df[(df['Age'] >= 18) & (df['Age'] <= 25)]
# print(age_filtered_df)
# age_filtered_df.dropna(inplace = True)
#
# def clean_mobile_number(mobile):
#     # Convert scientific notation to normal form
#     if 'e' in str(mobile):
#         mobile = "{:.0f}".format(mobile)
#     # Remove ".0" if it exists at the end
#     mobile_str = str(mobile)
#     if mobile_str.endswith('.0'):
#         mobile = mobile_str[:-2]
#     return mobile
#
# age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(clean_mobile_number)
# # age_filtered_df['Mobile'] = age_filtered_df['Mobile'].astype('str')
# age_filtered_df = age_filtered_df[age_filtered_df['Mobile'].str.isdigit()]
# age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
# age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(
#     lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
# print(len(age_filtered_df))
# age_filtered_df.drop_duplicates(subset=["Mobile"],inplace = True)
# print(len(age_filtered_df))

# print(len(df))
#
# df.dropna(inplace = True)
# df.drop_duplicates(subset=["Names","Mobile"],inplace = True)
# print(len(df))
# df.drop_duplicates(subset=["Mobile"],inplace = True)
# print(len(df))
#
# df["Names"] = df["Names"].astype(str)
# df["Names"] = df["Names"].str.strip()
# df["Names"] = df["Names"].str.title()
#
# df.to_excel("SATTENAPALLI_SCHEMES_FILE_UNIQUE_DATA.xlsx",index=False)
#
# print(df)

# import pandas as pd
#
# # Read the Excel file
# df = pd.read_excel("/home/rajashekar/Desktop/G_W_18_34_Data/GUNTUR_IMPORTED_DATA/Guntur West-94-B_(1-282)-AGE_ABOVE_80 (A4).xlsx", usecols=["Age", "Mobile"])
#
# # Filter the DataFrame to include only rows where the age is between 18 and 25
# age_filtered_df = df[(df['Age'] >= 18) & (df['Age'] <= 25)].copy()  # Make a copy to avoid SettingWithCopyWarning
#
# # Drop any NaN values in the 'Mobile' column
# age_filtered_df.dropna(subset=['Mobile'], inplace=True)
#
# # Define a function to clean mobile numbers
# def clean_mobile_number(mobile):
#     # Convert to string and remove any scientific notation
#     mobile_str = str(mobile).replace('e', '')
#     # Remove ".0" if it exists at the end
#     mobile_str = mobile_str.rstrip('.0')
#     return mobile_str
#
# # Apply the clean_mobile_number function to the 'Mobile' column
# age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(clean_mobile_number)
#
# # Filter out non-digit mobile numbers and fix formatting
# age_filtered_df["Mobile"] = age_filtered_df[age_filtered_df['Mobile'].str.isdigit()]  # Keep only digit mobile numbers
# age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)  # Remove '91' prefix
# age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)  # Keep only 10-digit numbers starting with 6, 7, 8, or 9
#
# # Drop duplicate mobile numbers
# age_filtered_df.drop_duplicates(subset=["Mobile"], inplace=True)
# age_filtered_df.dropna(inplace = True)
# age_filtered_df=age_filtered_df[["Mobile"]]
# # Print the length of the cleaned DataFrame
# # print("Length after cleaning:", len(age_filtered_df))
# # age_filtered_df = age_filtered_df[age_filtered_df["Mobile"]]
# age_filtered_df.to_excel("/home/rajashekar/Desktop/G_W_18_34_Data/G_W_Voter_Data2.xlsx",index = False)

#
# import pandas as pd
#
# # Read the Excel file
# df = pd.read_excel("/home/rajashekar/Desktop/G_W_18_34_Data/GUNTUR_IMPORTED_DATA/Guntur West-94-B_(1-282)-AGE_ABOVE_80 (A4).xlsx", usecols=["Age", "Mobile"])
#
# # Filter the DataFrame to include only rows where the age is between 18 and 25
# age_filtered_df = df[(df['Age'] >= 18) & (df['Age'] <= 28)].copy()  # Make a copy to avoid SettingWithCopyWarning
#
# # Drop any NaN values in the 'Mobile' column
# age_filtered_df.dropna(subset=['Mobile'], inplace=True)
#
# # Define a function to clean mobile numbers
# def clean_mobile_number(mobile):
#     # Convert to string and remove any scientific notation
#     mobile_str = str(mobile).replace('e', '')
#     # Remove ".0" if it exists at the end
#     mobile_str = mobile_str.rstrip('.0')
#     return mobile_str
#
# # Apply the clean_mobile_number function to the 'Mobile' column
# age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(clean_mobile_number)
#
# # Convert the 'Mobile' column back to string type
# age_filtered_df['Mobile'] = age_filtered_df['Mobile'].astype(str)
#
# # Filter out non-digit mobile numbers and fix formatting
# age_filtered_df = age_filtered_df[age_filtered_df['Mobile'].str.isdigit()]  # Keep only digit mobile numbers
# age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)  # Remove '91' prefix
# age_filtered_df['Mobile'] = age_filtered_df['Mobile'].apply(lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)  # Keep only 10-digit numbers starting with 6, 7, 8, or 9
#
# # Drop duplicate mobile numbers
# age_filtered_df.drop_duplicates(subset=["Mobile"], inplace=True)
# age_filtered_df.dropna(inplace=True)
#
# print(age_filtered_df)
#
# # age_filtered_df=age_filtered_df[["Mobile"]]
#
# # age_filtered_df.to_excel("/home/rajashekar/Desktop/G_W_18_34_Data/G_W_Voter_Data2.xlsx",index = False)

### Adding of new mobile Numbers to the old file ##################################
import pandas as pd
df1 = pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/G_W_94_DATA/GUNTUR_WEST_FINAL_DATA_UNIQUE/GUNTUR_WEST_94_FINAL_DATA.xlsx",usecols=["Mobile"])
df2 = pd.read_excel(r"")




