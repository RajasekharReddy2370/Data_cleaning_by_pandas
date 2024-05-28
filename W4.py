import pandas as pd
import os
import NUmpy_PRAC
import time

start_time = time.time()

def get_mobile_numbers(folder1_path, folder2_path):
    all_mobiles = []
    for file1, file2 in zip(os.listdir(folder1_path), os.listdir(folder2_path)):
        file1_path = os.path.join(folder1_path, file1)
        file2_path = os.path.join(folder2_path, file2)

        if os.path.isfile(file1_path) and os.path.isfile(file2_path):
            df1 = pd.read_excel(file1_path)
            df2 = pd.read_excel(file2_path)

            if 'Mobile' in df1.columns and 'Mobile' in df2.columns:
                mobiles1 = df1['Mobile'].dropna().astype(str).tolist()
                mobiles2 = df2['Mobile'].dropna().astype(str).tolist()

                # Concatenate mobile numbers from both files
                all_mobiles.extend(mobiles1)
                all_mobiles.extend(mobiles2)

    return all_mobiles


def get_unique_random_mobiles(folder1_path, folder2_path, num_mobiles):
    all_mobiles = get_mobile_numbers(folder1_path, folder2_path)
    unique_mobiles = set(all_mobiles)

    if len(unique_mobiles) < num_mobiles:
        raise ValueError("Not enough unique mobile numbers available.")

    # Randomly select unique mobile numbers
    selected_mobiles = random.sample(unique_mobiles, num_mobiles)

    return selected_mobiles


# Example usage
folder1_path = "/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/BENEFICIARY/Medak"
folder2_path = "/home/rajashekar/Desktop/TS_CPU/MOBILE_NUMBERS/VOTER/Medak"
num_mobiles = 100000

selected_mobiles = get_unique_random_mobiles(folder1_path, folder2_path, num_mobiles)
print(len(selected_mobiles))



