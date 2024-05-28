import pandas as pd
import os

main_file_path = r"/home/rajashekar/Desktop/Mahbubnagar_Gender_Data/B_Females"
files = os.listdir(main_file_path)

for file in files:
    # print(file)
    df = pd.read_excel(main_file_path+'/'+file)
    print(file,len(df))

# import pandas as pd
# import os
#
# main_path = r"/home/rajashekar/Desktop/TS_CPU/BENEFICIARY_DATA_schemes/Medak/Medak_34"
# all_files = os.listdir(main_path)
# for file in all_files:
#     if file.endswith('.xlsx'):
#         try:
#             for i in range(1,4):
#                 df = pd.read_excel(main_path+'/'+file,header=i)
#                 fx = file.split('.')[0]
#                 print(fx)
#                 print(df.columns)
#         except Exception as e:
#             print("Exception",e)
#     if file.endswith('.csv'):
#         try:
#             for i in range(1,4):
#                 df = pd.read_csv(main_path+'/'+file,header = i,low_memory=False)
#                 fc = file.split('.')[0]
#                 print(fc)
#                 print(df.columns)
#         except Exception as e:
#             print("Exception",e)

import pandas as pd
import os

# main_path = r"/home/rajashekar/Desktop/TS_CPU/BENEFICIARY_DATA_schemes/Medak/Medak_34"
# all_files = os.listdir(main_path)
#
# for file in all_files:
#     if file.endswith('.xlsx'):
#         try:
#             df = pd.read_excel(main_path+'/'+file, header=None)  # No header specified, will read all data
#             fx = file.split('.')[0]
#             print(fx)
#             print(df.columns)
#         except Exception as e:
#             print("Exception", e)
#     elif file.endswith('.csv'):
#         try:
#             df = pd.read_csv(main_path+'/'+file, header=None, low_memory=False)  # No header specified, will read all data
#             fc = file.split('.')[0]
#             print(fc)
#             print(df.columns)
#         except Exception as e:
#             print("Exception", e)

