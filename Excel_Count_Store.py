
import os
import pandas as pd

# Path to the folder containing the files
folder_path = "/home/rajashekar/Desktop/TS_CPU/Assembly_unique_concat_files/Medak"

# Get a list of all files in the folder
file_names = os.listdir(folder_path)

# Create lists to store file names and their lengths
names = []
lengths = []

# Iterate through the files
for file_name in file_names:
    f_n = file_name.split('_')[0]
    names.append(f_n)
    df = pd.read_excel(os.path.join(folder_path, file_name))
    l = len(df)
    lengths.append(l)

# Create DataFrame from lists
dff = pd.DataFrame({"Names": names, "Cnt": lengths})
print(dff)
