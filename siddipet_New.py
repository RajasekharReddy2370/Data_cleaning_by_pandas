# import pandas as pd
# import time
# start_time = time.time()
#
# name = 'Narayanraopet VIllage Kuttu Machina List 06.03.2024 (1)'
# # Replace 'your_excel_file.xlsx' with the path to your Excel file
# df = pd.read_excel('/home/rajashekar/Downloads/siddipet_new/Narayanraopet VIllage Kuttu Machina List 06.03.2024 (1).xlsx',header = 1)
#
# print(df.columns)
# df = df.loc[:, ['Benefeciary Name', 'Phone Num']]
# df.rename(columns={'Benefeciary Name':'Names','Phone Num': 'Mobile'}, inplace=True)
#
# print("**************************************************************",len(df))
# print(df)
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
# df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
# df['Mobile'] = df['Mobile'].astype(str)
# df = df[df['Mobile'].str.isdigit()]
# df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
# df['Mobile'] = df['Mobile'].apply( lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
#
# df.dropna(inplace = True)
# df.drop_duplicates(subset = ['Names','Mobile'],inplace  =True)
# df.drop_duplicates(subset = ['Mobile'],inplace  =True)
# print("*********************************************************",len(df))
# print(df)
# df.to_excel(f'/home/rajashekar/Downloads/siddipet_new_cleaned/{name}.xlsx',index = False)
# end_time = time.time()
# print(end_time-start_time)

import pandas as pd

df= pd.read_excel(r"/home/rajashekar/Desktop/AP_CPU/MOBILE_NUMBERS/MP/Araku/Araku_voter_Mp_Mobile_Numbers.xlsx")
# print(len(df1))
# df2 = pd.read_excel(r"/home/rajashekar/Desktop/TS_CPU/Siddipet_15_files_data.xlsx")
# print(len(df2))
#
# df = pd.concat([df1,df2],ignore_index=True)
# print(len(df))
#
# df.drop_duplicates(subset=["Mobile"],inplace=True)
# print(len(df))
#
# df.to_excel("SIDDIPET.xlsx", index = False)

df["Mobile"] = df["Mobile"].astype(str)
filtered_df = df[df['Mobile'].str.len() == 10]

filtered_df.to_excel("/home/rajashekar/Desktop/AP_CPU/MOBILE_NUMBERS/MP/Araku/Araku_voter_Mp_Mobile_Numbers_cleaned.xlsx")
