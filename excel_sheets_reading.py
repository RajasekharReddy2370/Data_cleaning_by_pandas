# import pandas as pd
#
# # Load Excel file
# excel_file = "/home/rajashekar/Desktop/MALKAJGIRI_IMPORTED_DATA/mutation pending total 19000 above.xlsx"
#
# # Dictionary to store data from different sheets
# data_dict = {}
#
# # Read each sheet
# xls = pd.ExcelFile(excel_file)
# for sheet_name in xls.sheet_names:
#     # Read only "Names" and "Mobile" columns
#     df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=["Names", "Mobile"])
#     # Store data in the dictionary
#     data_dict[sheet_name] = df
#
# # Print data from each sheet
# for sheet_name, df in data_dict.items():
#     print(f"Sheet: {sheet_name}")
#     print(df)
#     print("\n")

import pandas as pd

# Load Excel file
excel_file = "/home/rajashekar/Desktop/MALKAJGIRI_IMPORTED_DATA/PENSION REPORT-22-1.xlsx"

# List to store dataframes from different sheets
dfs = []

# Read each sheet and append to the list
xls = pd.ExcelFile(excel_file)
for sheet_name in xls.sheet_names:
    # Read only "Names" and "Mobile" columns
    df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=["Names", "Mobile"])
    dfs.append(df)

# Concatenate dataframes
concatenated_df = pd.concat(dfs, ignore_index=True)

# Print concatenated dataframe
print(concatenated_df)
concatenated_df.to_excel("Pension_Report.xlsx",index = False)



xls =pd.ExcelFile(r"/home/rajashekar/Downloads/Final.xlsx")
dfs=[]
for sheet in xls.sheet_names:
    df = pd.read_excel(xls,sheet_name=sheet,usecols=["Names",["Mobile"])
    print(df)


