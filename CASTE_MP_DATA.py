
import pandas as pd


df = pd.read_excel(r"/home/rajashekar/Desktop/MAHBUBNAGAR_CASTE_WISE_DATA/MAHBUBNAGAR_VOTER_DATA_CONSTITUENCIES/Makthal-77-AC- iToC Voter Data_cleaned_Data.xlsx")

constituency = "Makthal"

print("ORIGINAL LENGTH ...................................", len(df))

df["Names"] = df["Names"].astype(str)


def add_space_in_dot(name):
    if "." in name:
        name = name.replace(".", " ")
    return name.strip()


df['Names'] = df['Names'].apply(add_space_in_dot)

# common_Reddy_names = ['Reddy', 'Redd', 'Reddi', 'Redde', 'Redi', 'Redy','Red']

common_muslim_names = [
    'Ahmed', 'KHAJA', 'Muhammad', 'MOHAMMED', 'Syed', 'Hussain', 'Khan', 'Abdullah', 'Mohammad', 'Mohammed',
    'Sayyad', 'Shaik', 'SHAIK', 'MOHD', 'Md', 'Pasha', 'KHAN', 'Mohd', 'Ali', 'Mohmad', 'Shek', 'Mohmmad',
    'Ullah', 'Mahmad', 'Uddin', 'Mahammad', 'Mohemmad', 'Sayed', 'Isak', 'Mahmad', 'Saieed', 'Alee', 'Abdul',
    'BAIG', 'M D', 'uddin', 'Imran', 'Aisha', 'Fatima', 'Omar', 'Zainab', 'Bilal', 'Khadija', 'Zahra', 'Ibrahim',
    'Sana', 'Yusuf',
    'Safiya', 'Rahim', 'Farida', 'Salman', 'Amina', 'Hamza', 'Layla', 'Rashid', 'Sumaya', 'Tariq', 'Fatemeh',
    'Nadia', 'Mustafa', 'Sara', 'Jamil', 'Mariam', 'Hadi', 'Ayesha', 'Aliya', 'Karim', 'Nasir', 'Noor', 'Musa',
    'Hasan', 'Hana', 'Malik', 'Amina', 'Yasir', 'Hadiya', 'Talha', 'Saida', 'Jafar', 'Sabira', 'Iman', 'Nabil',
    'Amina', 'Yusuf', 'Leila', 'Tahir', 'Farida', 'Khalid', 'Aaliyah', 'Zakariya', 'Fatimah', 'Jabir', 'Safi',
    'Sarina', 'Najib', 'Layla', 'Amin', 'Dina', 'Rahman', 'Inaya', 'Najla', 'Rizwan', 'Asma', 'Wahid', 'Jamila',
    'Kareem', 'Ayesha', 'Faisal', 'Yasmine', 'Tariq', 'Nadia', 'Shakir', 'Nour', 'Jamal', 'Huda', 'Yahya',
    'Rukhsar',
    'Naima', 'Bashir', 'Shabnam', 'Adnan', 'Arifa', 'Ilyas', 'Zeba', 'Junaid', 'Farah', 'Asif', 'Samina', 'Ismail',
    'Nasreen', 'Yaqub', 'Gulzar', 'Rukhsar', 'Rizwana', 'Arshad', 'Rukaiya', 'Feroz', 'Nafisa', 'Tanveer', 'Sahar',
    'Feroze', 'Yasmin', 'Javed', 'Parveen', 'Qasim', 'Zarina', 'Arif', 'Nazia', 'Waseem', 'Fazila', 'Kamran',
    'Zubaida',
    'Yusuf', 'Amina', 'Bilquis', 'Ilyas', 'Fariha', 'Rashida', 'Tariq', 'Nusrat', 'Sohail', 'Fahim', 'Ayesha',
    'Fareed',
    'Rukhsar', 'Ghulam', 'Arzoo', 'Zubair', 'Rukaiya', 'Aftab', 'Alia', 'Qamar', 'Zeenat', 'Arman', 'Kausar',
    'Sultan',
    'Parveen', 'Rafi', 'Aali', 'Zoya', 'Afzal', 'Nashit', 'Rehana', 'Saif', 'Najma', 'Adil', 'Yasmeen', 'Imtiaz',
    'Alisha',
    'Sarwar', 'Fiza', 'Wahab', 'Nashra', 'Irfan', 'Saba', 'Naveed', 'Saima', 'Basharat', 'Yasir', 'Rabia', 'Shoaib',
    'Zubaida',
    'Zaheer', 'Shahida', 'Feroz', 'Yumna', 'Aqil', 'Shehnaz', 'Mushtaq', 'Salma', 'Aftab', 'Sabah', 'Rameez',
    'Rukhsana', 'Ariz',
    'Arshiya', 'Naveeda', 'Qais', 'Arshia', 'Mujeeb', 'Iram', 'Saifullah', 'Sahira', 'Jawad', 'Atiya',
    'Arif',
    'Naheed', 'Aslam', 'Saher', 'Basit', 'Samira', 'Tanveer', 'Asiya', 'Zafran', 'Khair', 'Shazia', 'Nawab',
    'Tanzila',
    'Waheed', 'Farkhanda', 'Azeem', 'Salima', 'Talat', 'Sikandar', 'Dilshad', 'Ismat', 'Umar', 'Maimoona', 'Younus',
    'Mehnaz']

common_muslim_names_lower = [name.lower() for name in common_muslim_names]


# Function to check if any part of the name matches the common SC/ST names
def check_common_muslims(name):
    name_parts = name.split()
    for part in name_parts:
        if part.lower() in common_muslim_names_lower:
            return True
    return False


# Apply the function to the "Names" column to create a boolean mask
mask = df['Names'].apply(check_common_muslims)

# Filter the DataFrame using the mask
muslim_df = df[mask].copy()  # Make a copy to avoid SettingWithCopyWarning

# Convert "Names" column to title case
muslim_df.loc[:, "Names"] = muslim_df["Names"].astype(str)

# Convert "Names" column to title case
muslim_df.loc[:, "Names"] = muslim_df["Names"].str.title()
print(muslim_df)

print("muslims_length.............................", len(muslim_df))

muslim_df.to_excel(
    f"/home/rajashekar/Desktop/MAHBUBNAGAR_CASTE_WISE_DATA/Mahbubnagar_Voter_CASTE/MAHBUBNAGAR_MUSLIMS/{constituency}_muslims_Data.xlsx",
    index=False)