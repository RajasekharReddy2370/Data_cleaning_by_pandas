import pandas as pd

# Load the Excel file
df = pd.read_excel(r"/home/rajashekar/Downloads/Manthani.xlsx")

# Split the 'Names' column based on the first whitespace
df[['Firstname', 'Lastname']] = df['Names'].str.split(' ', n=1, expand=True)

df.to_excel("Manthani_Firstname_and_Lastname_mobiles.xlsx",index = False)


