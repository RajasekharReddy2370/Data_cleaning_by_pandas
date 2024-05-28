import os
from indic_transliteration import sanscript
import pandas as pd
import re
import time

start_time = time.time()
file_path = r"/home/rajashekar/Desktop/TS_CPU/BENEFICIARY_DATA_schemes/Mahbubnagar"
MP_Constituency = file_path.split('/')[-1]

# possible_column_names = ['mobile','contact','phone']
all_folders = os.listdir(file_path)
# beneficiary_names = ['Names','Name of the Beneficiary', 'Beneficiary Name', 'PT_NAME', 'Name', 'BENEFICIARY_NAME','NAME_IN_AADHAR', 'Farmer Name',
#                      'Name of the Beneficiary(Nominee of Deceased Farmer)']
PhoneNumbers = ['Mobile','Mobile Number', 'Contact_Number', 'Contact Number', 'CONTACT_NO','Mobile NO',
                   'Phone Number','MOBILE_NUMBER','MOBILE','Phone number','Mobile No.']
# constituency_name = 'Malkajgiri_44'

MP = pd.DataFrame()

for folder in all_folders:
    print('folder',folder)
    # if folder in ('Jadcherla','Mahbubnagar','Shadnagar','Kodangal','Makthal','Devarkadra','Narayanpet'):
    if folder != "Siddipet_33":
        fol = folder.split('_')[0]

        all_files_in_folder = os.listdir(file_path+'/'+folder)
        # print(len(all_files_phone_nums))
        cdf = pd.DataFrame()
        c = 0
        for file in all_files_in_folder:
            c+=1
            # print('file','-----------------------',file)
            # print('file',file)
            # if file.endswith('.xlsx'):
            #     fil = file.split('.xlsx')[0]
            #
            #     # print('file','ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff',file)
            #     df = pd.read_excel(file_path + '/' + folder + '/' + file)
            #     # print(df.columns)
            #     # print("ooooooooooooooooooooooooooollllllllllllllllllllllllllllllllllllllllllllllllllll",len(df))
            #     #
            #     # df.dropna(subset=["Mobile"],inplace=True)
            #     # print("A_F_Nullllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll",len(df))
            #     if 'Mobile' in df.columns:
            #
            #         def clean_mobile_number(mobile):
            #             try:
            #                 mobile_float = float(mobile)
            #                 mobile = "{:.0f}".format(mobile_float)
            #             except ValueError:
            #                 mobile = str(mobile)
            #
            #             if mobile.endswith(".0"):
            #                 mobile = mobile[:-2]
            #
            #             return mobile
            #
            #         # Assuming df is your DataFrame
            #         df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
            #
            #         df['Mobile'] = df['Mobile'].astype('str')
            #         df = df[df['Mobile'].str.isdigit()]
            #         df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
            #         df['Mobile'] = df['Mobile'].apply(
            #             lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
            #         df = df[df["Mobile"].notna()]  # Remove rows where Mobile is None
            #         # print("A_M_Vnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn",len(df))
            #
            #         df["Mobile"] = df["Mobile"].astype(int)
            #         df.drop_duplicates(subset=["Mobile"],inplace=True)
            #         df = df[["Mobile"]]
            #         # print(df)
            #         cdf = pd.concat([cdf,df],ignore_index=True)
            #         # print("Tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt",len(df))
            #         lent = len(df)
            #         print(fil,"---------------------------",lent)
            #
            #         if lent > 25000:
            #             # df.loc[25001:,:]
            #
            #             df.to_excel(
            #                 f'/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Medak/Medak_Constituencies_11_schemes_1_25000/Siddipet_Assembly_Constituency_1_25000/morethan_25000/{fil}_mobile_cleaned.xlsx',
            #                 index=False)
            #         else:
            #             # df.loc[:25000,:]
            #             df.to_excel(
            #                 f'/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Medak/Medak_Constituencies_11_schemes_1_25000/Siddipet_Assembly_Constituency_1_25000/1_25000/{fil}_mobile_cleaned.xlsx',
            #                 index=False)
            #
            #         df.to_excel(f'/home/rajashekar/Documents/Medak_Beneficiary_Scheme_wise_count_sunday_5/Siddipet/{fil}_Beneficiary_Scheme_Mobile_Numbers.xlsx',index = False)
            #
            #     else:
            #         pass
            #
            #     # df.to_excel(f'/home/rajashekar/Documents/Medak_Beneficiary_Scheme_wise_count_sunday_5/Siddipet/{fil}_Beneficiary_Scheme_Mobile_Numbers.xlsx',index = False)
            #     # df.to_excel(f'/home/rajashekar/Documents/Medak_Beneficiary_Scheme_wise_count_sunday_5/All_Medak_Mp_Scheme_files/{fil}_Beneficiary_Scheme_Mobile_Numbers.xlsx',index = False)
            # else:
            #     pass
            # # if file.endswith('.csv') and ("KCR" in file or "Dalit" in file or "Milk" in file or "Polyhouse" in file or "Sheep" in file or "Tractor" in file):
            # # if file.endswith('.csv') and ("Kalyan" in file or "Shadi" in file):
            if file.endswith('.csv') and ("ESS" in file):
            # # if file.endswith('.csv') and ("Rythubhima" in file):
            # # if file.endswith('.csv') and ("Arogya" in file or "Arogyasri" in file):
            # # if file.endswith('.csv') and ("Kantivelegu" in file):
            # if file.endswith('.csv'):
                # print("fileeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",file)
                df = pd.read_csv(file_path + '/' + folder + '/' + file, low_memory=False)
                # df = pd.read_csv(file_path + '/' + folder + '/' + file)
                fil = file.split('.csv')[0]
                # print(df.columns)

                if 'Mobile' in df.columns:
                # if all(col in df.columns for col in beneficiary_names) and all(col in df.columns for col in PhoneNumbers):
                # if all(col in df.columns for col in PhoneNumbers):

                    # print(df)
                    # print("OLllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll",len(df))

                    df.dropna(subset=["Mobile"], inplace=True)
                    # print("A_D_Nllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll",len(df))

                    def clean_mobile_number(mobile):
                        try:
                            mobile_float = float(mobile)
                            mobile = "{:.0f}".format(mobile_float)
                        except ValueError:
                            mobile = str(mobile)

                        if mobile.endswith(".0"):
                            mobile = mobile[:-2]

                        return mobile

                    # Assuming df is your DataFrame
                    df['Mobile'] = df['Mobile'].apply(clean_mobile_number)

                    df['Mobile'] = df['Mobile'].astype('str')
                    df = df[df['Mobile'].str.isdigit()]
                    df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
                    df['Mobile'] = df['Mobile'].apply(
                        lambda x: x if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
                    df = df[df["Mobile"].notna()]  # Remove rows where Mobile is None

                    df["Mobile"] = df["Mobile"].astype(int)
                    df.drop_duplicates(subset=["Mobile"], inplace=True)
                    df = df[["Mobile"]]
                    cdf = pd.concat([cdf,df],ignore_index=True)
                    # print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",len(df))
                    # print(df)
                    # lenth = len(df)
                    # print(fil,"--------------------------------------------",lenth)
                    #
                    # if lenth > 25000:
                    #     # df.loc[25001:,:]
                    #
                    #     df.to_excel(f'/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Medak/Medak_Constituencies_11_schemes_1_25000/Siddipet_Assembly_Constituency_1_25000/morethan_25000/{fil}_mobile_cleaned.xlsx',index = False)
                    # else :
                    #     # df.loc[:25000,:]
                    #     df.to_excel(f'/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Medak/Medak_Constituencies_11_schemes_1_25000/Siddipet_Assembly_Constituency_1_25000/1_25000/{fil}_mobile_cleaned.xlsx',index = False)

                    df.to_excel(f'/home/rajashekar/Desktop/TELANGANA_STATE_DAILY_DATA/Mahbubnagar/Mahbubnagar_18_28_Age_group/beneficiary_Ess/{fil}_mobile_cleaned.xlsx',index=False)

                    # df.to_excel(f'/home/rajashekar/Documents/Medak_Beneficiary_Scheme_wise_count_sunday_5/Siddipet/{fil}_Beneficiary_Scheme_Mobile_Numbers.xlsx',index=False)
                    # df.to_excel(f'/home/rajashekar/Documents/Medak_Beneficiary_Scheme_wise_count_sunday_5/All_Medak_Mp_Scheme_files/{fil}_Beneficiary_Scheme_Mobile_Numbers.xlsx',index=False)

                else :
                    pass
            else :
                pass
        # cdf.drop_duplicates(subset=["Mobile"],inplace = True)
        # cdf.dropna(inplace = True)
        # print(fol,"CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC",len(cdf))
        # MP = pd.concat([MP,cdf],ignore_index=True)
        # cdf.to_excel(f'/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/BENEFICIARY/Nizamabad/{fol}_Mobile_Numbers.xlsx',index=False)

# print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",len(MP))
# MP.drop_duplicates(subset=["Mobile"],inplace = True)
# MP.dropna(inplace=True)
# l = len(MP)
# if l > 1000000:
#     first_part = MP.iloc[:1000000, :]
#     second_part = MP.iloc[1000001:, :]
#
#     # first_file_path = f"/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/Beneficiary_Mp/Chevella/{MP_Constituency}_MP_Beneficiary_Mobile_Numbers_Part1.xlsx"
#     first_part.to_excel(first_file_path, index=False)
#
#     print("............................................first_part")
#
#     # second_file_path = f"/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/Beneficiary_Mp/Chevella/{MP_Constituency}_MP_Beneficiary_Mobile_Numbers_Part2.xlsx"
#     second_part.to_excel(second_file_path, index=False)
#     print("............................................second_part")
# else:
#     # file_path = f"/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/Beneficiary_Mp/Chevella/{MP_Constituency}_MP_Beneficiary_Mobile_Numbers.xlsx"
#     MP.to_excel(file_path, index=False)
#     print("file........................Stored_Successfully")
# # MP.to_excel(f"/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/Beneficiary_Mp/Medak/Medak_Beneficiary_Mp_Mobile_Numbers.xlsx",index = False)
# for i in all_folders:
#     print(i)