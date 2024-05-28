import pandas as pd
import time
import os
import re
start_time = time.time()

file_path = r"/home/rajashekar/Desktop/TS_CPU/Voter_MP_Data"
all_folders = os.listdir(file_path)
# pattern = r'^[6-9]\d{9}$'
# constituency_name = 'Adilabad_7'
for folder in all_folders:
    # print(folder)
    if folder == 'Medak_34':
        files = os.path.join(file_path+'/'+folder)
        # print(files)
        file_name = (os.listdir(files))
        concat_df_female = pd.DataFrame()
        # concat_df_male = pd.DataFrame()

        c = 0
        for file in file_name:
            print(file)
            constituency = file
            df = pd.read_excel(file_path + '/' + folder + '/' + file)
            print(file_path + '/' + folder + '/' + file)
            new_df = df.loc[:, ['First Name','Mobile', 'G','Voter ID']]

            new_df = new_df[new_df['G'] == 'F']
            selected_columns = ['First Name','Mobile', 'G','Voter ID']
            result = new_df[selected_columns]
            result.rename(columns = {'First Name':"Names",'Voter ID':'Voter_id'},inplace = True)

            def add_space_in_dot(name):
                name = str(name)
                if "." in name:
                    name = name.replace(".", " ")
                    return name
                else:
                    return name

            result['Names'] = result['Names'].apply(add_space_in_dot)
            result['Names'] = result['Names'].str.strip()
            result = result[result['Names'].str.strip() != ""]

            def extract_alphabets_and_spaces(values):
                value = str(values)
                return re.sub(r'[^a-zA-Z\s]', '', value)

            result['Names'] = result['Names'].apply(extract_alphabets_and_spaces)

            result.dropna(subset=['Mobile'], inplace=True)
            result.dropna(subset=['G'], inplace=True)
            result.dropna(subset=['Names'], inplace=True)
            result.dropna(subset=['Voter_id'], inplace=True)

            def clean_mobile_number(mobile):
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

            result['Mobile'] = result['Mobile'].apply(clean_mobile_number)

            result['mobile'] = result['Mobile'].astype(str)
            result = result[result['Mobile'].str.isdigit()]
            result['Mobile'] = result['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
            result['Mobile'] = result['Mobile'].apply(
                lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)

            result = result[['Names','G', 'Mobile','Voter_id']]
            result.dropna(subset=['Mobile'], inplace=True)
            result.dropna(subset=['G'], inplace=True)
            result.dropna(subset=['Names'], inplace=True)
            result.dropna(subset=['Voter_id'], inplace=True)
            result.dropna(inplace = True)
            result.drop_duplicates(subset=['Mobile'], ignore_index=True, inplace=True)
            result = result[['Names',"Mobile","G","Voter_id"]]
            print(result)
            # result = result[result['G'] == 'F']
            # count_F = result[result['G'] == 'F']['G'].count()

            concat_df_female = pd.concat([concat_df_female,result],ignore_index=True)
            # print(result)
            result.to_excel(f'/home/rajashekar/Desktop/Medak_Gender_Data/V_Females/{constituency}_Female_mobile_numbers.xlsx', index=False)
            print("********************************************************************************females_count", len(result))

            # result = result[result['G'] == 'M']
            # count_M = result[result['G'] == 'M']['G'].count()
            # df_M = pd.concat([concat_df_male,df_M],ignore_index=True)
            # print(result)
            # concat_df_male = pd.concat([concat_df_male,result],ignore_index=True)


            # result.to_excel(f'/home/rajashekar/Desktop/M_Fe_Ma_Data/Males/{constituency}_Male_mobile_numbers.xlsx', index=False)
            # print("********************************************************************************males_count", len(result))

            c = c+1
            print('******************************************************************************************',c)
            # break
        print(len(concat_df_female))
        #
        concat_df_female.drop_duplicates(subset=["Mobile"],inplace=True)
        concat_df_female.dropna(inplace=True)
        concat_df_female = concat_df_female[["Names","Mobile","Voter_id"]]
        print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO_FFFFFFFFFFFFff",len(concat_df_female))
        concat_df_female.to_excel("/home/rajashekar/Desktop/Medak_Gender_Data/Medak_MP_Voter_Female_Data.xlsx",index=False)
        #
        # print(len(concat_df_male))
        # concat_df_male.drop_duplicates(subset=["Mobile"], inplace=True)
        # concat_df_male.dropna(inplace=True)
        # concat_df_male = concat_df_male[["Names", "Mobile", "Voter_id"]]
        # print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO_MMMMMMMMMMMMMMMMMMMMMMM",len(concat_df_male))
        # concat_df_male.to_excel("/home/rajashekar/Desktop/Medak_Gender_Data/Medak_Mp_Gender_Data.xlsx", index=False)
        # concat_df_male.to_excel("/home/rajashekar/Desktop/M_Fe_Ma_Data/Mehbubnagar_Males_Mp_Data_from_Voters_Data.xlsx", index=False)
end_time = time.time()
print("time :",end_time-start_time)
print('**********************************completed***********************************************',)




