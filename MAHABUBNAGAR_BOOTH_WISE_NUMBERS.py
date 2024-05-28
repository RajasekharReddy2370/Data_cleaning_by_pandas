# import pandas as pd
#
# constituency = "JADCHERLA"
# df = pd.read_excel(r"/home/rajashekar/Desktop/TS_CPU/Voter_MP_Data/Mahbubnagar_74/Jadcherla-75-AC- iToC Voter Data.xlsx",usecols=["B#","First Name","Mobile"])
# df.rename(columns={"B#":"BOOTH","First Name":"Names"},inplace=True)
#
# df.dropna(subset=["Mobile"],inplace=True)
# df.dropna(subset=["Names"],inplace=True)
# df.drop_duplicates(subset=["Mobile"],inplace=True)
#
# df["Mobile"] = df["Mobile"].astype(str)
# df['Mobile'] = df['Mobile'].str.strip()
# df = df[df["Mobile"].str.strip() != ""]
#
# print(len(df))
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
# df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
# df['Mobile'] = df['Mobile'].astype(str)
# df = df[df['Mobile'].str.isdigit()]
# df['Mobile'] = df['Mobile'].apply(lambda x: x[3:] if len(x) > 10 and x.startswith('+91') else x)
# df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
# df['Mobile'] = df['Mobile'].apply(lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
#
# df.dropna(inplace=True)
#
# print("AFTER MOBILE VALIDATION#############################################",len(df))
# # df.to_excel("A1.xlsx",index = False)
#
# # Group by 'B#' column
# grouped = df.groupby('BOOTH').head(4)
# print(grouped)
# print(len(grouped))
# # #
# random_1000 = grouped.sample(n=1000, random_state=42)  # You can change the random_state if you want different random samples
# random_1000.sort_values(by = "BOOTH",ascending=True,inplace=True)
# print(random_1000)
# # #
# random_1000.to_excel(f'{constituency}_BOOTH_WISE_MOBILE_NUMBERS.xlsx',index = False)

import pandas as pd
import os

main_file_path = "/home/rajashekar/Documents/MAHBUNNAGAR_BOOTH_WISE_DATA"
files = os.listdir(main_file_path)
result_df = pd.DataFrame()
for file in files:
    print(file)

    df = pd.read_excel(main_file_path+'/'+file)
    result_df = pd.concat([result_df,df],ignore_index=True)

print(result_df)
result_df.sort_values(by = "BOOTH",ascending=True,inplace=True)
result_df.to_excel("MAHABUBNAGAR_BOOTH_WISE_MP_DATA.xlsx",index=False)
# print(len(result_df))

