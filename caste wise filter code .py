import pandas as pd

# Load the Excel file into a DataFrame
file_path = '/home/rajashekar/Desktop/AP_CPU/G_W_94_DATA/GUNTUR_WEST_94_FINAL_DATA.xlsx'
df = pd.read_excel(file_path)

# List of common Muslim names (both first names and last names)
common_muslim_names = ['Ahmed','KHAJA','Muhammad','MOHAMMED','Syed','Hussain','Khan','Abdullah','Mohammad','Mohammed','Sayyad','Shaik','SHAIK','MOHD','Md','Pasha','KHAN','Mohd','Ali','Mohmad','Shek','Mohmmad','Ahmed','Ullah','Mahmad','Uddin','Mahammad','Mohemmad','Sayed','Isak','Mahmad','Saieed','Alee','Abdul','BAIG','M D','uddin'] 
# Function to check if a name is common among Muslims
# def is_potential_muslim(FM_NAME_EN, LASTNAME_EN):
#     return FM_NAME_EN in common_muslim_names or LASTNAME_EN in common_muslim_names

def is_potential_muslim(FM_NAME_EN):
    return FM_NAME_EN in common_muslim_names

# Apply the function and filter the DataFrame
# filtered_df = df[df.apply(lambda row: is_potential_muslim(row['FM_NAME_EN'], row['LASTNAME_EN']), axis=1)]
filtered_df = df[df.apply(lambda row: is_potential_muslim(row['Names']), axis=1)]

# Create a new DataFrame with only first name and last name columns
output_df = filtered_df[["Names","Telugu_Names","Mobile"]]

output_file_path = 'data1.xlsx'

# Save the resulting DataFrame to a text file
output_df.to_csv(output_file_path, index=False, sep='\t')  # You can use a different separator if needed

print(f"Output saved to {output_file_path}")