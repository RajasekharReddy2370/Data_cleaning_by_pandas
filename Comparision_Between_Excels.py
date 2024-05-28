import pandas as pd
import os
main_folder_path = "/home/rajashekar/Documents/Dubbak_1_25000_Beneficiary_schemes_mobile_Numbers"
files = os.listdir(main_folder_path)

excel_files = []
for file in files:
    excel_files.append(main_folder_path+'/'+file)

print(excel_files)

#
# # Load all excels into dataframes
# # excel_files = ["excel1.xlsx", "excel2.xlsx", "excel3.xlsx", "excel4.xlsx", "excel5.xlsx"]
# dfs = [pd.read_excel(file, usecols=["Mobile"]) for file in excel_files]
#
# # Find unique values in each dataframe
# unique_values = [set(df['Mobile']) for df in dfs]
#
# # Find values unique to each dataframe
# unique_to_each = [unique_values[i] - set.union(*[unique_values[j] for j in range(len(unique_values)) if j != i]) for i in range(len(unique_values))]
#
# # Print or save unique values for each excel
# for i, unique_values_in_excel in enumerate(unique_to_each):
#     print(f"Unique values in Excel {i+1}: {unique_values_in_excel}")
