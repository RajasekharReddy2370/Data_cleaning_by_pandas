import pandas as pd

from cls import name
from cls import mobile

df = pd.read_excel(r"/home/rajashekar/Documents/Thursday_2_may.xlsx",usecols=["Mobile"])
print(df)

n = name()

m = mobile()

p_n = n.print_name("Raja")
print(p_n)

c_df = m.clean_mobile_numbers(df)
print(c_df)

