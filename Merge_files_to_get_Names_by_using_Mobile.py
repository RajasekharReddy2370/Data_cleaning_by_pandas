# ############################################################### Getting Names through Names #######################################
#
# import pandas as pd
# from fuzzywuzzy import process
#
# # Sample DataFrame A
# A = pd.DataFrame({
#     'Names': ['Alice', 'cat Bob', 'Charlie David'],
#     'Mobile': ['1234567890', '2345678901', '3456789012']
# })
#
# # Sample DataFrame B
# B = pd.DataFrame({
#     'Teachernames': ['Alice', 'Eve', 'Bob cat', 'david charlie']
# })
#
# # Convert both Names and Teachernames to lowercase
# A['Names'] = A['Names'].str.lower()
# B['Teachernames'] = B['Teachernames'].str.lower()
#
# # Create a list to hold matched names and their corresponding mobile numbers
# matched_names = []
# matched_mobiles = []
#
# # Loop through each Teachernames to find best matches in Names
# for teacher in B['Teachernames']:
#     match, score, _ = process.extractOne(teacher, A['Names'])  # Unpacking three values
#     if score >= 80:  # Adjust threshold as needed
#         matched_names.append(teacher)
#         matched_mobiles.append(A.loc[A['Names'] == match, 'Mobile'].values[0])
#
# # Create the result DataFrame
# result = pd.DataFrame({'Teachernames': matched_names, 'Mobile': matched_mobiles})
# # Convert columns to title case
# result['Teachernames'] = result['Teachernames'].str.title()
# result['Mobile'] = result['Mobile'].str.title()  # This line isn't necessary for Mobile, but included for consistency
# print(result)


############################################################################################################################

################################################# GETTING NAMES Through MOBILE NUMBER #####################################

import pandas as pd

# Sample DataFrame A
A = pd.DataFrame({
    'Names': ['Alice', 'cat Bob', 'Charlie David'],
    'Mobile': ['1234567890', '2345678901', '3456789012']
})

# Sample DataFrame B
B = pd.DataFrame({
    'Mobile': ['5555555555', '2345678901', '3456789012']
})

# Convert Mobile columns to string for comparison
A['Mobile'] = A['Mobile'].astype(str)
B['Mobile'] = B['Mobile'].astype(str)

# Filter DataFrame A to include only rows with Mobile numbers that match those in DataFrame B
matched_df = A[A['Mobile'].isin(B['Mobile'])]

# Reset index of the result DataFrame for cleaner output
matched_df.reset_index(drop=True, inplace=True)

# Print the result
print(matched_df)
