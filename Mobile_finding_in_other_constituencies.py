import pandas as pd
import os

main_file_path = "/home/rajashekar/Desktop/RAJA_LAPTOP/Telangana/TELANGANA/TELANGANA_MOBILE_NUMBERS_from_Drive_data_and_schemes/Beneficiary_Voter_Assembly_Constituency/Karimnagar"
files = os.listdir(main_file_path)


result_df = pd.DataFrame()
# constituency = main_file_path.split('/')[-1]
# constituency = "Medak"

c = 0
for file in files:

    print(file)
    filename = file.split('_')[0]

    df1 = pd.read_excel(main_file_path+'/'+file,usecols=["Mobile"])
    df2 = pd.read_excel(
        r"/home/rajashekar/Documents/Telangana_daily/Graduates_Names_and_Numbers_Medak_Nizamabad_Adilabad_Karimnagar.xlsx")

    # Merge dataframes on 'Mobile' column
    df_output = pd.merge(df2, df1, on='Mobile')

    # Add Filename column
    df_output['Filename'] = filename

    # Display output
    print(df_output)
    df_output.to_excel(f"/home/rajashekar/Documents/Telangana_daily/G3/{filename}.xlsx",index = False)


