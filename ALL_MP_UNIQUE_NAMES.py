import pandas as pd
import time
import re
from indic_transliteration import sanscript

start_time = time.time()
print('start_time',start_time)

constituency = "TS_MP_ALL_UNIQUE"

df1 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Adilabad_7/Adilabad_7_Total_data.xlsx')
df2 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Bhongir_94/Bhongir_94_Total_data_part1.xlsx')
df3 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Bhongir_94/Bhongir_94_Total_data_part2.xlsx')
df4 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Chevella_53/Chevella_53_Total_data_part1.xlsx')
df5 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Chevella_53/Chevella_53_Total_data_part2.xlsx')
df6 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Hyderabad/Hyderabad_Total_data.xlsx')
df7 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Karimnagar_26/Karimnagar_26_Total_data_part1.xlsx')
df8 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Karimnagar_26/Karimnagar_26_Total_data_part2.xlsx')
df9 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Khammam_112/Khammam_112_Total_data.xlsx')
df10 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Mahabubabad_102/Mahabubabad_102_Total_data.xlsx')
df11 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Mahbubnagar_74/Mahbubnagar_74_Total_data.xlsx')
df12 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Malkajgiri_44/Malkajgiri_44_Total_data_part1.xlsx')
df13 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Malkajgiri_44/Malkajgiri_44_Total_data_part2.xlsx')
df14 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Medak_34/Medak_34_Total_data_part1.xlsx')
df15 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Medak_34/Medak_34_Total_data_part2.xlsx')
df16 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Nagarkurnool_81/Nagarkurnool_81_Total_data.xlsx')
df17 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Nalgonda_92/Nalgonda_92_Total_data_part1.xlsx')
df18 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Nalgonda_92/Nalgonda_92_Total_data_part2.xlsx')
df19 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Nizamabad/Nizamabad_Total_data.xlsx')
df20 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Peddapalle_25/Peddapalle_25_Total_data.xlsx')
df21 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Secunderabad_70/Secunderabad_70_Total_data.xlsx')
df22 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Warangal/Warangal_Total_data_part1.xlsx')
df23 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Warangal/Warangal_Total_data_part2.xlsx')
df24 = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/Beneficiary_voter_MP_data_unique/Zahirabad_38/Zahirabad_38_Total_data.xlsx')

df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24],ignore_index=True)
df = df.loc[:,['Names']]
print(df.columns)

df['Names'] = df['Names'].astype(str)
df['Names'] = df['Names'].str.lower()
df['Names'] = df['Names'].str.strip()
def add_space_in_dot(name):
    if "." in name:
        name = name.replace("."," ")
        return name
    else:
        return name
df['Names'] = df['Names'].apply(add_space_in_dot)

df['split_names'] = df['Names'].str.split()

split_names_list = df['split_names'].tolist()
all_names = [name for sublist in split_names_list for name in sublist]
unique_names = list(set(all_names))

unique_names_df = pd.DataFrame(unique_names,columns=['UNIQUE_NAME'])

# def add_space_in_dot(name):
#     if "." in name:
#         name = name.replace("."," ")
#         return name
#     else:
#         return name
# unique_names_df['UNIQUE_NAME'] = unique_names_df['UNIQUE_NAME'].apply(add_space_in_dot)

def extract_alphabets_and_spaces(values):
    value = str(values)
    return re.sub(r'[^a-zA-Z\s]', '', value)
unique_names_df["UNIQUE_NAME"] = unique_names_df['UNIQUE_NAME'].apply(extract_alphabets_and_spaces)
unique_names_df['UNIQUE_NAME'] = unique_names_df['UNIQUE_NAME'].str.strip()
unique_names_df = unique_names_df[unique_names_df["UNIQUE_NAME"].str.strip() != ""]

# Apply the function to the "name" column
unique_names_df["Telugu_Names"] = unique_names_df['UNIQUE_NAME'].apply(extract_alphabets_and_spaces)
unique_names_df["Telugu_Names"]=unique_names_df["Telugu_Names"].astype(str)
unique_names_df["Telugu_Names"]=unique_names_df["Telugu_Names"].str.lower()
def replace_z_with_s_q_with_k(input_string):
    # Replace both 'Z' and 'z' with 'S' and 's', respectively
    output_string = input_string.replace('z', 'j').replace('q', 'k')
    return output_string
unique_names_df['Telugu_Names'] = unique_names_df['Telugu_Names'].apply(replace_z_with_s_q_with_k)

def add_ph_in_f(name):
    if "f" in name:
        name = name.replace("f","ph")
        return name
    else:
        return name
unique_names_df['Telugu_Names'] = unique_names_df['Telugu_Names'].apply(add_ph_in_f)
unique_names_df['Telugu_Names'] = unique_names_df['Telugu_Names'].astype(str)
unique_names_df['Telugu_Names'] = unique_names_df['Telugu_Names'].str.lower()
# Function to transliterate English names to Telugu script
def transliterate_to_telugu(name):
    telugu_name = sanscript.transliterate(name, sanscript.ITRANS, sanscript.TELUGU)
    return telugu_name
# Apply the transliteration function to the 'Names' column and create a new 'Telugu_Names' column
unique_names_df['Telugu_Names'] = unique_names_df['Telugu_Names'].apply(transliterate_to_telugu)

unique_names_df['Hindi_Names'] = unique_names_df['UNIQUE_NAME'].apply(extract_alphabets_and_spaces)
unique_names_df["Hindi_Names"]=unique_names_df["Hindi_Names"].astype(str)
unique_names_df["Hindi_Names"]=unique_names_df["Hindi_Names"].str.lower()

def transliterate_to_hindi(name):
    return sanscript.transliterate(name, sanscript.ITRANS, sanscript.DEVANAGARI)
# Apply transliteration to create new column 'Hindi'
unique_names_df['Hindi_Names'] = unique_names_df['Hindi_Names'].apply(transliterate_to_hindi)

# df = df.drop(columns=['Telugu_Names'])
unique_names_df = unique_names_df[['UNIQUE_NAME','Telugu_Names','Hindi_Names',]]
unique_names_df.sort_values(by="UNIQUE_NAME")
print(len(unique_names_df))
l = len(unique_names_df)
if l > 1000000:
    first_part = unique_names_df.iloc[:1000000, :]
    second_part = unique_names_df.iloc[1000000:, :]

    first_file_path = f"{constituency}_1st_part.xlsx"
    first_part.to_excel(first_file_path, index=False)

    print("............................................first_part")

    second_file_path = f"{constituency}_2nd_part.xlsx"
    second_part.to_excel(second_file_path, index=False)
    print("............................................second_part")
else:
    file_path = f"{constituency}.xlsx"
    unique_names_df.to_excel(file_path, index=False)
    print("*******************************************original file stored successfully")
# unique_names_df.to_excel("ALL_MP_UNIQUE_NAMES.xlsx",index = False)

end_time = time.time()
print('end_time',end_time)
print("overall_time",end_time-start_time)



