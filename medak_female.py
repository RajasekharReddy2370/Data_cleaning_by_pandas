# import pandas as pd
# import time
# import os
# import re
# start_time = time.time()
#
# file_path = r"/home/rajashekar/Desktop/TS_CPU/Voter_MP_Data"
# all_folders = os.listdir(file_path)
# # pattern = r'^[6-9]\d{9}$'
# # constituency_name = 'Adilabad_7'
# for folder in all_folders:
#     print(folder)
#     if folder == 'Mahbubnagar_74':
#         files = os.path.join(file_path+'/'+folder)
#         print(files)
#         file_name = os.listdir(files)
#         concat_df = pd.DataFrame()
#
#         c = 0
#         for file in file_name:
#             print(file)
#             constituency = file
#             df = pd.read_excel(file_path + '/' + folder + '/' + file)
#             print(file_path + '/' + folder + '/' + file)
#             new_df = df.loc[:, ['First Name','Mobile', 'G']]
#
#             new_df = new_df[new_df['G'] == 'F']
#             selected_columns = ['First Name','Mobile', 'G']
#             result = new_df[selected_columns]
#             result.rename(columns = {'First Name':"Names"})
#
#             def add_space_in_dot(name):
#                 name = str(name)
#                 if "." in name:
#                     name = name.replace(".", " ")
#                     return name
#                 else:
#                     return name
#
#             result['First Name'] = result['First Name'].apply(add_space_in_dot)
#             result['First Name'] = result['First Name'].str.strip()
#             result = result[result['First Name'].str.strip() != ""]
#
#             def extract_alphabets_and_spaces(values):
#                 value = str(values)
#                 return re.sub(r'[^a-zA-Z\s]', '', value)
#
#             result['First Name'] = result['First Name'].apply(extract_alphabets_and_spaces)
#
#             result.dropna(subset=['Mobile'], inplace=True)
#             result.dropna(subset=['G'], inplace=True)
#             result.dropna(subset=['First Name'], inplace=True)
#
#             def clean_mobile_number(mobile):
#                 # Convert scientific notation to normal form
#                 if 'e' in str(mobile):
#                     mobile = "{:.0f}".format(mobile)
#                 # Remove ".0" if it exists at the end
#                 mobile_str = str(mobile)
#                 if mobile_str.endswith('.0'):
#                     mobile = mobile_str[:-2]
#                 return mobile
#
#             result['Mobile'] = result['Mobile'].apply(clean_mobile_number)
#             result['mobile'] = result['Mobile'].astype(str)
#             result = result[result['Mobile'].str.isdigit()]
#             result['Mobile'] = result['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
#             result['Mobile'] = result['Mobile'].apply(
#                 lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
#
#             result = result[['First Name','G', 'Mobile']]
#             result.dropna(subset=['Mobile'], inplace=True)
#             result.dropna(subset=['G'], inplace=True)
#             result.dropna(subset=['First Name'], inplace=True)
#             result.dropna(inplace = True)
#             result.drop_duplicates(subset=['Mobile'], ignore_index=True, inplace=True)
#             result = result[['First Name',"Mobile"]]
#             concat_df = pd.concat([concat_df,result],ignore_index=True)
#
#             print(result)
#             result.to_excel(f'/home/rajashekar/Desktop/Mahbubnagar_Female_Data/{constituency}_female_mobile_numbers.xlsx', index=False)
#             print("********************************************************************************unique", len(result))
#             print("Filed stored successfully....")
#             c = c+1
#             print('******************************************************************************************FILE_NO',c)
#
#
#         print(len(concat_df))
#
#         concat_df.drop_duplicates(subset=["Mobile"],inplace=True)
#         concat_df.dropna(inplace=True)
#         concat_df = concat_df[["Mobile"]]
#         print(len(concat_df))
#         concat_df.to_excel("/home/rajashekar/Desktop/Mahbubnagar_Female_Data/Mahbubnagar_MP_Female_Mobile_Numbers_Data.xlsx",index=False)
# end_time = time.time()
# print("time :",end_time-start_time)
# print('**********************************completed***********************************************',)

Gender = ['Gender']


import os
import pandas as pd

file_path = r"/home/rajashekar/Desktop/TS_CPU/Schemes/BD"
all_folders = os.listdir(file_path)

for folder in all_folders:
    if folder == 'Devarkadra_76':
        all_files_in_folder = os.listdir(file_path+'/'+folder)
        result_df = pd.DataFrame()
        for file in all_files_in_folder:
            print('file', file)
            if file.endswith('.xlsx'):
                try:
                    for i in range(1, 4):
                        df = pd.read_excel(file_path+'/'+folder+'/'+file, header=i)
                        print(file_path+'/'+folder+'/'+file)
                        print(df.columns)
                except:
                    pass
            if file.endswith('.csv'):
                try:
                    for i in range(1, 4):
                        df = pd.read_csv(file_path+'/'+folder+'/'+file, header=i)
                        print(file_path+'/'+folder+'/'+file)
                        print(df.columns)
                except:
                    pass


