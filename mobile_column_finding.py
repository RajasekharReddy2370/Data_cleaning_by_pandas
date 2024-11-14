import pandas as pd

# Load the Excel file
df = pd.read_excel(r"/home/rajashekar/Downloads/687000 data contants karimnagar.xlsx")
# print(df.head)
# pd.set_option('display.max_rows', None)


# pd.set_option('display.max_columns', None)   # Show all columns

# Print the DataFrame

print(df.info())
# # Define a function to check if a value is a valid mobile number
# def is_mobile_number(value):
#     # Check if the value is a string of 10 digits starting with 6, 7, 8, or 9
#     return isinstance(value, str) and value.isdigit() and len(value) == 10 and value[0] in "6789"
#
# # Initialize mobile_df as an empty DataFrame
# mobile_df = pd.DataFrame()
#
# # Loop through columns to find the mobile number column
# for col in df.columns:
#     # Check if the column has valid mobile numbers in all rows
#     if df[col].apply(is_mobile_number).all():
#         df = df.rename(columns={col: 'MOBILE'})  # Rename the column to 'MOBILE'
#         mobile_df = df[['MOBILE']]  # Retrieve only the 'MOBILE' column
#         break
#
# # Display the DataFrame with only the MOBILE column, or a message if no column is found
# if not mobile_df.empty:
#     print(mobile_df)
# else:
#     print("No mobile number column found.")



