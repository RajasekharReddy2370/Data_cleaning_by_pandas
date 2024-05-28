import pandas as pd
import json

constituency = 'Hyderabad'

# Load the original JSON file
with open(r'/home/rajashekar/WORK/Hyderabad_messages.json', 'r') as json_file:
    json_data = json.load(json_file)

# Get the number of keys and total number of values in the original JSON data
num_keys_original = len(json_data.keys())
print("Number of keys in original JSON data:", num_keys_original)

total_values_original = sum(len(values) for values in json_data.values())
print("Total number of values in original JSON data:", total_values_original)

# Read the DataFrame
df = pd.read_excel(r'/home/rajashekar/Desktop/TS_CPU/LOD_to telugu_names/Hyderabad/Hyderabad_ENG_to_TEL_HIN.xlsx', usecols=['Names', 'Mobile'])

# Group mobile numbers by name and convert to dictionary with values as lists
df_dict = df.groupby('Names')['Mobile'].apply(list).to_dict()

# Update the original JSON data with the new data from the DataFrame
json_data.update(df_dict)

# Write the updated JSON data to a new JSON file
output_json_file = f'{constituency}_updated_json_data.json'  # Provide the desired filename here
with open(output_json_file, 'w') as file:
    json.dump(json_data, file, indent=4)

print(f"Updated JSON data has been saved to '{output_json_file}'")

# Get the number of keys and total number of values in the updated JSON data
num_keys_updated = len(json_data.keys())
print("Number of keys in updated JSON data:", num_keys_updated)

total_values_updated = sum(len(values) for values in json_data.values())
print("Total number of values in updated JSON data:", total_values_updated)
