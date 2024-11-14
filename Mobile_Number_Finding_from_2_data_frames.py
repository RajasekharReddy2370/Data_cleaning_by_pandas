#########################3 FINDING OF MOBILE NUMBERS WHCH ARE NOT PRERSENT IN DF1  #####################################


import pandas as pd

df1 = pd.read_excel(r"/home/rajashekar/Documents/Telangana_daily/Graduates/Graduates_Names_and_MobileNumbers.xlsx",usecols=["Mobile"])
df2 = pd.read_excel(r"/home/rajashekar/Desktop/RAJA_LAPTOP/Telangana/TELANGANA/IMPORTED_DATA/IMPORTED_DATA_CLEANED/KARIMNAGAR/Karimnagar_teachers_mobile_numbers.xlsx",usecols = ["Mobile"])

mobile_not_in_df1 = df2[~df2['Mobile'].isin(df1['Mobile'])]

print(len(mobile_not_in_df1))

mobile_not_in_df1.to_excel("/home/rajashekar"
                           "/Documents/Telangana_daily/Graduate_Numbers_which_having_No_Names.xlsx",index = False)