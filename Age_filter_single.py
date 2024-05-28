import pandas as pd
import re
# Read the Excel file
# df = pd.read_excel("/home/rajashekar/Desktop/AP_CPU/voter_MP_Data/Guntur/Guntur West-94-AC- iToC Voter Data.xlsx",usecols = ["First Name","Last Name","Mobile","Voter ID"])
# df = pd.read_excel("/home/rajashekar/Desktop/AP_CPU/voter_MP_Data/Guntur/Guntur West-94-AC- iToC Voter Data.xlsx",usecols = ["First Name","Last Name","Mobile","Voter ID","Age"])
df = pd.read_excel("/home/rajashekar/Desktop/AP_CPU/voter_MP_Data/Guntur/Guntur West-94-AC- iToC Voter Data.xlsx")
print(df.columns)
# print(len(df))
# new_df = df[(df['res_dfe'] >= 18) & (df['res_dfe'] <= 24)].copy()  # Make a copy to avoid SettingWithCopyWarning
new_df = df[df['Age'] >= 90].copy()  # Make a copy to avoid SettingWithCopyWarning
print(len(new_df))
new_df.to_excel("/home/rajashekar/Documents/Guntur_west_85_87_90/Guntur_West_above_90.xlsx",index = False)

print(len(new_df))
# new_df = df.loc[:, ['B#',"First Name", "Last Name", 'Mobile']]
# print(new_df)
#
new_df["Last Name"] = new_df["Last Name"].fillna('')
new_df["First Name"] = new_df["First Name"].astype(str)
new_df["Last Name"] = new_df["Last Name"].astype(str)
new_df["First Name"] = new_df["First Name"].str.strip()
new_df["Last Name"] = new_df["Last Name"].str.strip()
new_df['Names'] = new_df["First Name"] + ' ' + new_df["Last Name"]

new_df["Names"] = new_df["Names"].str.lower()

def add_space_in_dot(name):
    if "." in name:
        name = name.replace(".", " ")
        return name
    else:
        return name

new_df['Names'] = new_df['Names'].apply(add_space_in_dot)
#
def extract_alphabets_and_spaces(values):
    value = str(values)
    return re.sub(r'[^a-zA-Z\s]', '', value)
new_df['Names'] = new_df['Names'].apply(extract_alphabets_and_spaces)

new_df["Names"] = new_df["Names"].astype(str)
new_df["Names"] = new_df["Names"].str.strip()
new_df["Names"] = new_df["Names"].str.title()

# print(new_df)
res_df = new_df[["Names","Mobile","Voter ID"]]
print(res_df.columns)

# print(res_df)

#
# # Filter the DataFrame to include only rows where the res_dfe is between 18 and 25
# res_dfe_filtered_df = df[(df['res_dfe'] >= 18) & (df['res_dfe'] <= 28) & (df['G'] == 'F')].copy()  # Make a copy to avoid SettingWithCopyWarning
# # res_dfe_filtered_df = df[(df['res_dfe'] >= 18) & (df['res_dfe'] <= 28)].copy()  # Make a copy to avoid SettingWithCopyWarning
# # res_dfe_filtered_df = df[(df['res_dfe'] >= 18) & (df['res_dfe'] <= 28)].copy()  # Make a copy to avoid SettingWithCopyWarning
# res_dfe_filtered_df = res_df[(res_df['res_dfe'] >= 18) & (res_df['res_dfe'] <= 24)].copy()  # Make a copy to avoid SettingWithCopyWarning
#
# # # Drop any NaN values in the 'Mobile' column
#
res_df.dropna(subset=['Mobile'], inplace=True)
res_df['Mobile'] = res_df['Mobile'].astype(str)

def clean_mobile_number(mobil):
    mobile = str(mobil)
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
# res_df['Mobile'] = res_df['Mobile'].apply(clean_mobile_number)
#
res_df.loc[:, 'Mobile'] = res_df['Mobile'].apply(clean_mobile_number)

# # Convert the 'Mobile' column back to string type
res_df.loc[:,'Mobile'] = res_df['Mobile'].astype(str)
#
# # Filter out non-digit mobile numbers and fix formatting
res_df = res_df[res_df['Mobile'].str.isdigit()]  # Keep only digit mobile numbers
res_df['Mobile'] = res_df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)  # Remove '91' prefix
res_df['Mobile'] = res_df['Mobile'].apply(lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)  # Keep only 10-digit numbers starting with 6, 7, 8, or 9

# # Drop duplicate mobile numbers
# res_dfe_filtered_df.drop_duplicates(subset=["Mobile"], inplace=True)
res_df.dropna(inplace=True)
#

print(len(res_df))
# print(res_df)